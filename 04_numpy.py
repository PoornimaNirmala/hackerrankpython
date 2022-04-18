import numpy

#input the one dimensional array
array_1D = numpy.array(list(map(int,input().split())))
#reshape the one dimensional array to 3x3
print(numpy.reshape(array_1D,(3,3)))
