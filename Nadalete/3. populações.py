A = 15000 
A2 = 15000 #população A na segunda parte do exercício
B = 45000 
C = 65000 

anos1 = 0 
anos2 = 0 

while A < B: 
    A = A * 1.10 
    B = B * 1.05 
    anos1 = anos1 + 1 
print(f'A população de A alcançará B em {anos1} anos.')

while ((A2-C)/C ) <= 0.23: 
    A2 = A2 * 1.10 
    C = C * 1.025 
    anos2 = anos2 + 1 
print(f'A população A ultrapassará C em 23% em {anos2} anos')
