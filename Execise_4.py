# Задача 4
# Напишите программу, которая по заданному номеру четверти показывает диапазон возможных
# координат точек в этой четверти (x и y).

numberA = int(input('Введите номер четверти: '))
if numberA == 1:
    print('Диапазон возможных координат точек в этой четверти: x = (0, +inf), y = (0, +inf)')
elif numberA == 2:
    print('Диапазон возможных координат точек в этой четверти: x = (0, -inf), y = (0, +inf)')
elif numberA == 3:
    print('Диапазон возможных координат точек в этой четверти: x = (0, -inf), y = (0, -inf)')
elif numberA == 4:
    print('Диапазон возможных координат точек в этой четверти: x = (0, inf), y = (0, -inf)')