import cProfile
import pstats
import threading
import time

def slow_function():
    time.sleep(5)

def run_slow_function2x_serial():
    slow_function()
    slow_function()

def run_slow_function2x_parallel():
    thread_a = threading.Thread(target=slow_function)
    thread_b = threading.Thread(target=slow_function)
    thread_a.start()
    thread_b.start()
    thread_a.join()
    thread_b.join()

def main():
    print('==== Running 2x slow function in a serial fashion ====')
    cProfile.run('run_slow_function2x_serial()', filename='serial')
    print('==== Running 2x slow function in parallel ====')
    cProfile.run('run_slow_function2x_parallel()', filename='parallel')
    print('===== Serial statistics: ====')
    py_stats = pstats.Stats('serial')
    py_stats.print_stats('serial')
    print('===== Parallel statistics: ====')
    py_stats2 = pstats.Stats('parallel')
    py_stats2.print_stats('parallel')
    print('All done!')

    
if __name__ == "__main__":
    main()
