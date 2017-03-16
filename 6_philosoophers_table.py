import cProfile
import pstats
import threading
import time

# Credits: http://dabeaz.blogspot.co.uk/2009/11/python-thread-deadlock-avoidance_20.html

def philosopher(left, right):
    while True:
        forks = sorted((left, right), key=lambda x: id(x))
        with forks[0]:
            with forks[1]:
                print str(id(threading.currentThread())) + 'is eating'

def main():
    n_forks = 5
    forks = [threading.Lock() for n in range(n_forks)]

    philosophers = [threading.Thread(target=philosopher,
                                     args = (forks[n],forks[(n+1) % n_forks]))
                    for n in range(n_forks)]

    for p in philosophers:
        p.start()

if __name__ == "__main__":
    main()
