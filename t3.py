# Создайте функцию генератор чисел Фибоначчи (см. Википедию).

def fib(limit: int):
    f_num = [0, 1]
    while limit > 0:
        yield f_num[-1]
        f_num.append(f_num[-1] + f_num[-2])
        limit -= 1


for number in fib(11):
    print(number)
