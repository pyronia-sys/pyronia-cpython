'''
Generate 100 test modules used to create an n-deep callstack
for benchmarking.

Author: Marcela S. Melara
'''

test_file_prefix = "test_mod_"
n = 99

for i in range (n, 1, -1):
    test_file = test_file_prefix+str(i)+".py"
    f = open("test_modules/"+test_file, 'a+')
    #f.write("import "+test_file_prefix+str(i-1)+"\n")
    f.write("\n")
    f.write("def connect():\n")
    f.write("\t"+test_file_prefix+str(i-1)+".connect()\n")
    f.close()
