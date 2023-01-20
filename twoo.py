f = open('travels.txt')

l = [elem for elem in f]

summ1 = 0
summ2 = 0
summ3 = 0
summLipki = 0
summRastDen1 = 0

for i in l:
    st = i.split()

    if int(st[0]) == 1:
        summ1 += int(st[6])
    elif int(st[0]) == 2:
        summ2 += int(st[6])
    elif int(st[0]) == 3:
        summ3 += int(st[6])

if max(summ1, summ2, summ3) == summ1:
    print(f"В первый день было перевезенно больше, чем в остальные два - {summ1}")
elif max(summ1, summ2, summ3) == summ2:
    print(f"Во второй день было перевезенно больше, чем в остальные два - {summ2}")
elif max(summ1, summ2, summ3) == summ3:
    print(f"В третий день было перевезенно больше, чем в остальные два - {summ3}")

for i in l:
    st = i.split()

    if st[2] == 'Липки':
        summLipki += int(st[6])

print(summLipki)

for i in l:
    st = i.split()

    if int(st[0]) == 1:
        summRastDen1 += int(st[4])

print(summRastDen1)