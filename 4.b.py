count_max=0
count=0
sum_max=0
sum=0


for i in range (0,150):
    if (i == 0):
        atual = int(input('digite o número '))
    else:
        anterior = atual
        atual = int(input('digite o número '))
        if atual == anterior: 
            count = count + 1
            if (count == 1):
                sum = anterior
            sum = sum + atual
        else:
            if count >= count_max:
                if sum > sum_max:
                        sum_max = sum
                count_max = count
                count = 0
            sum = 0
print(f'Existem {count_max + 1} elementos repetidos, somando {sum_max}')
