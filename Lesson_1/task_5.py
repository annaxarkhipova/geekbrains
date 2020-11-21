# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.
# https://drive.google.com/file/d/1ydDhgRFY0F_4WXiqLSupQQdnR_XbU7Fo/view?usp=sharing

print("Введи любые две буквы")  # строчные буквы от a-z
first_letter = ord(input("Первая "))
second_letter = ord(input("Вторая "))
if first_letter != ord(chr(first_letter).lower()) or second_letter != ord(chr(second_letter).lower()):
    print("error")
else:
    first_letter_place = abs(ord("a") - first_letter) + 1
    second_letter_place = abs(ord("a") - second_letter) + 1
    print(f"{first_letter_place= }, {second_letter_place= }")
    amount_symbols_between_letters = abs(first_letter_place - second_letter_place) - 1
    print(f"{amount_symbols_between_letters= }")
