graph = {
    "A":['B','C','F'],
    'B':['D'],
    'D':['F'],
    'C':['E']
}
#Tratar o grafo como se fosse acessar uma matriz 2x2


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



DFS(graph,'A')
#print(graph['A'][1])