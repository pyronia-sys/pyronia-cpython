import sys
import file_read
import util

n = 10
i = 10000

def set_experiment(d):
    if d == 0:
        return file_read.read
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

if __name__ == '__main__':
    file_read.set_experiment(sys.argv[2])
    depth = int(sys.argv[1])
    read_func = set_experiment(depth)
    for x in range(0, n):
        file_read.total_elapsed = 0
        for y in range(0, i):
            read_func()
        util.print_experiment_microsecs(depth, util.avg(file_read.total_elapsed, i))
