import numpy

#input two integer arrays A and B of dimensions NxM
N, M = map(int,input().split())
arrayA = numpy.array([input().split() for i in range(N)], int)
arrayB = numpy.array([input().split() for i in range(N)], int)
# add(A+B)
print(arrayA + arrayB)
# subtract(A-B)
print(arrayA - arrayB)
# multiply(A*B)
print(arrayA * arrayB)
# integer division(A//B)
print(arrayA // arrayB)
# mod(A%B)
print(arrayA % arrayB)
# power(A**B)
print(arrayA ** arrayB)