n = int (input("Введи натуральное число: ")) # вводится n от пользователя
factorial = 1 # инициализируем факториал как 1

for i in range(1, n + 1): # цикл по числам от 1 до n
  factorial *= i # умножаем текущий факториал на i

print(f"Факториал числа {n}: {factorial}") # результат
