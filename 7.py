print('even numbers are:')
i=1
while i<=100:
    if i%2 == 0:
        print(i)
    i=i+1

print('odd numbers are:')
i=1
while i<=100:
    if i%2 != 0:
        print(i)
    i=i+1



print('prime numbers are:')
for a in range (1, 101):
    i = 0
    for i in range(2, (a//2 + 1)):
        if(a % i == 0):
            i = i + 1
            break

    if (i == 0 and i != 1):
        print(" %d" %i, end = '  ')




for Number in range (1, 101):
    count = 0
    for i in range(2, (Number//2 + 1)):
        if(Number % i == 0):
            count = count + 1
            break

    if (count == 0 and Number != 1):
        print(" %d" %Number, end = '  ')
