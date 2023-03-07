import Jogo

def jogar():
    print("Bem-Vindo ao jogo da Forca")



    print("Deseja jogar novamente ou mudar de jogo?")
    jogar_novamente = int(input("(1) Jogar nomavamente (2)Mudar de jogo: "))
            
    if(jogar_novamente == 1):
        jogar()
                
    elif (jogar_novamente == 2):
        Jogo.escolha_jogos()

if(__name__ == "__main__"):
    jogar()