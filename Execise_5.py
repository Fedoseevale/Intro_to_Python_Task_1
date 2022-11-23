# Задача 5
# Напишите программу, которая принимает на вход координаты двух точек и находит
# расстояние между ними в 2D пространстве (НЕОБЯЗАТЕЛЬНО, ПО ЖЕЛАНИЮ: найти расстояние в 3D пространстве)
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21
import math

print('Введите координаты первой точки')
x1 = int(input('x1: '))
y1 = int(input('y1: '))
z1 = int(input('z1: '))
print('Введите координаты второй точки')
x2 = int(input('x2: '))
y2 = int(input('y2: '))
z2 = int(input('z2: '))

def dist (ax, ay, az, bx, by, bz):
    difX = bx - ax
    difY = by - ay
    difZ = bz - az
    return round((math.sqrt(difX*difX + difY*difY + difZ*difZ)), 2)

distance =  dist (x1, y1, z1, x2, y2, z2)
print(f'Расстояние между точками: {distance}')
