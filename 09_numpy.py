import numpy

#input 2Darray NXM.
N, M = map(int,input().split())
arr = numpy.array([input().split() for i in range(N)], int)
#sum of numpy array along axis 0
sum_array = numpy.sum(arr, axis = 0)

#product of the sum array
print(numpy.prod(sum_array))