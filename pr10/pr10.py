def read_matrix_from_file(filename):
    with open(filename, 'r') as file:
        matrix = [list(map(int, line.split())) for line in file]
    return matrix

def find_second_max(matrix):
    max1 = float('-inf')
    max2 = float('-inf')

    for row in matrix:
        for num in row:
            if num > max1:
                max2 = max1
                max1 = num
            elif num > max2:
                max2 = num

    if max2 == float('-inf'):
        return "Нет второго по величине элемента"
    else:
        return max2

def write_result_to_file(filename, result):
    with open(filename, 'w') as file:
        file.write(str(result))

input_filename = 'ФИО_группа_vvod.txt'
output_filename = 'ФИО_группа_vivod.txt'

matrix = read_matrix_from_file(input_filename)

result = find_second_max(matrix)

write_result_to_file(output_filename, result)

print(f"Результат записан в файл {output_filename}")