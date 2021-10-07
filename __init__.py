import pandas as pd
import requests
from keys import bingMapsKey
import random


centros_vacina = {
    "CEMEPAR, Estacionamento ": " Avenida Prefeito Lothário Meissner - Jardim Botânico",

    "PAVILHÃO DE EVENTOS DO PARQUE BARIGUI": "Alameda Ecológica Burle Marx ,2518 – Santo Inácio",

    "US VILA DIANA": "Rua René Descartes, 537 – Abranches Boa Vista",

    "US BOM PASTOR ": "Rua José Casagrande, 220 – Vista Alegre",

    "US SANTA QUITÉRIA I": "Rua Divina Providência, 1445 – Santa Quitéria",

    "US FANNY-LINDOIA": "Rua Condes dos Arcos, 295 – Lindoia ",

    "US WALDEMAR MONASTIER": "Rua Romeu Bach, 80 – Boqueirão ",

    "US CAJURU": "Rua Pedro Bochino, 750 – Vila Oficinas ",

    "US SÃO MIGUEL": "Rua Des. Cid Campelo, 8060 – Cidade Industrial",

    "US SÃO JOÃO DEL REY": "Rua Realeza, 259 – Sitio Cercado",

    "US MORADIAS SANTA RITA": "Rua Adriana Zago Bueno, 743 – Tatuquara",
}

endereco = list(centros_vacina.values())


def get_distance(origem, destino):
    # key bing maps api

    # abrir request ao servidor
    route = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + \
        origem + "&wp.1=" + destino + "/&key=" + bingMapsKey

    # coletar distancia (em KM) e tempo (em Minutos)
    r = requests.get(url=route)
    result = r.json()
    distance = result["resourceSets"][0]["resources"][0]["travelDistance"]

    return distance


def make_matrix():
    distancias = []
    for origem in endereco:
        dist = []
        for destino in endereco:
            dist.append(get_distance(origem, destino))
        distancias.append(dist)
    print(distancias)


# make_matrix()

distancias = [[0, 10.41, 11.413, 9.057, 9.84, 566.543, 10.047, 5.02, 12.817, 15.772, 20.296],
              [10.364, 0, 9.416, 4.098, 6.538, 571.001,
                  15.427, 12.598, 14.915, 27.946, 25.388],
              [12.163, 11.835, 0, 7.355, 15.988, 565.881,
                  18.246, 15.055, 25.383, 38.414, 35.856],
              [10.518, 5.045, 8.722, 0, 9.081, 570.965,
                  15.581, 12.752, 17.104, 18.718, 27.577],
              [9.906, 6.8, 15.362, 9.359, 0, 573.663,
                  13.979, 12.14, 4.096, 12.752, 17.137],
              [565.989, 573.727, 567.339, 572.374, 575.599, 0,
               577.463, 575.21, 595.606, 586.097, 591.672],
              [9.35, 16.36, 17.905, 15.007, 13.875,
                  575.852, 0, 7.432, 22.229, 8.339, 18.295],
              [4.778, 13.969, 14.972, 12.616, 13.399,
                  567.478, 7.554, 0, 16.376, 19.331, 23.855],
              [15.063, 15.747, 25.004, 18.955, 4.154,
                  593.681, 14.648, 16.632, 0, 15.882, 13.324],
              [15.939, 27.021, 36.278, 18.166, 13.781,
                  583.421, 8.965, 17.508, 13.807, 0, 9.873],
              [20.337, 26.422, 35.679, 29.63, 18.828, 588.538, 17.683, 21.906, 13.208, 10.724, 0]]


def alg_genetico():
    populucao = init_pop()
    # repet for all generations
    fitness(populucao)
    cross_over_genes()
    mutate()

    pass


def init_pop():
    """
    Cria uma população com individuos gerados aleatoriamente cada gene 
    é composto de um lista com os indices dos postos 
    [2,3,6,7,9,5]

    endereco[2] = "Rua René Descartes, 537 – Abranches Boa Vista"

    """
    populacao = []
    for _ in range(n_populacao):  # passa por todos os individuos em um população
        individuo = random.sample(range(1, n_populacao-1), n_populacao-2)
        # começo é fixo
        individuo.append(0)
        # final é fixo
        individuo.insert(0, 0)

        populacao.append(individuo)

    return populacao


def fitness(população, distancia):
    """
        Função para verificar quão bom é o indivio em relação a solução ótima
        somando as distancias entre as cidades 
        busca distancia = 0

    """

    for indivio in população:
        sum_distancia = 0
        for genes in indivio[:-1]:
            sum_distancia += distancias[genes][genes+1]

    pass


def cross_over_genes():
    pass


def mutate():
    pass


n_populacao = 10

n_geraçoes = 1000

n_individuo = len(centros_vacina)

prop_mut = 0.01

print(init_pop())
