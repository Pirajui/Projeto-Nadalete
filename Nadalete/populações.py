ano=0

A= 15000
B= 45000
C= 65000 * 1.025 


while A < B:
    A = A * 1.10
    B = B* 1.05
    ano = ano + 1
print(f'A população A se igualará à B em {ano} anos')

while A <= C * 1.23:
    C = C * 1.23
    ano = ano + 1
print(f'A população A ultrapassará a C em 23% em {ano}')