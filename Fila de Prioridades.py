#-----------------------------------------------------------------------------------------------------------------------
atividades = input().split()
prioridade = []
for x in range(0,len(atividades),2):
    prioridade.append([atividades[x], int(atividades[x+1])])


prioridade = sorted(prioridade, key=lambda t:t[1], reverse=1)
atividade_realizar = int(input())
#-----------------------------------------------------------------------------------------------------------------------
for i in range(0,atividade_realizar):
    if atividade_realizar == 0:
        pass
    elif atividade_realizar != 0:
        prioridade.pop()
        atividade_realizar -= 1
#-----------------------------------------------------------------------------------------------------------------------


prioridade = sorted(prioridade, key=lambda t:t[1], reverse=0)


#-----------------------------------------------------------------------------------------------------------------------
print(f'Tamanho da fila: {len(prioridade)}')

for lista in range(len(prioridade)):
    print(f'Atividade: {prioridade[lista][0]}, Prioridade: #{prioridade[lista][1]}')