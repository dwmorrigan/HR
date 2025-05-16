from collections import namedtuple

# Version 1
n = int(input())
Gradebook = namedtuple('Gradebook', 'ID MARKS NAME CLASS')
order = input().strip().split()
for i in range(4):
    if order[i] == "ID":
        id = i
    elif order[i] == "MARKS":
        marks = i
    elif order[i] == "NAME":
        name = i
    elif order[i] == "CLASS":
        class_ = i
list_of_grades = []
for i in range(n):
    line = input().strip().split()
    grade = Gradebook(ID = line[id], MARKS = line[marks], NAME = line[name], CLASS = line[class_])
    list_of_grades.append(grade)
addit = 0
for i in range(len(list_of_grades)):
    mark = int(list_of_grades[i].MARKS)
    addit += mark
avg = addit / len(list_of_grades)
print(f"{avg:.2f}")

# Surely this is the worst way to make it work, but work it does.

# Version 2
n = int(input())
# I had NO idea you could do the names in-place. That's awesome
Gradebook = namedtuple('Gradebook', input().strip().split())
list_of_grades = []
for i in range(n):
    grade = Gradebook(*input().strip().split())
    list_of_grades.append(int(grade.MARKS))
print(f"{sum(list_of_grades)/n:.2f}")