# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой

def private_def ():
    list_1 = list(input('Введите через пробел имя, фамилию, год рождения, город проживания, почту, телефон: ').split())
    first_name = list_1[0]
    second_name = list_1[1]
    birth = list_1[2]
    town = list_1[3]
    mail = list_1[4]
    number = list_1[5]
    return  first_name, second_name, birth, town, mail, number

first_name_val, second_name_val, birth_val, town_val, mail_val, number_val = private_def()
print(first_name_val, second_name_val, birth_val, town_val, mail_val, number_val)