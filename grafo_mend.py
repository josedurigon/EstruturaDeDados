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

lista.append(("A", "B", {"tempo": 5, "consumo_medio": 3, "distancia": 10, "velocidade_media": 60}))
lista.append(("A", "C", {"tempo": 7, "consumo_medio": 4, "distancia": 12, "velocidade_media": 55}))


def addGrafo(cidade, tempo, distancia, consumo_medio, velocidade_media):
    grafo = {
        "cidade":cidade,
        "tempo":tempo,
        "distancia":distancia,
        "consumo_medio":consumo_medio,
        "velocidade_media": velocidade_media
    }
    lista.append(grafo)


def infoGrafo(grafo, no):
    node = grafo[no]
    print("Nó: ", no["cidade"])
    print("Tempo", no["tempo"])
    print("consumo medio", no["consumo_medio"])
    print("Distancia", no["distancia"])
    print("Velocidade media", no["velocidade_media"])


def imprimir_nos_adjacentes(grafo, lista, no):
    for conexao in lista:
        if conexao[0] == no:
            proximo_no = grafo[conexao[1]]
            print("Nó Adjacente:", proximo_no["nome"])
            print("Tempo:", conexao[2]["tempo"])


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

