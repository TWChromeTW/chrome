print('Задание 1 \n!---------!')

f = open('Perepis.txt')

l = [elem for elem in f]

colvo = 0

for i in l:
    l2 = i.split()

    if int(l2[3][6:]) < 1978:
        print(l2[0], l2[1], l2[2])
        colvo += 1

print()

print(colvo)

print()
print('!------!')

print('Задание 2\n!---------!')

a = int(input('Введите с какого года:\n'))
b = int(input('Введите до какого года:\n'))

print()

for i in l:
    l2 = i.split()

    if (a <= int(l2[3][6:]) <= b):
        print(l2)