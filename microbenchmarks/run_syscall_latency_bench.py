import sys
import syscalls_bench
import util

n = 1
i = 10000

def set_experiment(d):
    if d == 0:
        return syscalls_bench.read
    elif d == 25:
        import test_mod_24
        return test_mod_24.read
    elif d == 50:
        import test_mod_49
        return test_mod_49.read
    elif d == 75:
        import test_mod_74
        return test_mod_74.read
    elif d == 100:
        import test_mod_99
        return test_mod_99.read
    else:
        import test_mod_1
        return test_mod_1.read

def set_net_experiment(d):
    if d == 0:
        return syscalls_bench.connect
    elif d == 25:
        import test_mod_24
        return test_mod_24.connect
    elif d == 50:
        import test_mod_49
        return test_mod_49.connect
    elif d == 75:
        import test_mod_74
        return test_mod_74.connect
    elif d == 100:
        import test_mod_99
        return test_mod_99.connect
    else:
        import test_mod_1
        return test_mod_1.connect


if __name__ == '__main__':
    '''
    file_size = sys.argv[2]
    file_read.set_experiment(file_size)
    '''
    depth = int(sys.argv[1])
    '''
    read_func = set_experiment(depth)
    '''
    connect_func = set_net_experiment(depth)
    for x in range(0, n):
        syscalls_bench.total_elapsed = 0
        for y in range(0, i):
            #read_func()
            connect_func()
        util.save_conn_latency(depth, util.avg(syscalls_bench.total_elapsed, i))
        #util.print_experiment_microsecs(depth, util.avg(file_read.total_elapsed, i))
