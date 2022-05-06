class no:
    def __init__(self,id,adj,estacoes):
        self.pai = None

        self.custo = 0 
        self.peso = 0
        
        self.id = id #Identifica qual estação é 

        self.adj = [] #lista de adjacencias
        for i in range(0,len(adj)):
            self.adj.append(adj[i])

        self.estacoes = [] #Lista com estações que o nó atual faz parte
        for i in range(0,len(estacoes)):
            self.estacoes.append(estacoes[i])
        self.estacao = None #Essa estação é a estação que faz parte do caminho
                
    def eh_solucao(self, no_destino):
        if(self.id == no_destino.id):
            return True
        return False

    def analisar_estacoes(self,no):
        #Eu vejo as estações do nó filho, aquela que tbm tiver no nó pai, é a estação que estamos
        #salvo ela como estação desse nó e se o pai tiver estacao = none, significa que é o no de origem
        for estacao in no.estacoes:
            if estacao in self.estacoes:
                no.estacao = estacao
                break
        if(no.estacao == self.estacao or self.estacao == None):#N teve baldeação #None indica que é o nó pai
            return 0
        return 4#teve

    def gerar_filhos(self,fronteira,visitados,nos,heuristica):
        for i in range(0,14): #vou loopar por toda a lista de adjacencia desse nó
            if(self.adj[i] != 0 and visitados[i] == 0): #se existe a possibilidade de ir para esse nó e ainda NÃO foi visitado...
                #inserir em ordem
                no = nos[i] #puxo o nó que tenho interesse (Meio que crio uma cópia)
                
                adicionar_baldeacao = self.analisar_estacoes(no)

                no.custo = self.custo + self.adj[i] + adicionar_baldeacao #Custo é o quanto gastei até agora + custo pra ir pra esse
                no.peso = heuristica[i] + no.custo  #o Peso é custo pra chegar a esse nó + a heuristica desse nó

                

                no.pai = self   #seto o pai desse nó...   
                flag_inseriu = 0

                #agora decidir onde encaixar esse nó na fronteira
                #procuro a posição que o meu novo nó tem seu custo menor que o atual
                for j in range (0,len(fronteira)): 
                    if(no.peso < fronteira[j].peso):
                        fronteira.insert(j,no)
                        flag_inseriu = 1
                        break
                #casos que o nó percorreu a lista toda e nao foi inserido
                #Basicamente, quando entra no fim da lista
                if(flag_inseriu == 0):
                    fronteira.append(no)

class solucao:
    def __init__(self,origem,destino,lista_nos,heuristica):

        self.heuristica = []
        for valor in heuristica: #passo a heuristica escolhida
            self.heuristica.append(valor)
        
        self.lista_nos = [] #copio a lista de nós
        for no in lista_nos:
            self.lista_nos.append(no)
        
        self.destino = destino

        self.fronteira = [origem] #nos na fronteira (Ordenada do menor custo para o maior)
        self.visitados = [0,0,0,0,0,0,0,0,0,0,0,0,0,0] #nos que já visitei (0 nao 1 sim)
        self.caminho = [] #caminho quando acha o destino

    def mostrar_caminho(self):
        for no in self.caminho:
            print('ID: {} CUSTO ACUMULADO (minutos): {} ESTACAO: {}'.format(no.id + 1,no.custo,no.estacao))
        

    def a_star(self):
        while True:
            no = self.fronteira.pop(0) #retiro o primeiro nó da fronteira
            if(self.visitados[no.id] == 1): #se ele já foi visitado antes, eu pulo fora
                continue

            if(no.eh_solucao(self.destino)): #se ele for solução...
                while(no.pai != None):#VAMO LOOPAR ATÉ CHEGAR NA ORIGEM
                    self.caminho.insert(0,no)# insiro na lista do caminho e continuo
                    no = no.pai
                break
            else:
                no.gerar_filhos(self.fronteira,self.visitados,self.lista_nos,self.heuristica) #gera os filhos...
                self.visitados[no.id] = 1 #marca visitado

def main():
    #Custo no nó numero_da_linha até os outros nós
    heuristica = [
    [0, 22, 40, 54, 80, 86, 78, 56, 36, 20, 36, 60, 60, 64],
    [22, 0, 18, 32, 58, 64, 56, 38, 22, 8, 34, 46, 42, 48],
    [40, 18, 0, 14, 40, 44, 38, 30, 20, 22, 42, 42, 26, 36],
    [54, 32, 14, 0, 26, 32, 24, 26, 26, 36, 52, 42, 22, 34],
    [80, 58, 40, 26, 0, 6, 4, 42, 50, 62, 76, 54, 32, 40],
    [86, 64, 44, 32, 6, 0, 8, 46, 56, 66, 82, 60, 34, 40],
    [78, 56, 38, 24, 4, 8, 0, 44, 50, 58, 76, 56, 26, 34],
    [56, 38, 30, 26, 42, 46, 44, 0, 18, 44, 36, 14, 50, 60],
    [36, 22, 20, 26, 50, 56, 50, 18, 0, 26, 24, 24, 46, 56],
    [20, 8, 22, 36, 62, 66, 58, 44, 26, 0, 40, 54, 40, 46],
    [36, 34, 42, 52, 76, 82, 76, 36, 24, 40, 0, 30, 70, 78],
    [60, 46, 42, 42, 54, 60, 56, 14, 24, 54, 30, 0, 62, 74],
    [60, 42, 26, 22, 32, 34, 26, 50, 46, 40, 70, 62, 0, 10],
    [64, 48, 36, 34, 40, 40, 34, 60, 56, 46, 78, 74, 10, 0]
    ]   

    #Lista de adjacencias: 0 = não tem como chegar, c.c = custo pra ir
    custo = [
    [0, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [22, 0, 18, 0, 0, 0, 0, 0, 22, 8, 0, 0, 0, 0],
    [0, 18, 0, 14, 0, 0, 0, 0, 0, 20, 0, 0, 26, 0],
    [0, 0, 14, 0, 26, 0, 0, 26, 0, 0, 0, 0, 22, 0],
    [0, 0, 0, 26, 0, 6, 4, 42, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 26, 42, 0, 0, 0, 18, 0, 0, 14, 0, 0],
    [0, 22, 20, 0, 0, 0, 0, 18, 0, 0, 24, 0, 0, 0],
    [0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 24, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 14, 0, 0, 0, 0, 0, 0],
    [0, 0, 26, 22, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 0]
    ]
    

    origem = int(input("Indique a origem (1 até 14): "))
    origem = origem -1
    destino = int(input("Indique o destino (0 até 14): "))
    destino = destino - 1

    e1 = no(0,custo[0],['Azul'])
    e2 = no(1,custo[1],['Azul','Amarelo'])
    e3 = no(2,custo[2],['Azul','Vermelho'])
    e4 = no(3,custo[3],['Azul','Verde'])
    e5 = no(4,custo[4],['Azul','Amarelo'])
    e6 = no(5,custo[5],['Azul'])
    e7 = no(6,custo[6],['Amarelo'])
    e8 = no(7,custo[7],['Amarelo','Verde'])
    e9 = no(8,custo[8],['Amarelo','Vermelho'])
    e10 = no(9,custo[9],['Amarelo'])
    e11 = no(10,custo[10],['Vermelho'])
    e12 = no(11,custo[11],['Verde'])
    e13 = no(12,custo[12],['Vermelho','Verde'])
    e14 = no(13,custo[13],['Verde'])

    #Lista com todos os nós
    nos = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11,e12,e13,e14]

    no_origem = nos[origem] #nó de origem
    no_destino = nos[destino] #nó de destino

    solve = solucao(no_origem,no_destino,nos,heuristica[destino])
    solve.a_star()
    solve.mostrar_caminho()

main()
