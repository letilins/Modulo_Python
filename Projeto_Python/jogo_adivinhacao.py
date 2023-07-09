import random

def  adivinhacao():
    
    limite_inferior = int(input("Digite o numero inferior do intervalo: "))
    limite_superior = int(input("Digite o numero superior do intervalo: "))
    
    numero_secreto = random.randint(limite_inferior, limite_superior)  
    max_tentativas = 5
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação de números!")
    print("Estou pensando em um número entre Numero inferior e Numero superior.")

    while tentativas < max_tentativas:
        palpite = int(input("Digite o seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Tente um número maior!")
        elif palpite > numero_secreto:
            print("Tente um número menor!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
            break

    if palpite != numero_secreto:
        print(f"Fim de jogo! O número secreto era {numero_secreto}")
        
jogo_novamente = input("Quer jogar novamente? (sim ou não): ")
if jogo_novamente.lower() == "sim":
    adivinhacao()
else:
    print("Fim de Jogo.... Obrigado por jogar!")