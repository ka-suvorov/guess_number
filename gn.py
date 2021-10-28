# -*- coding: utf-8 -*-

# Угадай число

# Модуль случайных чисел
import random  

# Инициализация переменных
lowDigit = 10
highDigit = 50
digit = 0
countInput = 0
win = False
playGame = True
x = 0
startScore = 100
score = 0
maxScore = 0

# Главный цикл

while (playGame):
    digit = random.randint(lowDigit, highDigit)
    print("_" * 30)
    countInput = 0
    score = startScore
    print("Компьютер загадал число, попробуйте отгадать")
    print("_" * 30)
    
# Цикл слежения за результатом игры
    while (not win and score >0):
        print("_" * 30)
        print(f"Заработано очков: {score}")
        print(f"Рекорд: {maxScore}")
        x = ""
        
# Ввод числа
        while (not x.isdigit()):
            x = input("Введите число от {lowDigit} до {highDigit}: ")
            if (not x.isdigit()):
                print("." * 27 + "Введите число: ")

# Преобразование строки в целое число
        x = int(x)

# Подсказки
        if (x == digit):
            win = True
        else:
            length = abs(x - digit)
            if (length < 3):
                print("Очень горячо")
            elif (length < 5):
                print("Горячо")
            elif (length < 10):
                print("Тепло")
            elif (length < 15):
                print("Прохладно")
            elif (length < 20):
                print("Холодно")
            else:
                print("Ледяной ветер")

            if (countInput == 7):
                score -= 10
                if (digit % 2 == 0):
                    print("Число четное")
                else:
                    print("Число не четное")
            elif (countInput == 6):
                score -= 8
                if (digit % 3 == 0):
                    print("Число делится на три")
                else:
                    print("Число не делится на три")
            elif (countInput == 5):
                score -= 4
                if (digit % 4 == 0):
                    print("Число делится на четыре")
                else:
                    print("Число не делится на четыре")
            elif (countInput > 2 and countInput < 5):
                score -= 2
                if (x > digit):
                    print("Загаданное число МЕНЬШЕ Вашего")
                else:
                    print("Загаданное число БОЛЬШЕ Вашего")
            score -= 5
        countInput += 1 # Счетчик попыток

# Текстовое меню
    print("*" * 40)
    if (x == digit):
        print("Победа! Поздравляю!")
    else:
        print("Ой, у вас кончились очки. Вы проиграли!")

    if (input("Enter = Сыграть еще, 0 - выход ") == "0"):
        playGame = False
    else:
        win = False

    if (score > maxScore):
        maxScore = score


# Текст после игры

print("*" * 40)
print("""Спасибо, что сыграли в мою игру!
Возвращайтесь скорей! Буду ждать!
P.S. Вы хорошо держались!""")
