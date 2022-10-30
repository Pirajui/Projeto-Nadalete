h = 1
n = int(input('Valor de N: '))
a = 1
b = 1
if n >=50:
    while b < n:
        a += 2
        b += 1
        c = a/b
        h += c
        h *= -1

    if b%2==0:
        h*=-1
        
    print(h)
else:
    print('n tem que ter um valor maior ou igual a 50')

    
h = 0
n = int(input('Valor de N: '))
a = 0
if n >= 50:
    while a < n:
        a += 1 
        b = a**2
        c = a/b
        h += c
        h *= -1

    if not(b%2==0):
        h*=-1
        
    print(h)
else:
    print('n tem que ser um valor maior ou igual a 50')

n = 3
N = int(input('Valor: '))
P = 2
a = 2
b = 1
b1 = 1

if N >= 50: 
    while n<=N:
        mult=0
        for count in range(3,n):
            if n%count==0:
                mult+=1
        b1 += 2
        b = b1**3
        a = n 
        P += a/b
        n+=2

    print(P)
else:
    print('n tem que ser valor maior ou igual a 50')

