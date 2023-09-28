#                    Задание 3
# Найти сумму каждого столбца матрицы размером m*n.
from random import randint


def check(s):
    while True:
        try:
            mn = int(input(s))
            if mn <= 0:
                print("!?")
                continue
        except ValueError:
            print("Введите целое число!")
        else:
            return mn


def n_sum(mtrx):
    for j in range(n):
        summ = 0
        for i in range(m):
            summ += mtrx[i][j]
        print("Сумма", j + 1, "столбца - ", summ)
    print()


print("Задание 2\n")
m = check("Количество строк = ")
n = check("Количество столбцов = ")
print("\nМатрица:")
matrix = []
for i in range(m):
    matrix.append([])
    for j in range(n):
        matrix[i].append(randint(0, 10))
        print(matrix[i][j], end='\t')
    print()
print()
n_sum(matrix)