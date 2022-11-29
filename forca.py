
def imprime(lista):
    for i in lista:
        print(i,' ',end = '')

txt_file = open("palavras.txt","r")
palavras = txt_file.readlines()

for i in range(len(palavras)):
    palavras[i] = palavras[i].replace("\n", "")

print(palavras)

import random
palavra_sorteada = random.choice(palavras)

acerto = []

for i in palavra_sorteada:
    acerto.append('_')
    

chances = 0

cont_acerto = 0

while True:
    imprime(acerto)
    print("\n",chances)
    if cont_acerto == len(palavra_sorteada):
        print("Você Venceu!!!")
        break
    if chances == 6:
        print("Você Perdeu!!!")
        break
    jogadas = str(input("Informe a Letra que deseja jogar:"))
    if jogadas not in palavra_sorteada:
        chances = chances + 1
    cont=0
    for i in palavra_sorteada:
        if jogadas == i:
            acerto[cont] = jogadas
            cont_acerto += 1
        cont += 1
  
