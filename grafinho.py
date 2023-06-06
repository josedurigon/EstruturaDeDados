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

#'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1
adj_matrix = [
                                #1                                                      2                                                                   3                                                               4                                                           5                                                           6                                                               7                                                           8                                                           9                                                           10
    [[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}]], #1
    [[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}]], #2
    [[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}]], #3
    [[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}]], #4
    [[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}]], #5
    [[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}]], #6
    [[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}]], #7
    [[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}]], #8
    [[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}]], #9
    [[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}]]  #10
]



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
'''


for row in adj_matrix:
    print(row)




