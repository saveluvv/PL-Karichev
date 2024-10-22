# cоздал массив из 10 чисел
numbers = [1, 5, 3, 8, 2, 6, 9, 4, 7, 10]
# находим наибольшее число
max_number = numbers[0]  # предполагаем, что первое число - наибольшее
for number in numbers:
    if number > max_number:
        max_number = number
# считаем кол-во меньших и больших чисел
count_less = 0
count_greater = 0
for number in numbers:
    if number < max_number:
        count_less += 1
    elif number > max_number:
        count_greater += 1
# вывод результатов
print(f"Наибольшее число: {max_number}")
print(f"Кол-во чисел меньше наибольшего: {count_less}")
print(f"Кол-во чисел больше наибольшего: {count_greater}")