from random import randint
from time import sleep

lista = list()
jogos = list()

print('='*35)
print('MEGA-SENA')
print('='*35)
quant = int(input('Quantos jogos voce deseja: '))

tot = 1
while tot <= quant:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    tot += 1
print('='*35)
print('Jogos feitos com sucesso:')
print('='*35)

for i,l in enumerate(jogos):
    print(f'JOGO {i+1}: {l}')
    sleep(1)
print('='*35)


