# 8.	Есть словарь песен группы
# Depeche Mode violator songsdict \= { 'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68, }
# Выведите общее время звучания всех песен.
# Создайте список песен, время звучаниях которых больше 5 минут Создайте новый словарь тех песен, в название которых состоит из одного слова

violator_songsdict = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43, 'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07, 'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88, 'Blue Dress': 4.18, 'Clean': 5.68}
a = 0
spisok = []
for i in violator_songsdict:
    a += violator_songsdict[i]
print('Суммарное время звучания:', a)
for i in violator_songsdict:
    if violator_songsdict[i] > 5.0:

print(spisok)


