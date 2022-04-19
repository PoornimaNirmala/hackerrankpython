text = input()

#reverse the entered string and check if it matches
if text == text[::-1]:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
    