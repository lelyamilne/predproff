import csv
with open('songs.csv', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=';', quotechar='"')
    mas = list(reader)[1:]


mas1 = []
for i in mas:
    u = i[3]
    u = u[6:]
    u = int(u)
    if u < 2002:
        mas1.append(i)
    if i[3] in '01.01.2002.':
        mas1.append(i)

for i in mas1:
    print(f'<{i[2]}>-<{i[1]}>-<{i[0]}>')