import numpy

#input the dimensions NXM
N, M = map(int, input().split())
#input the array elements
arr = numpy.array([input().split() for i in range(N)], int)
#print the min of the array in axis 1 and then max of it
print(numpy.max(numpy.min(arr,axis = 1)))