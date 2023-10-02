#                    Задание 4
# Напишите программу, демонстрирующую работу try\except\finally

print("Задание 4\n")
while True:
    try:
        a = float(input("Введите делимое: "))
        b = float(input("Введите делитель: "))
        c = a / b
        print("Частное: %.2f" % c)
    except ValueError:
        print("Нельзя вводить строки")
    except ZeroDivisionError:
        print("Нельзя делить на ноль")
    else:
        print("Конец")
        break
    finally:
        print("-------")
