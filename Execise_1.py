# Задача 1
# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет,
# является ли этот день выходным.
# Пример:
# 6 -> да
# 7 -> да
# 1 -> нет

print('Введите число от 1 до 7: ')
number = int(input())
if number < 1 or number > 7:
    print('Вы ввели некорректное значение')
elif number == 1 or number == 2 or number == 3 or number == 4 or number == 4 or number == 5:
    print(f'{number} -> этот день не является выходным')
elif number == 6 or number == 7:
    print(f'{number} -> этот день является выходным')
