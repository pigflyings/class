import numpy as np
a = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype=np.float32)
print("a=\n",a)
print("a.dtype=",a.dtype)
print("type(a.dtype)=",type(a.dtype))
print("a.ndim=",a.ndim)
print("a.shape=",a.shape)
print("a.strides=",a.strides)
print("a.data=",a.data)
print("a.nbytes=",a.nbytes)