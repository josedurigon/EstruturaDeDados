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
'''
adj_matrix = [
                                #1                                                      2                                                                   3                                                               4                                                           5                                                           6                                                               7                                                           8                                                           9                                                           10
    [[{'tempo':0,'distancia':0,'consumo':0,'velocidade_media':0}],[{'tempo':10,'distancia':15,'consumo':5,'velocidade_media':80}],[{'tempo':12,'distancia':34,'consumo':15,'velocidade_media':100}],[{'tempo':90,'distancia':100,'consumo':20,'velocidade_media':100}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}],[{'tempo':1,'distancia':1,'consumo':1,'velocidade_media':1}]], #1
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
'''

adj_matrix = [
    [ #1
        [{'tempo': 0, 'distancia': 0, 'consumo': 0, 'velocidade_media': 0}],        #1
        [{'tempo': 10, 'distancia': 15, 'consumo': 5, 'velocidade_media': 80}],     #2
        [{'tempo': 12, 'distancia': 34, 'consumo': 15, 'velocidade_media': 100}],   #3
        [{'tempo': 90, 'distancia': 100, 'consumo': 20, 'velocidade_media': 100}],  #4
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 1}],        #5
        [{'tempo': 8, 'distancia': 7, 'consumo': 3, 'velocidade_media': 45}],       #6
        [{'tempo': 6, 'distancia': 25, 'consumo': 10, 'velocidade_media': 60}],     #7
        [{'tempo': 30, 'distancia': 50, 'consumo': 15, 'velocidade_media': 80}],    #8
        [{'tempo': 4, 'distancia': 2, 'consumo': 2, 'velocidade_media': 30}],       #9
        [{'tempo': 9, 'distancia': 12, 'consumo': 6, 'velocidade_media': 70}]       #10
    ],
    [#2
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 1}],
        [{'tempo': 0, 'distancia': 0, 'consumo': 0, 'velocidade_media': 0}],
        [{'tempo': 5, 'distancia': 8, 'consumo': 3, 'velocidade_media': 60}],
        [{'tempo': 7, 'distancia': 9, 'consumo': 4, 'velocidade_media': 70}],
        [{'tempo': 5, 'distancia': 4, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 1, 'velocidade_media': 30}],
        [{'tempo': 6, 'distancia': 7, 'consumo': 4, 'velocidade_media': 60}],
        [{'tempo': 10, 'distancia': 15, 'consumo': 8, 'velocidade_media': 90}],
        [{'tempo': 8, 'distancia': 7, 'consumo': 3, 'velocidade_media': 45}],
        [{'tempo': 3, 'distancia': 5, 'consumo': 2, 'velocidade_media': 35}]
    ],
    [#3
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 1}],
        [{'tempo': 6, 'distancia': 10, 'consumo': 4, 'velocidade_media': 70}],
        [{'tempo': 0, 'distancia': 0, 'consumo': 0, 'velocidade_media': 0}],
        [{'tempo': 7, 'distancia': 8, 'consumo': 5, 'velocidade_media': 70}],
        [{'tempo': 3, 'distancia': 6, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 3, 'distancia': 5, 'consumo': 2, 'velocidade_media': 35}],
        [{'tempo': 1, 'distancia': 2, 'consumo': 1, 'velocidade_media': 20}],
        [{'tempo': 6, 'distancia': 9, 'consumo': 4, 'velocidade_media': 50}],
        [{'tempo': 4, 'distancia': 8, 'consumo': 3, 'velocidade_media': 40}],
        [{'tempo': 2, 'distancia': 4, 'consumo': 2, 'velocidade_media': 30}]
    ],
    [#4
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 1}],
        [{'tempo': 5, 'distancia': 7, 'consumo': 3, 'velocidade_media': 60}],
        [{'tempo': 4, 'distancia': 5, 'consumo': 2, 'velocidade_media': 50}],
        [{'tempo': 0, 'distancia': 0, 'consumo': 0, 'velocidade_media': 0}],
        [{'tempo': 6, 'distancia': 7, 'consumo': 4, 'velocidade_media': 60}],
        [{'tempo': 2, 'distancia': 4, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 5, 'distancia': 5, 'consumo': 3, 'velocidade_media': 40}],
        [{'tempo': 3, 'distancia': 6, 'consumo': 3, 'velocidade_media': 50}],
        [{'tempo': 1, 'distancia': 2, 'consumo': 1, 'velocidade_media': 20}],
        [{'tempo': 7, 'distancia': 8, 'consumo': 4, 'velocidade_media': 70}]
    ],
    [#5
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 1}],
        [{'tempo': 6, 'distancia': 7, 'consumo': 3, 'velocidade_media': 70}],
        [{'tempo': 3, 'distancia': 4, 'consumo': 2, 'velocidade_media': 50}],
        [{'tempo': 8, 'distancia': 10, 'consumo': 5, 'velocidade_media': 90}],
        [{'tempo': 0, 'distancia': 0, 'consumo': 0, 'velocidade_media': 0}],
        [{'tempo': 4, 'distancia': 5, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 3, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 10}],
        [{'tempo': 5, 'distancia': 6, 'consumo': 3, 'velocidade_media': 60}]
    ],
    [#6
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 1}],
        [{'tempo': 5, 'distancia': 6, 'consumo': 3, 'velocidade_media': 50}],
        [{'tempo': 4, 'distancia': 4, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 5, 'distancia': 7, 'consumo': 3, 'velocidade_media': 60}],
        [{'tempo': 6, 'distancia': 8, 'consumo': 4, 'velocidade_media': 70}],
        [{'tempo': 0, 'distancia': 0, 'consumo': 0, 'velocidade_media': 0}],
        [{'tempo': 3, 'distancia': 4, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 1, 'distancia': 2, 'consumo': 1, 'velocidade_media': 20}],
        [{'tempo': 7, 'distancia': 9, 'consumo': 4, 'velocidade_media': 80}]
    ],
    [#7
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 1}],
        [{'tempo': 4, 'distancia': 5, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 2, 'distancia': 4, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 3, 'distancia': 4, 'consumo': 3, 'velocidade_media': 40}],
        [{'tempo': 4, 'distancia': 6, 'consumo': 3, 'velocidade_media': 60}],
        [{'tempo': 0, 'distancia': 0, 'consumo': 0, 'velocidade_media': 0}],
        [{'tempo': 1, 'distancia': 2, 'consumo': 1, 'velocidade_media': 20}],
        [{'tempo': 1, 'distancia': 2, 'consumo': 1, 'velocidade_media': 20}],
        [{'tempo': 5, 'distancia': 7, 'consumo': 3, 'velocidade_media': 60}]
    ],
    [#8
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 1}],
        [{'tempo': 3, 'distancia': 4, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 4, 'distancia': 6, 'consumo': 3, 'velocidade_media': 50}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 2, 'distancia': 4, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 10}],
        [{'tempo': 0, 'distancia': 0, 'consumo': 0, 'velocidade_media': 0}],
        [{'tempo': 1, 'distancia': 2, 'consumo': 1, 'velocidade_media': 20}],
        [{'tempo': 5, 'distancia': 6, 'consumo': 3, 'velocidade_media': 50}]
    ],
    [#9
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 1}],
        [{'tempo': 6, 'distancia': 8, 'consumo': 3, 'velocidade_media': 70}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 3, 'distancia': 4, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 1, 'distancia': 2, 'consumo': 1, 'velocidade_media': 20}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 2, 'distancia': 4, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 0, 'distancia': 0, 'consumo': 0, 'velocidade_media': 0}],
        [{'tempo': 4, 'distancia': 6, 'consumo': 3, 'velocidade_media': 50}]
    ],
    [#10
        [{'tempo': 1, 'distancia': 1, 'consumo': 1, 'velocidade_media': 1}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 3, 'distancia': 5, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 1, 'distancia': 2, 'consumo': 1, 'velocidade_media': 20}],
        [{'tempo': 2, 'distancia': 3, 'consumo': 2, 'velocidade_media': 30}],
        [{'tempo': 7, 'distancia': 9, 'consumo': 4, 'velocidade_media': 70}],
        [{'tempo': 1, 'distancia': 2, 'consumo': 1, 'velocidade_media': 20}],
        [{'tempo': 2, 'distancia': 4, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 4, 'distancia': 5, 'consumo': 2, 'velocidade_media': 40}],
        [{'tempo': 0, 'distancia': 0, 'consumo': 0, 'velocidade_media': 0}]
    ]
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




