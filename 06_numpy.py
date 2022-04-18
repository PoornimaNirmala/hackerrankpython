import numpy

numpy.set_printoptions(legacy='1.13')
#input the array size N rows and M columns
N, M = map(int,input().split())
#print the 2D array with 1's as diagonal and 0's everywhere
print(numpy.eye(N, M))

