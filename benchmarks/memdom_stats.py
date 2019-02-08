from statistics import mean, median, stdev
import json
import os

data_path = os.path.expanduser('~')+'/Research/lib-isolation/cpython/'

apps = ['hello', 'twitterPhoto', 'alexa', 'plant_watering']

outfile = 'benchmarks/app_memdom.data'

runs = 25

stats = dict()
stats['min'] = []
stats['mean'] = []
stats['median'] = []
stats['max'] = []
stats['total_doms'] = []
stats['interp_doms'] = []
for a in apps:
    print("Analyzing app "+a)
    total_memdoms = 0
    total_interp_doms = 0
    memdom_allocs = []
    for i in range(0, runs):
        f = open(data_path+'benchmarks/'+a+'/'+a+'-memdom-'+str(i)+'.data', 'r')
        memdom_data = [l.strip() for l in f.readlines()]
        f.close()
        # for apps that print out text, we need to skip it
        ctr = 0
        while not memdom_data[ctr].isdigit():
            ctr += 1
        memdom_data = memdom_data[ctr:]
        total_interp_doms = int(memdom_data[1])+1
        total_memdoms = int(memdom_data[0])+total_interp_doms
        memdom_allocs = [ int(d) for d in memdom_data[2:] ]

        if len(memdom_allocs) != total_memdoms:
            print("Mismatch in total memdoms and recorded allocs (run "+str(i)+")")
            exit(-1)

    stats['min'].append("%.d" % min(memdom_allocs))
    stats['mean'].append("%.2f" % mean(memdom_allocs))
    stats['median'].append("%.2f" % median(memdom_allocs))
    stats['max'].append("%d" % max(memdom_allocs))
    stats['total_doms'].append("%d" % total_memdoms)
    stats['interp_doms'].append("%d" % total_interp_doms)

out = open(data_path+outfile, 'w+')
json.dump(stats, out)
out.close()
