#---------------------------------Entrada-------------------------------------
# Formada por duas linhas. A primeira linha contém a relação de atividades. 
# Cada atividade é formada por uma única palavra com o nome da tarefa, 
# seguida de um número inteiro Y que representa a prioridade associada a esta atividade (1≤Y≤10). 
# A tarefa de maior prioridade é representada pelo número 1 e a de menor prioridade pelo número 10

entrada = input().split()

#A segunda linha contém o valor inteiro (X≥0) que representa a quantidade total de atividades que se pode realizar no período.

tamFila = int(input())

#---------------------------------Tratamento-----------------------------------

dictAtividades = dict() #Dicionario para guardar atividade e prioridade

for i in range(0,len(entrada),2): # Atribuição K = Atividade, V = Prioridada
    if entrada[i] in dictAtividades:
        dictAtividades['#'+entrada[i]] = int(entrada[i+1]) # Caso já exista atividade com mesmo nome, adicionar # para não substituir
    else:
        dictAtividades[entrada[i]] = int(entrada[i+1])

#-------------------------------Usando dict com fila--------------------------

dictAtividades = dict(reversed(sorted(dictAtividades.items(), key=lambda x:x[1]))) # Ordenação por valor(prioridade), e reversão para trabalhar como fila

resultadoFila = (len(dictAtividades))-tamFila 

if resultadoFila <= 0:
    print(f'Tamanho da fila: 0')
    exit()
else: #Removendo do inicio da fila
    for i in range(tamFila):
        dictAtividades.popitem()

#---------------------------------Saida-------------------------
#Apresente as informações conforme os exemplos. Na primeira linha, apresente o tamanho da fila. 
# Para cada elemento na fila cujas atividades não foram cumpridas, apresente suas informações. 
    
dictAtividades = dict(reversed(dictAtividades.items())) #Voltando a ordem inicial para realizar o print

print(f'Tamanho da fila: {resultadoFila}')

for (k, v) in dictAtividades.items():
    if '#' in k:
        print(f'Atividade: {k[1:]}, Prioridade: #{v}')
    else:
        print(f'Atividade: {k}, Prioridade: #{v}')
