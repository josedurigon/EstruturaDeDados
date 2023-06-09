art='''
 /$$      /$$                                     /$$$$$$$              /$$                         /$$
| $$$    /$$$                                    | $$__  $$            | $$                        | $$
| $$$$  /$$$$  /$$$$$$   /$$$$$$   /$$$$$$       | $$  \ $$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$$| $$
| $$ $$/$$ $$ /$$__  $$ /$$__  $$ |____  $$      | $$$$$$$/ /$$__  $$|_  $$_/   |____  $$ /$$_____/| $$
| $$  $$$| $$| $$$$$$$$| $$  \ $$  /$$$$$$$      | $$__  $$| $$  \ $$  | $$      /$$$$$$$|  $$$$$$ |__/
| $$\  $ | $$| $$_____/| $$  | $$ /$$__  $$      | $$  \ $$| $$  | $$  | $$ /$$ /$$__  $$ \____  $$    
| $$ \/  | $$|  $$$$$$$|  $$$$$$$|  $$$$$$$      | $$  | $$|  $$$$$$/  |  $$$$/|  $$$$$$$ /$$$$$$$/ /$$
|__/     |__/ \_______/ \____  $$ \_______/      |__/  |__/ \______/    \___/   \_______/|_______/ |__/
                        /$$  \ $$                                                                      
                       |  $$$$$$/                                                                      
                        \______/    '''


grafo = {
    'Zurique': [
        {'DESTINO': 'Berna', 'PROPRIEDADES': {'TEMPO': 1.5, 'DISTANCIA': 123, 'VELOCIDADE_MEDIA': 82, 'CONSUMO_MEDIO': 7.2}},
        {'DESTINO': 'Genebra', 'PROPRIEDADES': {'TEMPO': 3, 'DISTANCIA': 280, 'VELOCIDADE_MEDIA': 93, 'CONSUMO_MEDIO': 9.1}},
        {'DESTINO': 'Basileia', 'PROPRIEDADES': {'TEMPO': 1.25, 'DISTANCIA': 85, 'VELOCIDADE_MEDIA': 68, 'CONSUMO_MEDIO': 5.6}}
    ],
    'Berna': [
        {'DESTINO': 'Zurique', 'PROPRIEDADES': {'TEMPO': 1.5, 'DISTANCIA': 123, 'VELOCIDADE_MEDIA': 82, 'CONSUMO_MEDIO': 7.2}},
        {'DESTINO': 'Genebra', 'PROPRIEDADES': {'TEMPO': 2.75, 'DISTANCIA': 230, 'VELOCIDADE_MEDIA': 84, 'CONSUMO_MEDIO': 6.8}},
        {'DESTINO': 'Lausanne', 'PROPRIEDADES': {'TEMPO': 1.25, 'DISTANCIA': 100, 'VELOCIDADE_MEDIA': 80, 'CONSUMO_MEDIO': 6.2}}
    ],
    'Genebra': [
        {'DESTINO': 'Zurique', 'PROPRIEDADES': {'TEMPO': 3, 'DISTANCIA': 280, 'VELOCIDADE_MEDIA': 93, 'CONSUMO_MEDIO': 9.1}},
        {'DESTINO': 'Berna', 'PROPRIEDADES': {'TEMPO': 2.75, 'DISTANCIA': 230, 'VELOCIDADE_MEDIA': 84, 'CONSUMO_MEDIO': 6.8}},
        {'DESTINO': 'Lausanne', 'PROPRIEDADES': {'TEMPO': 0.75, 'DISTANCIA': 62, 'VELOCIDADE_MEDIA': 85, 'CONSUMO_MEDIO': 5.1}}
    ],
    'Basileia': [
        {'DESTINO': 'Zurique', 'PROPRIEDADES': {'TEMPO': 1.25, 'DISTANCIA': 85, 'VELOCIDADE_MEDIA': 68, 'CONSUMO_MEDIO': 5.6}},
        {'DESTINO': 'Lucerna', 'PROPRIEDADES': {'TEMPO': 1, 'DISTANCIA': 67, 'VELOCIDADE_MEDIA': 65, 'CONSUMO_MEDIO': 4.8}},
        {'DESTINO': 'Interlaken', 'PROPRIEDADES': {'TEMPO': 2.5, 'DISTANCIA': 172, 'VELOCIDADE_MEDIA': 69, 'CONSUMO_MEDIO': 5.9}}
    ],
    'Lausanne': [
        {'DESTINO': 'Berna', 'PROPRIEDADES': {'TEMPO': 1.25, 'DISTANCIA': 100, 'VELOCIDADE_MEDIA': 80, 'CONSUMO_MEDIO': 6.2}},
        {'DESTINO': 'Genebra', 'PROPRIEDADES': {'TEMPO': 0.75, 'DISTANCIA': 62, 'VELOCIDADE_MEDIA': 85, 'CONSUMO_MEDIO': 5.1}},
        {'DESTINO': 'Lucerna', 'PROPRIEDADES': {'TEMPO': 2.5, 'DISTANCIA': 204, 'VELOCIDADE_MEDIA': 76, 'CONSUMO_MEDIO': 7.5}}
    ],
    'Lucerna': [
        {'DESTINO': 'Basileia', 'PROPRIEDADES': {'TEMPO': 1, 'DISTANCIA': 67, 'VELOCIDADE_MEDIA': 65, 'CONSUMO_MEDIO': 4.8}},
        {'DESTINO': 'Lausanne', 'PROPRIEDADES': {'TEMPO': 2.5, 'DISTANCIA': 204, 'VELOCIDADE_MEDIA': 76, 'CONSUMO_MEDIO': 7.5}},
        {'DESTINO': 'Interlaken', 'PROPRIEDADES': {'TEMPO': 1.75, 'DISTANCIA': 68, 'VELOCIDADE_MEDIA': 62, 'CONSUMO_MEDIO': 5.2}}
    ],
    'Interlaken': [
        {'DESTINO': 'Basileia', 'PROPRIEDADES': {'TEMPO': 2.5, 'DISTANCIA': 172, 'VELOCIDADE_MEDIA': 69, 'CONSUMO_MEDIO': 5.9}},
        {'DESTINO': 'Lucerna', 'PROPRIEDADES': {'TEMPO': 1.75, 'DISTANCIA': 68, 'VELOCIDADE_MEDIA': 62, 'CONSUMO_MEDIO': 5.2}},
        {'DESTINO': 'St. Moritz', 'PROPRIEDADES': {'TEMPO': 5, 'DISTANCIA': 291, 'VELOCIDADE_MEDIA': 82, 'CONSUMO_MEDIO': 9.3}}
    ],
    'St. Moritz': [
        {'DESTINO': 'Interlaken', 'PROPRIEDADES': {'TEMPO': 5, 'DISTANCIA': 291, 'VELOCIDADE_MEDIA': 82, 'CONSUMO_MEDIO': 9.3}},
        {'DESTINO': 'Lugano', 'PROPRIEDADES': {'TEMPO': 3.5, 'DISTANCIA': 190, 'VELOCIDADE_MEDIA': 78, 'CONSUMO_MEDIO': 8.5}},
        {'DESTINO': 'Zermatt', 'PROPRIEDADES': {'TEMPO': 4.75, 'DISTANCIA': 283, 'VELOCIDADE_MEDIA': 75, 'CONSUMO_MEDIO': 8.1}}
    ],
    'Lugano': [
        {'DESTINO': 'St. Moritz', 'PROPRIEDADES': {'TEMPO': 3.5, 'DISTANCIA': 190, 'VELOCIDADE_MEDIA': 78, 'CONSUMO_MEDIO': 8.5}},
        {'DESTINO': 'Zermatt', 'PROPRIEDADES': {'TEMPO': 5.25, 'DISTANCIA': 254, 'VELOCIDADE_MEDIA': 73, 'CONSUMO_MEDIO': 7.6}},
        {'DESTINO': 'Locarno', 'PROPRIEDADES': {'TEMPO': 0.75, 'DISTANCIA': 51, 'VELOCIDADE_MEDIA': 68, 'CONSUMO_MEDIO': 5.3}}
    ],
    'Zermatt': [
        {'DESTINO': 'St. Moritz', 'PROPRIEDADES': {'TEMPO': 4.75, 'DISTANCIA': 283, 'VELOCIDADE_MEDIA': 75, 'CONSUMO_MEDIO': 8.1}},
        {'DESTINO': 'Lugano', 'PROPRIEDADES': {'TEMPO': 5.25, 'DISTANCIA': 254, 'VELOCIDADE_MEDIA': 73, 'CONSUMO_MEDIO': 7.6}},
        {'DESTINO': 'Locarno', 'PROPRIEDADES': {'TEMPO': 4, 'DISTANCIA': 169, 'VELOCIDADE_MEDIA': 68, 'CONSUMO_MEDIO': 6.2}}
    ],
    'Locarno': [
        {'DESTINO': 'Lugano', 'PROPRIEDADES': {'TEMPO': 0.75, 'DISTANCIA': 51, 'VELOCIDADE_MEDIA': 68, 'CONSUMO_MEDIO': 5.3}},
        {'DESTINO': 'Zermatt', 'PROPRIEDADES': {'TEMPO': 4, 'DISTANCIA': 169, 'VELOCIDADE_MEDIA': 68, 'CONSUMO_MEDIO': 6.2}},
        {'DESTINO': 'Ascona', 'PROPRIEDADES': {'TEMPO': 0.5, 'DISTANCIA': 35, 'VELOCIDADE_MEDIA': 70, 'CONSUMO_MEDIO': 4.9}}
    ],
    'Ascona': [
        {'DESTINO': 'Locarno', 'PROPRIEDADES': {'TEMPO': 0.5, 'DISTANCIA': 35, 'VELOCIDADE_MEDIA': 70, 'CONSUMO_MEDIO': 4.9}}
    ]
}

#########################################-------------------#################################

def dijkstra(grafos, inicio, criterio):
    # Inicialização
    distancias = {cidade: float('inf') for cidade in grafos}
    distancias[inicio] = 0
    visitados = set()
    predecessores = {}
    
    while len(visitados) < len(grafos):
        # Encontrar o vértice não visitado com a menor distância atual
        cidade_atual = None
        menor_distancia = float('inf')
        for cidade, distancia in distancias.items():
            if cidade not in visitados and distancia < menor_distancia:
                cidade_atual = cidade
                menor_distancia = distancia
        
        # Verificar se já encontrou o caminho mais curto até a cidade atual
        if cidade_atual is None:
            break
        
        visitados.add(cidade_atual)
        
        # Percorrer as conexões da cidade atual
        for conexao in grafos[cidade_atual]:
            cidade_destino = conexao['DESTINO']
            propriedades = conexao['PROPRIEDADES']
            
            # Obter o valor do critério para a conexão atual
            criterio_valor = propriedades[criterio]
            
            # Calcular a nova distância até a cidade destino
            nova_distancia = distancias[cidade_atual] + criterio_valor
            
            # Atualizar a distância e o predecessor se for menor do que a distância atual
            if nova_distancia < distancias[cidade_destino]:
                distancias[cidade_destino] = nova_distancia
                predecessores[cidade_destino] = cidade_atual
    
    return distancias, predecessores

# Função para exibir a interface e obter o critério do usuário
def obter_criterio():
    print(art)
    print("Escolha o critério:")
    print("1. Distância")
    print("2. Tempo")
    print("3. Velocidade Média")
    print("4. Consumo Médio")
    
    opcoes = {
        '1': 'DISTANCIA',
        '2': 'TEMPO',
        '3': 'VELOCIDADE_MEDIA',
        '4': 'CONSUMO_MEDIO'
    }
    
    while True:
        escolha = input("Digite o número correspondente ao critério desejado: ")
        if escolha in opcoes:
            return opcoes[escolha]
        else:
            print("Opção inválida. Digite novamente.")

# Função para exibir a interface e obter o ponto de partida do usuário
def obter_ponto_partida(grafos):
    print("Escolha o ponto de partida:")
    cidades = list(grafos.keys())
    
    for i, cidade in enumerate(cidades):
        print(f"{i+1}. {cidade}")
    
    while True:
        escolha = input("Digite o número correspondente ao ponto de partida desejado: ")
        if escolha.isdigit() and int(escolha) in range(1, len(cidades)+1):
            indice = int(escolha) - 1
            return cidades[indice]
        else:
            print("Opção inválida. Digite novamente.")

# Função para exibir a interface e obter o ponto de chegada do usuário
def obter_ponto_chegada(grafos):
    print("Escolha o ponto de chegada:")
    cidades = list(grafos.keys())
    
    for i, cidade in enumerate(cidades):
        print(f"{i+1}. {cidade}")
    
    while True:
        escolha = input("Digite o número correspondente ao ponto de chegada desejado: ")
        if escolha.isdigit() and int(escolha) in range(1, len(cidades)+1):
            indice = int(escolha) - 1
            return cidades[indice]
        else:
            print("Opção inválida. Digite novamente.")

# Obtendo o critério, o ponto de partida e o ponto de chegada do usuário
criterio = obter_criterio()
ponto_partida = obter_ponto_partida(grafo)
ponto_chegada = obter_ponto_chegada(grafo)

# Executando o algoritmo de Dijkstra
distancias, predecessores = dijkstra(grafo, ponto_partida, criterio)

# Verificando se foi encontrada uma rota mínima para o ponto de chegada
if ponto_chegada in predecessores:
    # Reconstruindo e exibindo a rota mínima para o ponto de chegada
    rota_minima = [ponto_chegada]
    cidade_atual = ponto_chegada
    while cidade_atual != ponto_partida:
        cidade_atual = predecessores[cidade_atual]
        rota_minima.insert(0, cidade_atual)
    
    print(f"Rota mínima de {ponto_partida} até {ponto_chegada}:")
    print(" -> ".join(rota_minima))
else:
    print(f"Não foi encontrada uma rota mínima de {ponto_partida} até {ponto_chegada}.")
