'''
Run n trials of i iterations of a 1K file read.

Author: Marcela S. Melara
'''
import time
import sys

FILENAME = 'test1K.txt'
READLEN = 1024
n = 10
i = 10000
total_elapsed = 0
trials = []

def set_experiment(expt):
    global FILENAME
    global READLEN
    if expt == '10K':
        FILENAME = 'test10K.txt'
        READLEN = 10240
    elif expt == '100K':
        FILENAME = 'test100K.txt'
        READLEN = 102400
    elif expt == '1M':
        FILENAME = 'test1M.txt'
        READLEN = 1048576
    elif expt == '10M':
        FILENAME = 'test10M.txt'
        READLEN = 10485760
    elif expt == '100M':
        FILENAME = 'test100M.txt'
        READLEN = 104857600

def read():
    global total_elapsed
    f = open(FILENAME, 'rb')
    start = time.clock()
    tmp = f.read(READLEN)
    diff = time.clock() - start
    total_elapsed += diff
    f.close()

def avg(total, reps):
    return total / reps

def print_stats(expt, average):
    print "%d, %.3f\n" % (expt, (average*1000000))

if __name__ == '__main__':
    set_experiment(sys.argv[1])
    for x in range(0, n):
        total_elapsed = 0
        for y in range(0, i):
            read()
        print_stats(READLEN, avg(total_elapsed, i))
    # only compute avg for last half of trials since
    # the read times needs a few iterations to converge
    #print_stats(avg(sum(trials[(n/2):]), (n/2)), (n/2))
