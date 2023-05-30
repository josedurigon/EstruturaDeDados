#Informação relacionada a ligação: distancia, tempo, consumo e velocidade media (vamos chamar de dados de relação para facilitar)


grafo = {}
lista =[]

node1 = {"cidade": "A", "tempo": 10, "consumo_medio": 5, "distancia": 20, "velocidade_media": 50}
node2 = {"cidade": "B", "tempo": 15, "consumo_medio": 6, "distancia": 25, "velocidade_media": 40}
node3 = {"cidade": "C", "tempo": 8, "consumo_medio": 4, "distancia": 15, "velocidade_media": 60}

grafo[node1["cidade"]] = node1
grafo[node2["cidade"]] = node2
grafo[node3["cidade"]] = node3
#aqui o DICIONARIO grafo recebe os dicionarios NODE e os armazena pelo nome da cidade (pela chave cidade no caso).
#Como os dados de relação somente fazem sentido em uma relação, cria-se portanto uma lista (vetor mesmo) para armazenar esses dados.

lista.append({"origem": "A", "destino": "B", "dados": {"tempo": 5, "consumo_medio": 3, "distancia": 10, "velocidade_media": 60}}) #correto
lista.append({"origem": "A", "destino": "C", "dados": {"tempo": 7, "consumo_medio": 4, "distancia": 12, "velocidade_media": 55}}) #correto


def addGrafo(cidade, tempo, distancia, consumo_medio, velocidade_media):
    novo_no = {
        "cidade":cidade,
        "tempo":tempo,
        "distancia":distancia,
        "consumo_medio":consumo_medio,
        "velocidade_media": velocidade_media
    }
    lista.append(novo_no)
    print("*** Adicionado ***")
    
    


def infoGrafo(grafo, no):
    node = grafo[no]
    print("Nó: ", node["cidade"])
    print("Tempo", node["tempo"])
    print("consumo medio", node["consumo_medio"])
    print("Distancia", node["distancia"])
    print("Velocidade media", node["velocidade_media"])

def imprimir_nos_adjacentes(grafo, lista, no):
    for conexao in lista:
        if isinstance(conexao, dict) and "origem" in conexao and conexao["origem"] == no:
            proximo_no = grafo.get(conexao.get("destino"))
            if proximo_no:
                print("Nó Adjacente:", proximo_no["cidade"])
                print("Tempo:", conexao["dados"]["tempo"])


'''
def imprimir_nos_adjacentes(grafo, lista, no):
    for conexao in lista:
        if "origem" in conexao and conexao["origem"] == no:
            destino = conexao.get("destino")
            if destino in grafo:
                proximo_no = grafo[destino]
                print("Nó Adjacente:", proximo_no["cidade"])
                print("Tempo:", conexao["dados"]["tempo"])

'''
'''
def depth_first_search(grafo, no_inicial):
    visitados = set()
    pilha = [no_inicial]
    while pilha:
        no = pilha.pop()

        if no not in visitados:
            visitados.add(no)
            print(f"Visitando no: {no}")

            vizinhos = grafo[no]

            for vizinho in vizinhos:
                if vizinhos not in visitados:
                    pilha.append(vizinho)


'''
def depth_first_search(grafo, no_inicial):
    visitados = set()
    pilha = [no_inicial]
    while pilha:
        no = pilha.pop()

        if no not in visitados:
            visitados.add(no)
            print(f"Visitando nó: {no}")

            vizinhos = grafo[no]

            for vizinho in vizinhos:
                if vizinho not in visitados:
                    pilha.append(vizinho)

#testes abaixo

addGrafo("D", 12, 18, 7, 55)
addGrafo("E", 9, 30, 6, 45)

infoGrafo(grafo, "A")
print("\n\n",lista,"\n\n")
imprimir_nos_adjacentes(grafo, lista, "A")
depth_first_search(grafo, "A")



