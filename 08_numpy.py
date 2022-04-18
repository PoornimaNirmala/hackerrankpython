import numpy

numpy.set_printoptions(legacy = '1.13')

arrayA = list(map(float,input().split()))
print(numpy.floor(arrayA))
print(numpy.ceil(arrayA))
print(numpy.rint(arrayA))

