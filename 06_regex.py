import re

string = "the sun rises in the east"

#using findall function
#The findall() function returns a list containing all matches.
result = re.findall('s',string)
print(result)

#using split function
#The split() function returns a list where the string has been split at each match
result = re.split('\s',string)
print(result)

#using sub function
#The sub() function replaces the matches with the text of your choice:
result = re.sub('\s','*',string)
print(result)

#using search function
#Check if the string starts with "the" and ends with "east"
result = re.search('^the.*east$',string)
if result:
    print("Yes, Match found!")
else:
    print("No Match found!")

#search function returns Match object which has properties and methods, span(),string,group()
#span() returns the start and end position of first occurence of the match 
result = re.search(r"\bs\w+",string)
print(result.span())
#string property returns the string passed into the function
result = re.search(r"\bs\w+",string)
print(result.string)
#group() returns the string where there was a match
result = re.search(r"\bs\w+",string)
print(result.group())