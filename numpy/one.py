import numpy as np
arr=np.array([[1,2,32,4]],np.int64)
# arr[0,1]
# print(arr[0,1])
# print(arr.shape)
# print(arr.dtype)
arr[0,1]=26
# print(arr)
# arrat creation methods
# 1. Conversion from ther python structures
a1=np.array([[1,2,3],[2,4,6],[3,5,7]])
# print(a1)
# print(a1.dtype)
# print(a1.shape)
# print(a1.size)

zeros=np.zeros((2,5))
# print(zeros)
rng=np.arange(15)
# print(rng)
lspace=np.linspace(1,4,4)
# print(lspace)
emp=np.empty((4,6))
# print(emp)
elike=np.empty_like(lspace)
# print(elike)
ide=np.identity(45)
# print(ide)
# print(ide.shape)

a2=np.arange(99)
# print(a2)
arr=a2.reshape(3,33)
# print(arr)
a2.ravel()
# print(a2.shape)


x=[[1,2,3],[4,5,6],[7,1,0]]
ar=np.array(x)
print(ar)
s=ar.sum(axis=1)
# print(s)
tr=ar.T
# print(tr)
print(ar.ndim)
print(ar.nbytes)

one=np.array([1,2,4,34,5])
print(one.argmax())
print(one.argmin())
print(one.argsort())
print(ar.argmax(axis=1))
# print(ar.argsort(axis=0))
# print(ar.reshape(9,1))


a2=np.array([[1,2,1],[4,0,6],[8,1,0]])
print(ar+a2)
print(ar.sum())

print(np.where(ar>5))
print(type(np.where(ar>5)))
print(np.count_nonzero(ar))


import sys
pyar=[0,2,4,5]
npar=np.array(pyar)
print(sys.getsizeof(1)*len(pyar))
print(npar.itemsize*npar.size)