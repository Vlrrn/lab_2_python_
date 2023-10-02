#                    Задание 2
# Напишите функцию, которая будет принимать один аргумент.
#   -Строка – вывести на экран самое длинное слово.
#   -Число – сумму цифр.
#   -Если в функцию передаётся множество, то найти сумму всех элементов.
#   -Если список, то найти произведение между первым и вторым отрицательными элементами.
#       Максимальный и минимальный элемент поменять местами.
# Сделать проверку со всеми этими случаями
def color_text(text):
    print("\033[1m\033[36m{}\033[0m".format(text))


def check_k(s):
    while True:
        try:
            k_e = int(input(s))
            if k_e <= 0:
                print("\033[1m\033[31m{}\033[0m".format("\nКоличество должно быть положительным!"))
                continue
            return k_e
        except ValueError:
            print("\033[1m\033[31m{}\033[0m".format("\nВведите целое положительное число!"))


def check_int(s):
    while True:
        try:
            c = int(input(s))
            return c
        except ValueError:
            print("\033[1m\033[31m{}\033[0m".format("\nВведите целое число!"))


def function(arg):
    print()
    if type(arg) == str:
        arg = arg.split()
        if len(arg) > 0:
            a = max(arg, key=len)
            print("Самое длинное слово: ", a)
            print("Его длина =", len(a))
        else:
            print("Не найдено слов.")
    elif type(arg) == int:
        summa = 0
        str_i = str(arg)
        print("Число: ", str_i)
        str_i = str_i.replace('-', '')
        # print(str_i)
        for i in str_i:
            if '0' <= i <= "9":
                summa += int(i)
        print("Сумма цифр числа = ", summa)
    elif type(arg) == set:
        print("Множество: ", arg)
        summ = 0
        for i_set in arg:
            summ += i_set
        print("Сумма элементов =", summ)
    elif type(arg) == list:
        first_min = second_min = -1
        for i in range(0, len(arg)):
            if arg[i] < 0:
                if first_min == -1:
                    first_min = i
                elif second_min == -1:
                    second_min = i
        if second_min >= 0 and first_min >= 0 and first_min != second_min - 1:
            s = 1
            for i in range(first_min + 1, second_min):
                s *= arg[i]
            print(s)
        elif first_min == second_min - 1:
            print("Отрицательные элементы находятся рядом.")
        else:
            print("Нет двух отрицательных элементов.")
        min_el = max_el = arg[0]
        min_el_i = max_el_i = arg.index(min_el)
        for i in arg:
            if i < min_el:
                min_el = i
                min_el_i = arg.index(min_el)
            if i > max_el:
                max_el = i
                max_el_i = arg.index(max_el)
        arg[min_el_i] = max_el
        arg[max_el_i] = min_el
        print("\nMax и Min поменялись местами.\nНовый список:", arg)


while True:
    print()
    print("\033[3m\033[36m{}\033[0m".format("""
     Что вы хотите ввести?
    ***********************
         1. Строку
         2. Число
         3. Множество
         4. Список
         0 - ВЫХОД
    ***********************"""))
    while True:
        v = check_int("- ")
        if v < 0 or v > 4:
            print("\nТакого пункта нет. Повторите ввод:")
        else:
            break
    print()
    if v == 1:
        color_text("""
=======================================
        ВЫ ВЫБРАЛИ ВВОД СТРОКИ
=======================================""")
        st = input("""
Введите строку, состоящую из слов 
(другие символы будут удалены)
- """)
        import re
        new_st = re.sub("[^A-Za-z ]", "", st)
        print("\nСтрока преобразована:\n" +
              "-", new_st)
        function(new_st)
    elif v == 2:
        print()
        color_text("""
=======================================
        ВЫ ВЫБРАЛИ ВВОД ЧИСЛА
=======================================""")
        f = check_int("""
Введите число.
(может быть <0)
- """)
        function(f)
    elif v == 3 or v == 4:
        if v == 3:
            color_text("""
=======================================
      ВЫ ВЫБРАЛИ ВВОД МНОЖЕСТВА
=======================================""")
        else:
            color_text("""
=======================================
        ВЫ ВЫБРАЛИ ВВОД СПИСКА
=======================================""")
        k = check_k("\nКоличество элементов = ")
        print()
        if v == 3:
            mn = set()
            i = 1
            while k > len(mn):
                mn.add(check_int("Введите %.f элемент: " % i))
                i += 1
            function(mn)
        else:
            l = []
            i = 1
            while k > len(l):
                l.append(check_int("Введите %.f элемент: " % i))
                i += 1
            function(l)
    elif v == 0:
        print("\033[33m{}\033[0m".format("""
                ／＞　    フ
        　　　　　| 　_　 _|
        　 　　　／`ミ _x 彡
        　　 　 /　　　 　 |
        　　　 /　 ヽ　　 ﾉ
        　／￣|　　 |　|　|
        　| (￣ヽ＿_ヽ_)_)
        　＼二つ
**********************************"""))
        exit()
