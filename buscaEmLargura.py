from collections import deque

def busca_em_largura(grafo, inicio, objetivo):
    fila = deque([(inicio, [inicio])])
    visitados = set([inicio])
    
    while fila:
        (vertice, caminho) = fila.popleft()
        if vertice == objetivo:
            return caminho
        for proximo_vertice in grafo[vertice]:
            if proximo_vertice not in visitados:
                visitados.add(proximo_vertice)
                fila.append((proximo_vertice, caminho + [proximo_vertice]))

# Exemplo 
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

caminho = busca_em_largura(grafo, 'A', 'F')
print("Caminho encontrado:", caminho)