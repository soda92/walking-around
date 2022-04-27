from ctypes import *

t = c_int(0x10)
pt = pointer(t)
pt_casted = cast(pt, POINTER(c_byte))
pt_casted[0] = 0x10
pt_casted[1] = 0x11
print(t)
