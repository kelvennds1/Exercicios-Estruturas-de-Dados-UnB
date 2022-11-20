stack = []
aux = 1
while aux != 0:
    aux = int(input())
    stack.append(aux)
pesoCerto = int(input())
stack.remove(0)
somaPeso = []
somaAnil = []
for peso in stack[::-1]:
    somaPeso.append(peso) 
    somaAnil.append(peso)
    if peso != pesoCerto:
        print(f'Peso retirado: {peso}')
        
    elif peso == pesoCerto:
        print(f'Peso retirado: {peso}')
        break
    

print(f'Anilhas retiradas: {len(somaAnil)}')
print(f'Peso total movimentado: {sum(somaPeso)}')


