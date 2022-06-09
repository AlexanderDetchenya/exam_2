# 5.	Создайте словарь из строки ' An apple a day keeps the doctor away'
# следующим образом: в качестве ключей возьмите символы
# строки,
# а значениями пусть будут числа, соответствующие количеству вхождений данной буквы в строку.

stroka = 'An apple a day keeps the doctor away'
simvoli = stroka.split(' ')
print(simvoli)
simv2 = []
for slova in simvoli:
    for j in slova:
        simv2.append(j)
print(simv2)
simv3 = set(simv2)
print('dlina', len(simv3))
simv4 = list(simv3)
print(simv4)
vx = []
a = 0
for i in simv3:
    a = simv2.count(i)
    vx.append(a)
print(vx)
slovar = dict(zip(simv3, vx))
print(slovar)