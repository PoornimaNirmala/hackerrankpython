import re

result = re.findall(r'(?<=[qwrtypsdfghjklzxcvbnm])([aeiou]{2,})(?=[qwrtypsdfghjklzxcvbnm])', input().strip(),re.IGNORECASE)

if result:
    for string in result:
        print(string)
else:
    print(-1)