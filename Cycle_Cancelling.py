import numpy as np

def ciclo_cancelling(grafo, costo, flusso_iniziale):
    n = len(grafo)
    flusso = np.array(flusso_iniziale)
    
    def trova_cicli_neg():
        dist = [float('inf')] * n
        padre = [-1] * n
        origine = 0
        dist[origine] = 0
        for _ in range(n):
            for u in range(n):
                for v in range(n):
                    if grafo[u][v] > 0 and dist[u] + costo[u][v] < dist[v]:
                        dist[v] = dist[u] + costo[u][v]
                        padre[v] = u
        
        for u in range(n):
            for v in range(n):
                if grafo[u][v] > 0 and dist[u] + costo[u][v] < dist[v]:
                    ciclo = [v]
                    while ciclo[0] != v or len(ciclo) == 1:
                        ciclo.insert(0, padre[ciclo[0]])
                    return ciclo
        
        return None

    while True:
        ciclo_negativo = trova_cicli_neg()
        if ciclo_negativo is None:
            break
        delta = min([grafo[u][v] for u, v in zip(ciclo_negativo, ciclo_negativo[1:])])
        for u, v in zip(ciclo_negativo, ciclo_negativo[1:]):
            flusso[u][v] += delta
            flusso[v][u] -= delta
    
    return flusso

grafo = [
    [0, 4, 2, 0],
    [0, 0, 2, 3],
    [0, 0, 0, 5],
    [0, 0, 0, 0]
]

costo = [
    [0, 2, 2, 0],
    [0, 0, 1, 3],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

flusso_iniziale = [
    [0, 3, 1, 0],
    [0, 0, 0, 3],
    [0, 0, 0, 1],
    [0, 0, 0, 0]
]

flusso_finale = ciclo_cancelling(grafo, costo, flusso_iniziale)
print("Flusso finale:")
for r in flusso_finale:
    print(r)
