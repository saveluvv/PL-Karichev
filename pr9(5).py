def print_digits_reverse(n):
    if n == 0:
        return
    print(n % 10)
    print_digits_reverse(n // 10)

N = 12345
print_digits_reverse(N)