import os

print("---- Attack testing ----")

os.system("echo I am the legit call to os.system")

# attack 1: this will actually execute an `ls` command
import attacklib

# attack 2: this will replace the argument in the stack frame
attacklib.newprint("hello, world")

# attack 3: this will jump to a different location in the source code
attacklib.coolprint("hallo!")

# attack 4: this will actually use attacklib's os.system
os.system("echo hello!")

# attack 5: this will replace the argument in the stack frame from a native library
attacklib.newprint1("hi there")

# attack 6: this uses reflection to change the value of a python global variable
# from a native library
x = 3
res = attacklib.add_3(x)
print("Adding 3 to "+str(x)+"; want "+str(x+3)+", get "+str(res))

print("\n---- Memory interaction testing ----")

import memtestlib

# test 1: A native lib shouldn't be able to change the value of an
# immutable Python object (corresponds to pass-by-value)
print("Trying to change the value of an immutable object (expect AssertionError if the change succeeds)")
print("Adding 4 to "+str(x)+"; want "+str(x+4)+", get "+str(memtestlib.add_4(x)))

# test 2: A native lib should be able to change the value of a
# mutable Python object (corresponds to pass-by-reference)
print("Trying to change the value of a mutable object (expect AssertionError if the change fails)")
print("Adding 5 to "+str(x)+"; want "+str(x+5)+", get "+str(memtestlib.add_5(x)))

# test 3: Python should be able to change the value of a native global
print("Accessing a native global variable: ")
print("Adding 12 to "+str(x)+"; want "+str(x+12)+", get "+str(memtestlib.add_12(x)))
