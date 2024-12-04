def find_second_max():
    max1 = float('-inf')
    max2 = float('-inf')

    while True:
        num = int(input("Введите число: "))
        if num == 0:
            break
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num

    if max2 == float('-inf'):
        return "Нет второго по величине элемента"
    else:
        return max2

result = find_second_max()
print(result)