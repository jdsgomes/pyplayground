import cProfile
import pstats
import threading
import time

def slow_function():
    print('Thread is going to sleep')
    time.sleep(5)
    print('Thread woke up')

def slow_function_daemon():
    print('Daemon is going to sleep')
    time.sleep(6)
    print('Daemon woke up')

def main():
    t = threading.Thread(target=slow_function)
    d = threading.Thread(target=slow_function_daemon)
    d.setDaemon(True)
    t.start()
    d.start()
    
if __name__ == "__main__":
    main()
