import re

# the number of test cases
T = int(input())
#input the number of strings
for _ in range(T):
    pattern = "^[-+]?[0-9]*\.[0-9]+$"
    print(bool(re.search(pattern,input())))

