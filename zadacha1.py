# Задача 1. Напишите программу, которая принимает на вход вещественное или целое число и показывает сумму его цифр. Через строку нельзя решать.
# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

def usernumbers(usertext):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{usertext}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = usernumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")