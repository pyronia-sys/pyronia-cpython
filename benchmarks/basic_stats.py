import json
from mem_overhead import read_mprofile_file

def calc_diff(new, orig):
    return float(new)-float(orig)

def calc_percent(new, orig):
    return (calc_diff(new, orig))/float(orig)

def calc_multi(new, orig):
    return float(new)/float(orig)

nopyr_data = dict()
pyr_data = dict()
with open('app_latency_pyr.data', 'r') as fp:
    pyr_data = json.load(fp)
with open('app_latency_nopyr.data', 'r') as fp:
    nopyr_data = json.load(fp)

apps = ['hello', 'twitterPhoto', 'alexa', 'plant_watering']

# gather pyr and no_pyr lists
pyr_means = [ float(a[0])/1000000.0 for a in pyr_data['mean'] ]
pyr_e2e_means = [ float(a[1])/1000000.0 for a in pyr_data['mean'] ]

nopyr_means = [ float(a[0])/1000000.0 for a in nopyr_data['mean'] ]
nopyr_e2e_means = [ float(a[1])/1000000.0 for a in nopyr_data['mean'] ]

print("Mean e2e overhead:")
for i in range(0, len(apps)):
    print("- %s: %.2f" % (apps[i], calc_multi(pyr_e2e_means[i], nopyr_e2e_means[i])))

print("Mean module-only overhead:")
for i in range(0, len(apps)):
    print("- %s: %.2f" % (apps[i], calc_multi(pyr_means[i], nopyr_means[i])))

print("Max median memory overhead:")
for i in range(1, len(apps)-1):
    pyr_mem_dict = read_mprofile_file(apps[i]+'/mprofile_'+apps[i]+'-medians-pyr.dat')
    nopyr_mem_dict = read_mprofile_file(apps[i]+'/mprofile_'+apps[i]+'-medians-nopyr.dat')
    print("- %s: %.2f MB" % (apps[i], calc_diff(max(pyr_mem_dict['mem_usage']), max(nopyr_mem_dict['mem_usage']))))
