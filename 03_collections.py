from collections import deque
# input the number of operations to be done
n = int(input())
d = deque()
# input the operations in a loop
for _ in range(n):
    operation = input().split()
    if operation[0] == "append":
        d.append(operation[1])
    elif operation[0] == "appendleft":
        d.appendleft(operation[1])
    elif operation[0] == "pop":
        d.pop()
    elif operation[0] == "popleft":
        d.popleft()
result = ''
for item in d:
    result += item + ' '
print(result)