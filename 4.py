# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def func(n: int) -> str:
    num = ''
    while n > 0:
        num += str(int(n % 2))
        n //= 2
    return num
number = int(input('Введите число: '))
print(f'десятичное число {number} -> двоичное число {func(number)}')