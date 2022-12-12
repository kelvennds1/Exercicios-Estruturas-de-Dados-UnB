def valorMax(n, lista, k):
    maximo = 0
    res = []
    for i in range(n - k + 1):
        maximo = lista[i]
        for j in range(1, k):
            if lista[i + j] > maximo:
                maximo = lista[i + j]
        res.append(maximo)
    return res
 

n = int(input())
lista = [int(x) for x in input().split()]
k = int(input())
print(*valorMax(n, lista, k), sep = '  ')

