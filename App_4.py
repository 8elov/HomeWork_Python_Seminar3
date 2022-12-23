# 4. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

def FindBinaryNumber(num):
    line = ''
    while num > 0:
        line += str(num % 2)
        num //= 2
    reversedline = ''.join(reversed(line))
    print(reversedline)

num = int(input('Введите десятичное число: '))
FindBinaryNumber(num)