#                    Задание 2
# Напишите функцию, которая будет принимать один аргумент.
#   -Строка – вывести на экран самое длинное слово.
#   -Число – сумму цифр.
#   -Если в функцию передаётся множество, то найти сумму всех элементов.
#   -Если список, то найти произведение между первым и вторым отрицательными элементами.
#       Максимальный и минимальный элемент поменять местами.
# Сделать проверку со всеми этими случаями

def check_e(s):
    while True:
        try:
            el = int(input(s))
            return el
        except ValueError:
            print("Введите целое число!")


def check_k(s):
    while True:
        try:
            k_e = int(input(s))
            if k_e <= 0:
                print("!?")
                continue
            return k_e
        except ValueError:
            print("Введите целое число!")


def check_i(s):
    while True:
        try:
            c = int(input(s))
            return c
        except ValueError:
            print("Введите целое число!")


def check_f(s):
    while True:
        try:
            c = float(input(s))
            return c
        except ValueError:
            print("Введите число!")


def function(arg):
    print()
    if type(arg) == str:
        print("str")
        arg = arg.split()
        a = max(arg, key=len)
        print(a)
        print(len(a))
    elif type(arg) == float:
        summa = 0
        str_f = str(arg)
        str_f = str_f.replace('-', '')
        str_f = str_f.replace('.', '')
        print(str_f)
        for i_f in str_f:
            summa += int(i_f)
        print(summa)
    elif type(arg) == set:
        print("set")
        summ = 0
        for i_set in arg:
            summ += i_set
        print(summ)
    elif type(arg) == list:
        print("list")
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
            print("0 elements")
        else:
            print("Nothing to do")
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
        print(arg)


while True:
    print()
    print("Что вы хотите ввести?\n" +
          "***********************\n" +
          "     1. Строку\n" +
          "     2. Число\n" +
          "     3. Множество\n" +
          "     4. Список\n" +
          "     0 - ВЫХОД\n" +
          "***********************")
    while True:
        v = check_i("- ")
        if v < 0 or v > 4:
            print("Такого пункта нет. Повторите ввод")
        else:
            break
    print()
    if v == 1:
        st = input("str ")
        import re
        new_st = re.sub("[^A-Za-z ]", "", st)
        print(new_st)
        function(new_st)
    elif v == 2:
        print()
        f = check_f("float ")
        function(f)
    elif v == 3 or v == 4:
        k = check_k("Количество элементов = ")
        if v == 3:
            mn = set()
            i = 1
            while k > len(mn):
                mn.add(check_e("Введите %.f элемент: " % i))
                i += 1
            function(mn)
        else:
            l = []
            i = 1
            while k > len(l):
                l.append(check_e("Введите %.f элемент: " % i))
                i += 1
            function(l)
    elif v == 0:
        print("""
                ／＞　    フ
        　　　　　| 　_　 _|
        　 　　　／`ミ _x 彡
        　　 　 /　　　 　 |
        　　　 /　 ヽ　　 ﾉ
        　／￣|　　 |　|　|
        　| (￣ヽ＿_ヽ_)_)
        　＼二つ
        """)
        exit()
