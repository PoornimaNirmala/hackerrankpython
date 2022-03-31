import re
#number of test cases
T = int(input())
# input T test cases to check if it is a valid regex or not
output = []
for _ in range(T):    
    try:
        re.compile(input())
        output.append(True)
    except re.error:
        output.append(False) 
for item in output:
    print(item)