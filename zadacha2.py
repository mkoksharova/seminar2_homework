# Задача 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*

# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def usernumbers(usertext):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{usertext}"))
            is_OK = True
        except ValueError:
            print("Число должно быть целое! ")
    return number


def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n - 1)


num = usernumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(fact(e))

print(f"Произведения чисел от 1 до {num}:  {list}")