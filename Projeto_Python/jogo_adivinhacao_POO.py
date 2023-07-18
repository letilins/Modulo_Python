import random

class Adivinhacao:
    def __init__(self, nome, lim_inferior, lim_superior, max_tentativas):
        self.jogador = nome
        self.limite_inferior = lim_inferior
        self.limite_superior = lim_superior
        self.max_tentativas = max_tentativas

    def Jogo(self):
        self.tentativas = 0
        self.numero_secreto = random.randint(self.limite_inferior, self.limite_superior)
        
        while self.tentativas < self.max_tentativas:
            palpite = int(input("Digite o seu palpite: "))
            self.tentativas += 1

            if palpite < self.numero_secreto:
                print("Tente um número maior!")
            elif palpite > self.numero_secreto:
                print("Tente um número menor!")
            else:
                print(f"Parabéns, {self.jogador}! Você acertou o número em {self.tentativas} tentativas!")
                break
        else:
            print(f"Fim de jogo! O número secreto era {self.numero_secreto}")
        
        print()

        self.jogo_novamente()

    def jogo_novamente(self):
        while True:
            jogo_novamente = input("\nQuer jogar novamente? (s = Sim ou n = Não): ")
            print()
            if jogo_novamente.lower() == "s":
                self.Jogo()
            else:
                print("\nFim de Jogo.... Obrigado por jogar!")
                break
            

    def iniciarjogo(self):
        print("Bem-vindo ao jogo de adivinhação de números, ", self.jogador, "!")
        print(f"Estou pensando em um número entre {self.limite_inferior} e {self.limite_superior}. "
              f"E você tem no máximo {self.max_tentativas} tentativas.")
        self.Jogo()
        


nome_jogador = input("Digite o seu nome: ")
limite_inferior = int(input("Digite o número inferior do intervalo: "))
limite_superior = int(input("Digite o número superior do intervalo: "))
max_tentativas = int(input("Digite o número máximo de tentativas: "))


jogo = Adivinhacao(nome_jogador, limite_inferior, limite_superior, max_tentativas)
jogo.iniciarjogo()