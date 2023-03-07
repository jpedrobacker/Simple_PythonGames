import Jogo
import random

def jogar():
    print("Bem-Vindo ao jogo da adivinhação!")
    print("Selecione a dificuldade!")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina a dificuldade:"))

    print("Você selecionou a dificuldade {}".format(nivel))

    total_de_tentativas = 0

    if  (nivel == 1):
        total_de_tentativas = 10
        
    elif(nivel == 2):
        total_de_tentativas = 5
        
    elif(nivel == 3):
        total_de_tentativas = 3

    numero_secreto = random.randrange(1 , 100+1)

    for rodada in range (1,total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada , total_de_tentativas))
        chute = int(input("Digite o seu numero entre 1 e 100: "))
        
        if( chute < 1 or chute > 100):
            print("Você deve digitar um numero entre 1 e 100!")
            continue
            
        print("Você escolheu:",chute)
        
        acertou = chute == numero_secreto
        maior   = chute >  numero_secreto
        menor   = chute <  numero_secreto
        errou   = chute != numero_secreto

        if(chute == numero_secreto):
            print("Parabéns você acertou o numero secreto")
            break
        else:
            if(maior):
                print("O seu chute foi maior do que o número secreto!")
            
            elif(menor):
                print("O seu chute foi menor do que o número secreto!")
        
        if(rodada == total_de_tentativas):
            print("Seu número de tentativas acabaram, você perdeu, o numero secreto era: {}".format(numero_secreto))
            print("Deseja jogar novamente ou mudar de jogo?")
            
            jogar_novamente = int(input("(1) Jogar nomavamente (2)Mudar de jogo: "))
            
            if(jogar_novamente == 1):
                jogar()
                
            elif (jogar_novamente == 2):
                Jogo.escolha_jogos()

if(__name__ == "__main__"):
    jogar()