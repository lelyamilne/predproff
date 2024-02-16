import csv
with open('songs.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    mas = list(reader)[1:]

russian_artists = []
foreign_artists = []
for i in mas:
    for n in i[1]:
        if n in 'ЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮйцукенгшщзхъфывапролджэячсмитьбю':
            russian_artists.append(i[1])
        else:
            foreign_artists.append(i[1])
a = len(russian_artists)
b = len(foreign_artists)
print(f'Количество российских исполнителей: {a}')
print(f'Количество зарубежных исполнителей: {b}')



