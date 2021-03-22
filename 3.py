# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def maximum (a, b, c):
    return max(a + b, a + c, b + c)
m = maximum (int(input('а = ')), int(input('b = ')), int(input('c = ')))

print(m)