from statistics import mean, median, stdev
import json
from basic_stats import calc_percent

app_path = '/Users/marcela/Research/lib-isolation/cpython/'

apps = ['hello', 'twitterPhoto', 'alexa', 'plant_watering']

outfile = 'benchmarks/app_latency_pyr.data'

stats = dict()
stats['min'] = []
stats['mean'] = []
stats['median'] = []
stats['max'] = []
stats['stddev'] = []
stats['pct'] = []
for a in apps:
    f = open(app_path+'benchmarks/'+a+'/'+a+'-latency-pyr.data', 'r')
    latencies = f.readlines()
    f.close()
    exec_times = []
    e2e_exec_times = []
    max_dep_depth = []
    for l in latencies:
        run_data = l.split(',')
        exec_times.append(float(run_data[0].strip()))
        e2e_exec_times.append(float(run_data[1].strip()))
        max_dep_depth.append(int(run_data[2].strip()))

    stats['min'].append((("%.2f" % min(exec_times)), ("%.2f" % min(e2e_exec_times)), ("%d" % min(max_dep_depth))))
    stats['mean'].append((("%.2f" % mean(exec_times)), ("%.2f" % mean(e2e_exec_times)), ("%.2f" % mean(max_dep_depth))))
    stats['median'].append((("%.2f" % median(exec_times)), ("%.2f" % median(e2e_exec_times)), ("%.2f" % median(max_dep_depth))))
    stats['max'].append((("%.2f" % max(exec_times)), ("%.2f" % max(e2e_exec_times)), ("%d" % max(max_dep_depth))))
    stats['stddev'].append((("%.2f" % stdev(exec_times)), ("%.2f" % stdev(e2e_exec_times)), ("%.2f" % stdev(max_dep_depth))))
    stats['pct'].append(("%.2f" % calc_percent(mean(e2e_exec_times), mean(exec_times))))

out = open(app_path+outfile, 'w+')
json.dump(stats, out)
out.close()
