#min_e int  -> missionarios esquerda
#min_d int -> missionarios direita
#can_e int -> canibais esquerda
#can_d int -> canibais direita
#barco -> 'E' ou 'D'
import time
class Estado:
    def __init__(self,min_e,min_d,can_e,can_d,barco):
        self.min_e = min_e
        self.min_d = min_d
        self.can_e = can_e
        self.can_d = can_d
        self.barco = barco
        self.pai = None
        self.filhos = []

    def ver_estado(self):
        print(self.min_e,self.min_d,self.can_e,self.can_d,self.barco)

    def verificar_solucao(self):
        missionarios = False
        canibais = False

        if(self.min_d == 3 and self.min_e == 0):
            missionarios = True
        if(self.can_d == 3 and self.can_e == 0):
            canibais = True
    
        return missionarios and canibais

    def estado_valido(self):
        #Não pode passar de 3 em cada lado, ou ficar negativo
        if(self.min_e > 3 or self.min_e < 0):
            return False
        if(self.min_d > 3 or self.min_d < 0):
            return False
        if(self.can_e > 3 or self.can_e < 0):
            return False
        if(self.can_d > 3 or self.can_d < 0):
            return False

        if ((self.min_e == 0 or self.min_e >= self.can_e) and (self.min_d == 0 or self.min_d >= self.can_d)):
            return True
        
    def gerar_filho(self):
        #Lista com os possiveis movimentos:
        movimentos = [
            [1,0],
            [1,1], #[missionarios, canibais]
            [2,0],
            [0,1],
            [0,2],
        ]

        #seta a nova posição do barco
        barco = 't' #temporario
        if(self.barco == 'e'):
            barco = 'd'
        elif(self.barco == 'd'):
            barco = 'e'

        for movimento in movimentos:    #pra cada movimento, gera um novo estado
            missionarios_esq = 0
            missionarios_dir = 0
            canibais_esq = 0
            canibais_dir = 0
            if(barco == 'd'):
                #Vamos p/direita
                missionarios_esq = self.min_e - movimento[0]
                missionarios_dir = self.min_d + movimento[0]

                canibais_esq = self.can_e - movimento[1]
                canibais_dir = self.can_d + movimento[1]

            elif(barco == 'e'):
                #voltar para a margem inicial
                missionarios_esq = self.min_e + movimento[0]
                missionarios_dir = self.min_d - movimento[0]

                canibais_esq = self.can_e + movimento[1]
                canibais_dir = self.can_d - movimento[1]
                
            novo = Estado(missionarios_esq,missionarios_dir,canibais_esq,canibais_dir,barco)
            novo.pai = self
            if(novo.estado_valido()):
                self.filhos.append(novo)
            
           
               
class Solucao:
    def __init__(self):
        #Lista com todos os estados que devemos explorar
        #primeiro, coloca o estado inicial
        self.lista = []
        primeiro = Estado(3,0,3,0,'e')
        self.lista.append(primeiro)

        self.caminho = []

    def gerar_solucao(self):
        #verificar se é solução -> gerar filhos -> yolo
        #Iterar pelos nós da lista
        for estado in self.lista:
            if(estado.verificar_solucao()):#VERIFICA SE É SOLUÇÃO
                self.caminho.insert(0,estado)#ACHEI, GUARDA NA LISTA AÍ

                while(estado.pai != None):#VAMO LOOPAR ATÉ CHEGAR NA ORIGEM
                    self.caminho.insert(0,estado)#COLOCA NA PRIMEIRA POSIÇÃO
                    estado = estado.pai#SETA O NOVO ESTADO PRA SER O PAI DELE (tipo recursão)
                break

            estado.gerar_filho()
            for i in estado.filhos:
                self.lista.append(i)
    
    def mostrar_caminho(self):
        for elemento in self.caminho:
            elemento.ver_estado()
        

def main():
    resolver = Solucao()
    resolver.gerar_solucao()
    resolver.mostrar_caminho()
main()