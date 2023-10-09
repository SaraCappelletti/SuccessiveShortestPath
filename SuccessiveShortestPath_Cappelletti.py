def bellman_ford(partenza, n, flusso):
    distanza = [float('inf')] * n
    distanza[partenza] = 0
    padre = [-1] * n

    for _ in range(n):
        for u in range(n):
            for v in range(n):
                if flusso[u][v] < grafo_capienza[u][v]:
                    if distanza[u] + costo[u][v] < distanza[v]:
                        distanza[v] = distanza[u] + costo[u][v]
                        padre[v] = u

    return distanza, padre

def successive_shortest_path(grafo_capienza, partenza, destinazione, costo):
    n = len(grafo_capienza)
    flusso = [[0] * n for _ in range(n)]
    
    while True:
        distanza, padre = bellman_ford(partenza, n, flusso)
        if distanza[destinazione] == float('inf'):
            break

        delta = float('inf')
        v = destinazione

        while v != partenza:
            u = padre[v]
            delta = min(delta, grafo_capienza[u][v] - flusso[u][v])
            v = u

        v = destinazione

        while v != partenza:
            u = padre[v]
            flusso[u][v] += delta
            flusso[v][u] -= delta
            v = u

    min_costo = 0
    for u in range(n):
        for v in range(n):
            min_costo += flusso[u][v] * costo[u][v]

    return min_costo, flusso


# Esempio di utilizzo
# La riga i e la colonna j della matrice grafo rappresentano l'arco dall'N-esimo nodo al M-esimo nodo.
# Gli zeri indicano l'assenza di un collegamento diretto
# Es: grafo_capienza[0][1] rappresenta l'arco dall'Nodo 0 al Nodo 1 con una capacità di 4 unità.

grafo_capienza = [
    [0, 4, 0, 2, 0, 0],
    [0, 0, 2, 6, 0, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 8, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 0, 0]
]

costo = [
    [0, 0, 0, 0, 0, 0],
    [0, 0, 4, 1, 0, 0],
    [0, 0, 0, 0, 0, 4],
    [0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0]
]

partenza = 0
destinazione = 5

min_costo, flusso = successive_shortest_path(grafo_capienza, partenza, destinazione, costo)
print("Costo minimo:", min_costo)
print("Flusso:")
for r in flusso:
    print(r)

