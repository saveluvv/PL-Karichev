# подпрограмма для нахождения наибольшего общего делителя методом Евклида
def gcd(x, y):
  while y != 0:
    x, y = y, x % y # обновляем значения x и y
  return x # возвращаем НОД
# вводим значения A, B, C, D от пользователя
A = int(input("Введите A (числитель первой дроби): "))
B = int(input("Введите B (знаменатель первой дроби): "))
C = int(input("Введите C (числитель второй дроби): "))
D = int(input("Введите D (знаменатель второй дроби): "))
# находим равные знаменатели для вычитания дробей
common_denominator = B * D # общий знаменатель
new_numerator = (A * D) - (C * B) # новый числитель
# применяем алгоритм Евклида для сокращения дроби
common_divisor = gcd(abs(new_numerator), common_denominator) # НОД
# сокращаем дробь
final_numerator = new_numerator // common_divisor
final_denominator = common_denominator // common_divisor
# результат
print(f"Результат вычитания: {final_numerator}/{final_denominator}")