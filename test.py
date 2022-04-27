from ctypes import *

int8p = c_int * 8
dll = CDLL("./lib.dll")
val = int8p.in_dll(dll, "a")
for i in val:
    print(i, end=" ")
print()
val[0] = 10
for i in val:
    print(i, end=" ")
print()
