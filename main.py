"""
Лабораторная 2 Вариант 9
Написать функцию, которая принимает челочисленный список, содержащий n элементов, и целое число, и выводит на экран
сгенерированные списки, содержащие n элементов с шагом итерации, равном элементу входящего списка.
"""

input_list = [2,3,5]
step = 2

def generate_lists(input_list, step):
    for num in input_list:
        generated_list = list(range(0, num*step, step))
        print(generated_list)

generate_lists(input_list, step)