import os

data_dir = os.path.expanduser('~')+'/cpython/microbenchmarks/data'

def avg(total, reps):
    return total / reps

def print_experiment_microsecs(expt, average):
    print "%d, %.3f" % (expt, (average*1000000))
    
def save_open_latency(expt, fsize, average):
    f = open(data_dir+'/open-latency-'+str(fsize)+'-pyr-nosi.csv', 'a+')
    f.write("%d, %.3f\n" % (expt, (average*1000000)))
    f.close()

def save_conn_latency(expt, average):
    f = open(data_dir+'/connect-latency-pyr.csv', 'a+')
    f.write("%d, %.3f\n" % (expt, (average*1000000)))
    f.close()
