stroka = input('Введите строку, чтобы слова разграничивались пробелом: ')
slova = stroka.split(' ')
dlina = []
for i in slova:
    k = len(i)
    dlina.append(k)
print(dlina)

slovar = dict(zip(slova, dlina))
print(slovar)
for i in dlina:
    if i == max(dlina):
        for key in slovar:
            if slovar[key] == i:
                print('Самое длинное слово: ', key)
        break