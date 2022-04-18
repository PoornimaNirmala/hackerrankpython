import numpy

def arrays(arr):
    numpy_array = numpy.array(arr,float)
    reverse_array = numpy_array[::-1]
    return reverse_array    

arr = input().strip().split(' ')
result = arrays(arr)
print(result)