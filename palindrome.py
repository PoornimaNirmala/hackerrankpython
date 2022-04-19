text = input()

#reverse the string and check if it matches with the entered string
if text == text[::-1]:
    print(f"{text} is a palindrome")
else:
    print(f"{text} is not a palindrome")
    
