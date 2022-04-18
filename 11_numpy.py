import numpy

N, M = map(int, input().split())
arr = numpy.array([input().split() for i in range(N)], int)
print(numpy.mean(arr, axis = 1))
print(numpy.var(arr, axis = 0))

numpy.set_printoptions(legacy='1.13')
print(numpy.std(arr))