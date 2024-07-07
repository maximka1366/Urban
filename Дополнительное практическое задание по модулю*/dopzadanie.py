from decimal import Decimal
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(students)
dict_students = {}
for i in range( 0, len(students_sort)) :
    dict_students[students_sort[i]] = sum(grades[i]) / len(grades[i])
print(dict_students)








