# 6. В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться,
# больше или меньше введенное пользователем число, чем то, что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.
# https://drive.google.com/file/d/15FPVBNFRXg_L7e0yv5YixfWFyEiCyPCQ/view?usp=sharing
import random


def program(random_generated):
    guess = int(input("Угадай число "))
    if 100 >= guess > 0:
        if guess == random_generated:
            return f"Угадали {random_generated}"
        if guess < random_generated:
            print("число больше")
        else:
            print("число меньше")
    return


number = random.randint(0, 100)
count = 10
while count > 0:
    program(number)
    count -= 1
print(f"{number=}")

