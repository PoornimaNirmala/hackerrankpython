import numpy
#input the integers for dimension array
N = tuple(map(int,input().split()))
#print zeroes and ones and convert it into integer, default is float
print(numpy.zeros(N,int))
print(numpy.ones(N,int))