# Distância entre as cidades
distancia = 100

# Velocidades em km/h
velocidade_carro = 110
velocidade_caminhao = 80

# Tempo que o caminhão leva a mais em cada pedágio (em horas)
tempo_pedagio = 5 / 60

# Tempo para se encontrarem (em horas)
tempo_encontro = distancia / (velocidade_carro + velocidade_caminhao)

# Distância percorrida pelo caminhão quando se encontram
distancia_caminhao = velocidade_caminhao * (tempo_encontro + tempo_pedagio)

# Distância percorrida pelo carro quando se encontram
distancia_carro = distancia - distancia_caminhao

# Tempo que o carro levou para percorrer a distância até o ponto de encontro
tempo_carro = distancia_carro / velocidade_carro

# Tempo que o caminhão levou para percorrer a distância até o ponto de encontro (considerando o tempo nos pedágios)
tempo_caminhao = tempo_encontro + tempo_pedagio - tempo_carro

# Distância do carro até Ribeirão Preto
distancia_carro_rp = distancia_carro + velocidade_carro * tempo_caminhao

# Distância do caminhão até Ribeirão Preto
distancia_caminhao_rp = distancia - distancia_carro_rp

# Verifica qual veículo está mais próximo de Ribeirão Preto
if distancia_carro_rp < distancia_caminhao_rp:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")
