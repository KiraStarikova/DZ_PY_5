# Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
import os

print("Введите абсолютный путь до файла ")
s = str(input())
a, b = os.path.split(s)
b, c = b.split('.')
result = (a, b, c)
print(result)
