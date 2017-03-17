import cProfile
import pstats
import threading
from multiprocessing.dummy import Pool as ThreadPool
import time
import random
import numpy as np

def slow_function(n):
    time.sleep(n)

def run_slow_functions_80x_parallel():
    sleep_ns = [random.random()*3 for x in range(80)]
    mean_sleep = np.mean(sleep_ns)
    print('Mean sleeping time per function call = %f' % mean_sleep)
    print('Total sleeping time = %f' % (mean_sleep*80))
    print('Ideal world parallel time = %f' % (mean_sleep*10))
    pool = ThreadPool(8)
    pool.map(slow_function, sleep_ns)
    pool.close()
    pool.join()

def main():
    print('==== Running 80x slow function in parallel ====')
    cProfile.run('run_slow_functions_80x_parallel()', filename='parallel')
    print('\n===== Parallel statistics: ====')
    py_stats2 = pstats.Stats('parallel')
    py_stats2.print_stats('parallel')
    print('All done!')

    
if __name__ == "__main__":
    main()
