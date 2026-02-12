print("------------")
print("Bem-Vindo ao jogo de adivinhação!")
print("------------")

n_secreto = 50947
entrada = int(input("Digite um número: "))
acerto = entrada == n_secreto
entrada_maior = entrada == n_secreto
entrada_menor = entrada < n_secreto

print(f"Você digitou o número: {entrada}")

if(acerto):
    print(f"Você acertou o número secreto. Parabéns!!!")
else:
    if(entrada_maior):
        print("O número digitado foi maior do que o número secreto")
    if(entrada_menor):
        print("O número digitado foi menor do que o número secreto")

print("FIm do Jogo!")