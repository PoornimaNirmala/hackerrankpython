import re

N = int(input())
for i in range(N):
    phone = re.search(r"^[789][0-9]{9}$",input())
    if phone:
        print("YES")
    else:
        print("NO")
