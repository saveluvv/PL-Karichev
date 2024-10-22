# cоздал массив из 10 чисел
numbers = [1, 2, 3, 3, 2, 1, 5, 6, 5, 7]
# создал пустой массив для хранения уникальных чисел
unique_numbers = []
# проходим по исходному массиву
for number in numbers:
# проверяем,  есть ли число в массиве `unique_numbers`
    if number not in unique_numbers:
        # если нет, то добавляем его
        unique_numbers.append(number)
# выводим новый массив с уникальными числами
print(unique_numbers)