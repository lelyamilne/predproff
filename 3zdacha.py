import csv
with open('songs.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    mas = list(reader)[1:]


n = input()
c = 0
for i in mas:
    if i[1] in n:
        c = 1
        print(f'У {n} найдена песня: {i[2]}')
    if c == 0:
        print('К сожалению, ничего не удалось найти')
while n != '0':
    n = input()
    c = 0
    for i in mas:
        if i[1] in n:
            c = 1
            print(f'У {n} найдена песня: {i[2]}')
    if c == 0:
        print('К сожалению, ничего не удалось найти')

