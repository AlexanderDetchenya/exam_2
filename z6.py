# 6.	Ввести 10 чисел, данные числа добавить их во множество.
a = [int(input('Введите число: ')) for i in range(10)]
mn = set(a)
print('Множество представлено: ', mn)

