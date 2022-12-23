# 3. Задайте список из вещественных чисел. 
# Напишите программу, которая найдет разницу между максимальным и минимальным значением дробной части.

def FindDiffMaxMin(list):
    new_list = []
    for i in list:
        if len(i.split('.')) == 2:
            new_list.append(float(i) % 1)
    print(round((max(new_list) - min(new_list)), 2))

list = input('Задайте список из вещественных чисел: ').split()
FindDiffMaxMin(list)
