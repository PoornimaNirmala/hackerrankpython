import numpy

N, M, P = map(int,input().split())

arr1 = numpy.array([input().split() for i in range(N)],int)
arr2 = numpy.array([input().split() for i in range(M)],int)
print(numpy.concatenate((arr1,arr2),axis = 0))