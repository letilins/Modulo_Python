import random

def  adivinhacao():
    
    jogador = input("nome do jogador: ")
    print()
    
    
    limite_inferior = int(input("Digite o numero inferior do intervalo: "))
    limite_superior = int(input("Digite o numero superior do intervalo: "))
    
    numero_secreto = random.randint(limite_inferior, limite_superior)  
    max_tentativas = 5
    tentativas = 0

    print("Bem-vindo ao jogo de adivinhação de números, ", jogador , "!")
    print(f"Estou pensando em um número entre {limite_inferior} e {limite_superior}.")

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
        print()

    if palpite == numero_secreto:
        print(f"Fim de jogo! O número secreto era {numero_secreto}")
        print()
        
jogo_novamente = input("Quer jogar novamente? (s = Sim ou n = Não): ")
print()

if jogo_novamente.lower() == "s":
    adivinhacao()
else:
    print("Fim de Jogo.... Obrigado por jogar!", "\n")
    
adivinhacao()