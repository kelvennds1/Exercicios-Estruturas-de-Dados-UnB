entrada = input().split()
tamFila = int(input())
dictAtividades = dict()

for i in range(0,len(entrada),2):
    if entrada[i] in dictAtividades:
        dictAtividades['#'+entrada[i]] = int(entrada[i+1])
    else:
        dictAtividades[entrada[i]] = int(entrada[i+1])
        
dictAtividades = dict(reversed(sorted(dictAtividades.items(), key=lambda x:x[1])))
resultadoFila = (len(entrada)//2)-tamFila
print(dictAtividades)
if resultadoFila <= 0:
    print(f'Tamanho da fila: 0')
    exit()
else:
    for i in range(tamFila):
        dictAtividades.popitem()
    
dictAtividades = dict(reversed(dictAtividades.items()))
print(f'Tamanho da fila: {resultadoFila}')
for (k, v) in dictAtividades.items():
    if '#' in k:
        print(f'Atividade: {k[1:]}, Prioridade: #{v}')
    else:
        print(f'Atividade: {k}, Prioridade: #{v}')