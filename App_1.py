# 1. Задайте список из нескольких чисел. 
# Напишите программу, которая найдет сумму элементов списка, стоящих на нечетной позиции.

def FindOfOddElements(list):
    count = 0
    for i in range(1, len(list), 2):
        count += int(list[i])
    print(count)

list = input('Задайте список: ').split()
FindOfOddElements(list)
