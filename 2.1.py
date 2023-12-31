#                        Задание 1.
# Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
# (каждый год размер его вклада увеличивается на 10%.
# Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты)
# Написать функцию bank, принимающая аргументы a и years, и
# возвращающую сумму, которая будет на счету пользователя
def check(s):
    while True:
        try:
            c = int(input(s))
            if c <= 0:
                print("Неверный ввод!")
                continue
        except ValueError:
            print("Введите целое число!")
        else:
            return c


def bank(a, years):
    for i in range(0, years):
        a *= 1.1
        # print(i + 1, "год - %.3f" % a)
    return a


print("Задание 1\n")
a = check("Вклад = ")
print()
years = check("Срок = ")
print("\nСчёт = %.2f" % bank(a, years))
