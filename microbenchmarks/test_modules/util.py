def avg(total, reps):
    return total / reps

def print_experiment_microsecs(expt, average):
    print "%d, %.3f" % (expt, (average*1000000))
