cube = lambda x: pow(x,3)

def fibonacci(n):
    # return a list of fibonacci numbers
    fibonacci = [0,1]
    for i in range(2,n):
        fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    return fibonacci


n = int(input())
print(list(map(cube, fibonacci(n))))