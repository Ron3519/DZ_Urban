from statistics import mean
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
result = {}
L = 0
for i in students:
    result[i] = grades[L]
    L += 1
for i in result:
    result[i] = mean(result[i])
print(result)