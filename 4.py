# Программа принимает действительное положительное число x и целое отрицательное число y.
# Необходимо выполнить возведение числа x в степень y.
# Задание необходимо реализовать в виде функции my_func(x, y).
# При решении задания необходимо обойтись без встроенной функции возведения числа в степень.
# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func_1(x, y):
    return x ** y
print(my_func_1 (int(input('x = ')), int(input('степень х  = '))))

def my_func_2(b1, b2):
    z2 = - b2
    z1 = b1
    z = 2
    while z <= z2:
        z = z + 1
        z1 = z1 * b1
    return 1/z1
print(my_func_2(int(input('x = ')), int(input('степень х  = '))))