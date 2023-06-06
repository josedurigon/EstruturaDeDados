'''
graph = {
    "A":['B','C','F'],
    'B':['D'],
    'D':['F'],
    'C':['E']
}
'''

graph = {
    "A": ['B', 'C', 'F'],
    "B": ['D'],
    "C": ['E'],
    "D": ['F'],
    "E": [],
    "F": [],
    "G": ['H'],
    "H": ['I'],
    "I": ['J'],
    "J": ['K'],
    "K": []
}

#Tratar o grafo como se fosse acessar uma matriz 2x2

index_to_vertex={
    0: 'A',
    1:'B' ,
    2:'C',
    3:'D',
    4:'E',
    5:'F',
    6:'G',
    7:'H',
    8:'I',
    9:'J',
    10:'K'
}
'''
adj_matrix = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0]
]
'''


'''
def DFS (graph, source):    
    stack =[source]
    visited = set()
    while stack:
        if stack != None:
            current = stack.pop()
            print(current)
            if current not in visited:
                if current in graph:
                    for neighbor in graph[current]:
                        stack.append(neighbor)
                        visited.add(current)
'''
def DFS(graph, adj_matrix, source):
    stack = [source]
    visited = set()
    while stack:
        current = stack.pop()
        print(current)
        if current not in visited:
            visited.add(current)
            if current in graph:
                neighbors = graph[current]
                properties = adj_matrix[vertices.index(current)]
                for i in range(len(neighbors)):
                    neighbor = neighbors[i]
                    property_value = properties[i][1] if i < len(properties) else None
                    if property_value:
                        print(f"Propriedade: {property_value}")
                    stack.append(neighbor)






#print(graph['A'][1])

# Definindo os vértices do grafo
vertices = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']

# Criando a matriz de adjacência preenchida com listas vazias
adj_matrix = [[] for _ in range(len(vertices))]

# Adicionando as propriedades de relacionamento à matriz de adjacência
adj_matrix[0] = [
    (1, 'TEMPO'), (2, 'CONSUMO_MEDIO'), (5, 'DISTANCIA'), (8, 'VELOCIDADE_MEDIA')
]
adj_matrix[1] = [(3, 'TEMPO'), (6, 'CONSUMO_MEDIO'), (9, 'DISTANCIA'),(10, 'VELOCIDADE_MEDIA')]
adj_matrix[2] = [(4, 'TEMPO'), (7, 'CONSUMO_MEDIO'), (10, 'DISTANCIA'),(11, 'VELOCIDADE_MEDIA')]

# Imprimindo a matriz de adjacência
'''
for row in adj_matrix:
    print(row)
'''



DFS(graph, adj_matrix, 'A')