class jogo():
    def __init__(self):       
        self.tabuleiro = ['-','-','-'
        ,'-','-','-',
        '-','-','-']
    
    def mostrar(self): #print do tabuleiro
        for i in range (0,9):
            print(self.tabuleiro[i],end='')
            if(i == 2 or i == 5 or i == 8):
                print()
        print()

    def MinMax(self,ismax):
        valor = ganhou(self.tabuleiro)
        if(valor != -2):
            return valor
        
        if(ismax):
            melhor = -1000
            for i in range(0,9):
                if(self.tabuleiro[i] == '-'):
                    self.tabuleiro[i] = 'O'
                    melhor = max(melhor,self.MinMax(False))
                    self.tabuleiro[i] = '-'
            return melhor


        else:
            melhor = 1000
            for i in range(0,9):
                if(self.tabuleiro[i] == '-'):
                    self.tabuleiro[i] = 'X'
                    melhor = min(melhor,self.MinMax(True))
                    self.tabuleiro[i] = '-'
            return melhor
            

    def melhor_movimento(self):
        melhor_valor = -1000
        posicao = -1
        for i in range(0,9):
            if(self.tabuleiro[i] == '-'):
                self.tabuleiro[i] = 'O'
                valor = self.MinMax(False)
                self.tabuleiro[i] = '-'
                if(valor > melhor_valor):
                    melhor_valor = valor
                    posicao = i
        return posicao


    def validar_jogada(self,i): #verifica se a entrada fornecida não está vazia ou não está preenchida com O
        if(self.tabuleiro[i] == '-'):
            return True
        return False

    def entrar_jogada(self): #Valida a entrada do jogador
        while(True):
            movimento = int(input("Escolha a posição: [0 até 8]: "))
            if(self.validar_jogada(movimento)):
                self.tabuleiro[movimento] = 'X'
                break

    def jogar(self):
        while(True):
            self.mostrar()
            self.entrar_jogada() #Jogador = X   
            if(ganhou(self.tabuleiro) == -1):
                print("Jogador Ganhou")
                break

            ia = self.melhor_movimento()
            self.tabuleiro[ia] = 'O'

            if(ganhou(self.tabuleiro) == 1):
                print("IA ganhou")
                break
            
            if(ganhou(self.tabuleiro) == 0):
                print("Empate")
                break

def ganhou(tabuleiro):

    if((tabuleiro[0] == 'X' and tabuleiro[1] == 'X' and tabuleiro[2] == 'X') or
    (tabuleiro[3] == 'X' and tabuleiro[4] == 'X' and tabuleiro[5] == 'X') or
    (tabuleiro[6] == 'X' and tabuleiro[7] == 'X' and tabuleiro[8] == 'X') or
    (tabuleiro[0] == 'X' and tabuleiro[3] == 'X' and tabuleiro[6] == 'X') or
    (tabuleiro[1] == 'X' and tabuleiro[4] == 'X' and tabuleiro[7] == 'X') or
    (tabuleiro[2] == 'X' and tabuleiro[5] == 'X' and tabuleiro[8] == 'X') or
    (tabuleiro[0] == 'X' and tabuleiro[4] == 'X' and tabuleiro[8] == 'X') or
    (tabuleiro[2] == 'X' and tabuleiro[4] == 'X' and tabuleiro[6] == 'X')):
        return -1
    
    if((tabuleiro[0] == 'O' and tabuleiro[1] == 'O' and tabuleiro[2] == 'O') or
    (tabuleiro[3] == 'O' and tabuleiro[4] == 'O' and tabuleiro[5] == 'O') or
    (tabuleiro[6] == 'O' and tabuleiro[7] == 'O' and tabuleiro[8] == 'O') or
    (tabuleiro[0] == 'O' and tabuleiro[3] == 'O' and tabuleiro[6] == 'O') or
    (tabuleiro[1] == 'O' and tabuleiro[4] == 'O' and tabuleiro[7] == 'O') or
    (tabuleiro[2] == 'O' and tabuleiro[5] == 'O' and tabuleiro[8] == 'O') or
    (tabuleiro[0] == 'O' and tabuleiro[4] == 'O' and tabuleiro[8] == 'O') or
    (tabuleiro[2] == 'O' and tabuleiro[4] == 'O' and tabuleiro[6] == 'O')):
        return 1

    flag = True
    for i in range(0,9):
        if(tabuleiro[i] == '-'):
            flag = False
    if(flag == True):
        return 0
    
    return -2

def main():
    instancia = jogo()
    instancia.jogar()
main()
