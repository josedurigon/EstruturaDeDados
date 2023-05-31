grafo =[]
listaAdjacencia = []

node1 = {"cidade": "A", "tempo": 10, "consumo_medio": 5, "distancia": 20, "velocidade_media": 50}
node2 = {"cidade": "B", "tempo": 15, "consumo_medio": 6, "distancia": 25, "velocidade_media": 40}
node3 = {"cidade": "C", "tempo": 8, "consumo_medio": 4, "distancia": 15, "velocidade_media": 60}

grafo.append(node1)
grafo.append(node2)
grafo.append(node3)


listaAdjacencia.append({"origem": "A", "destino": "B", "dados": {"tempo": 5, "consumo_medio": 3, "distancia": 10, "velocidade_media": 60}}) #correto
listaAdjacencia.append({"origem": "A", "destino": "C", "dados": {"tempo": 7, "consumo_medio": 4, "distancia": 12, "velocidade_media": 55}}) #correto

def atribuir_relacionamentos_grafo(grafo, listaAdjacencia):
    grafo_completo = {}

    for node in grafo:
        cidade = node['cidade']
        grafo_completo[cidade] = {'dados': node, 'adjacencias': []}

    for aresta in listaAdjacencia:
        origem = aresta['origem']
        destino = aresta['destino']
        dados = aresta['dados']

        if origem in grafo_completo and destino in grafo_completo:
            grafo_completo[origem]['adjacencias'].append((destino, dados))
        else:
            print(f"Erro: Cidades de origem ou destino inválidas - Origem: {origem}, Destino: {destino}")

    return grafo_completo

def novoGrafo(cidade, tempo, distancia, consumo_medio, velocidade_media):
    novo_no = {
        "cidade":cidade,
        "tempo":tempo,
        "distancia":distancia,
        "consumo_medio":consumo_medio,
        "velocidade_media": velocidade_media
    }
    grafo.append(novo_no)