import random as rd

print("------------")
print("Bem-Vindo ao jogo de adivinhação!")
print("------------")

n_secreto = rd.randranger
n_tentativas = 3
rodada = 1

for rodada in range(1,n_tentativas + 1):
    print(f"Tentativa {rodada} de {n_tentativas}")
    entrada = int(input("Digite um número de 1 a 100: "))
    acerto = entrada == n_secreto
    entrada_maior = entrada == n_secreto
    entrada_menor = entrada < n_secreto

    if(entrada > 100 or entrada < 1):
        print("O valor digitado não é permitido")
        continue

    print(f"Você digitou o número: {entrada}")

    if(acerto):
        print(f"Você acertou o número secreto. Parabéns!!!")
        break
    else:
        if(entrada_maior):
            print("O número digitado foi maior do que o número secreto")
        if(entrada_menor):
            print("O número digitado foi menor do que o número secreto")

    rodada = rodada + 1

print("FIm do Jogo!")