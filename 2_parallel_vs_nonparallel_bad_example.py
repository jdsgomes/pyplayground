import cProfile
import pstats
import threading
import time

def cocky_function():
    print('I\'m fast!')

def run_cocky_function1000x_serial():
    for i in range(1000):
        cocky_function()

def run_cocky_function1000x_parallel():
    threads = []
    for i in range(1000):
        thread = threading.Thread(target=cocky_function)
        thread.start()
        threads.append(thread)
    for thread in threads:
        thread.join()

def main():
    print('==== Running 1000x cocky function in a serial fashion ====')
    cProfile.run('run_cocky_function1000x_serial()', filename='serial')
    print('==== Running 1000x cocky function in parallel ====')
    cProfile.run('run_cocky_function1000x_parallel()', filename='parallel')
    print('===== Serial statistics: ====')
    py_stats = pstats.Stats('serial')
    py_stats.print_stats('serial')
    print('===== Parallel statistics: ====')
    py_stats2 = pstats.Stats('parallel')
    py_stats2.print_stats('parallel')
    print('All done!')

    
if __name__ == "__main__":
    main()
