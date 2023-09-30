#                    Задание 2
# Напишите функцию, которая будет принимать один аргумент.
#   -Строка – вывести на экран самое длинное слово.
#   -Число – сумму цифр.
#   -Если в функцию передаётся множество, то найти сумму всех элементов.
#   -Если список, то найти произведение между первым и вторым отрицательными элементами.
#       Максимальный и минимальный элемент поменять местами.
# Сделать проверку со всеми этими случаями

# ------------------------------------
#            :/ список
# ------------------------------------
def check(s):
    while True:
        try:
            ii = int(input(s))
        except ValueError:
            print("Введите целое число!")
        else:
            return ii


def check_k(s):
    while True:
        try:
            k_e = int(input(s))
            if k_e <= 0:
                print("!?")
                continue
        except ValueError:
            print("Введите целое число!")
        else:
            return k_e


def check_i(s):
    while True:
        try:
            c = int(input(s))
        except ValueError:
            print("Введите целое число!")
        else:
            return c


def check_f(s):
    while True:
        try:
            c = float(input(s))
        except ValueError:
            print("Введите число!")
        else:
            return c


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
        for i in str_f:
            summa += int(i)
        print(summa)
    elif type(arg) == set:
        print("set")
        summ = 0
        for i in arg:
            summ += i
        print(summ)
    elif type(arg) == list:
        print("list")
        first_min = -1
        second_min = -1
        for i in range(0, len(arg)):
            if arg[i] < 0:
                if first_min == -1:
                    first_min = i
                else:
                    if second_min == -1:
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
# a = input("In ")
# print(a, " ", type(a))
while True:
    # a = "str"
    # function(a)
    # a = 2.3
    # function(a)
    # a = {1, 2}
    # function(a)
    # a = [1, 4, -5]
    # function(a)
    # break
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
        function(st)
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
                mn.add(check("Введите %.f элемент: " % i))
                i += 1
            function(mn)
        else:
            l = []
            i = 1
            while k > len(l):
                l.append(check("Введите %.f элемент: " % i))
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
