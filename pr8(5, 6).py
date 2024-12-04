def sort_rows(matrix):
    for row in matrix:
        row.sort()
    return matrix

def replace_min_elements(matrix):
    for row in matrix:
        min_elem = min(row)
        min_index = row.index(min_elem)
        if min_elem % 2 == 0:
            row[min_index] = 0
        else:
            row[min_index] = 1
    return matrix

n = 3
m = 4
matrix = [
    [4, 2, 9, 1],
    [5, 6, 3, 8],
    [10, 1, 7, 3]
]

# Задание 1
sorted_matrix = sort_rows(matrix)
print("Отсортированная матрица:")
for row in sorted_matrix:
    print(row)

# Задание 2
modified_matrix = replace_min_elements(matrix)
print("Измененная матрица:")
for row in modified_matrix:
    print(row)