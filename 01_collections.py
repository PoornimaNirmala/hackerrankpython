from collections import namedtuple

#enter total number of students
N = int(input())
sum_marks = 0
#enter names of the columns in any order
header = ','.join(input().split())
Student = namedtuple('Student',header)
#enter the data for the list
for _ in range(N):
    student_details = input().split()
    student = Student(*student_details)
    sum_marks += int(student.MARKS)
#print the average marks corrected by two decimals
print("{0:.2f}".format(sum_marks/N))
