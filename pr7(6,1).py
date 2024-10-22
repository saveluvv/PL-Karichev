# функция для нахождения НОД (Наибольшего Общего Делителя) двух натуральных чисел с использованием алгоритма Евклида.
def gcd(a, b):
  while b != 0:
    a, b = b, a % b # обновляем значения a и b
  return a # возвращаем НОД
# функция для нахождения НОК (Наименьшего Общего Кратного) двух натуральных чисел, используя НОД.
def lcm(a, b):
  return (a * b) // gcd(a, b) # формула НОК
# пользователь вводит два числа
a = int(input("Введи первое число: "))
b = int(input("Введи второе число: "))
# находим НОД и НОК
nod = gcd(a, b)
nok = lcm(a, b)
# результат
print(f"НОД({a}, {b}) = {nod}")
print(f"НОК({a}, {b}) = {nok}")