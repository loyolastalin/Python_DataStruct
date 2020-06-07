import ctypes
import sys
def make_array(c): # nonpublic utitity
#Return new array with capacity c.”””
    return (c * ctypes.py_object)()
    
v = make_array(2)
v[0] ='1as'
v[1] ='2asd' 
for item in v:
    print(item)
print(type(v))
print(sys.getsizeof(v))
z = ctypes.py_object()
z = 'asdasdasd'

print(z)