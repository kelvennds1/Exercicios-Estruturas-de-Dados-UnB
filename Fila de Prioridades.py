#---------------------------------Entrada-------------------------------------
# Formada por duas linhas. A primeira linha contém a relação de atividades. 
# Cada atividade é formada por uma única palavra com o nome da tarefa, 
# seguida de um número inteiro Y que representa a prioridade associada a esta atividade (1≤Y≤10). 
# A tarefa de maior prioridade é representada pelo número 1 e a de menor prioridade pelo número 10

class addAtividade:
    def __init__(self, atividade, prioridade):
        self.item = atividade
        self.prioridade = prioridade
    def __str__(self):
        return str(self.item) + '' + str(self.prioridade)

class filaPrioridade:

    def __init__(self):
        self.itens = []

    def is_empty(self):
        return self.itens == []

    def size(self):
        return len(self.itens)

    def enqueue(self,atv,prioridade):
        atividade = addAtividade(atv,prioridade)
        self.itens.insert(0, atividade)
    
    def dequeue(self):
        if self.is_empty():
            print('Lista Vazia')
        else:
            print('Dequeue')
            posicao = 0 
            menor = self.itens[posicao].prioridade
            for i in range(self.size()):
                if self.itens[i].prioridade < menor:
                    posicao = i
                    menor = self.itens[i].prioridade
            removido = self.itens.pop(posicao)
            return removido.item
    
    def print_queue(self):
        L = []
        for x in self.itens:
            L.append(x.item)
        print(L)


entrada = input().split()

#A segunda linha contém o valor inteiro (X≥0) que representa a quantidade total de atividades que se pode realizar no período.

tamFila = int(input())
atividades = filaPrioridade()
#---------------------------------Tratamento-----------------------------------
for i in range(0,len(entrada),2):
    atividades.enqueue(entrada[i], entrada[i+1]) 


#---------------------------------Saida-------------------------
#Apresente as informações conforme os exemplos. Na primeira linha, apresente o tamanho da fila. 
# Para cada elemento na fila cujas atividades não foram cumpridas, apresente suas informações. 
