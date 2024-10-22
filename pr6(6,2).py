# пользователь заполняет массив из 10 чисел
numbers = []
for i in range(10):
  number = int(input(f"Введите {i + 1}-е число: "))
  numbers.append(number)
# считаем сумму чисел, но чтобы было больше 5
sum = 0
for number in numbers:
  if number > 5:
    sum += number
# вывод результата
print(f"Сумма чисел, больше 5: {sum}")