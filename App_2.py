# 2. Напишите программу, которая найдет произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

def FindMultOfPairs(list):
    new_list = []
    for i in range(int(len(list)/2 + 0.5)):
        new_list.append(int(list[i]) * int(list[-i-1]))
    print(new_list)

list = input('Задайте список: ').split()
FindMultOfPairs(list)