import pandas as pd
import requests
import random
from random import sample

def get_distance(origem,destino):
    # key bing maps api
    bingMapsKey = "AsNvItM2ty9tkDhoC-J69ttib9XJkpXN5iWUEcSM874piuq2gEeaqJS7E0r0BU5S"

    #abrir request ao servidor
    route = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + origem + "&wp.1=" + destino + "/&key=" + bingMapsKey

    print(route)

    # coletar distancia (em KM) e tempo (em Minutos)
    r = requests.get(url = route)
    result = r.json()
    distance = result["resourceSets"][0]["resources"][0]["travelDistance"]
    #print(distance)
    return distance

def make_matrix(endereco):
    distancias = []
    for origem in endereco:
        dist = []
        for destino in endereco:
            dist.append(get_distance(origem, destino))
        distancias.append(dist)
    print(distancias)

#retorna o tamanho do percurso
def fit(distancias,m,n,visitados):
    visitados.append(m)
    sum = 0
    for x in n:
        sum += distancias[m][x]
        visitados.append(x)
        m=x

    sum += distancias[m][0] #retornando para o incio
    visitados.append(0)
    return sum



def main():
    visitados = []
    centros_vacina = {
        "CEMEPAR, Estacionamento": " Avenida Prefeito Lothário Meissner - Jardim Botânico",
        
        "PAVILHÃO DE EVENTOS DO PARQUE BARIGUI": "Alameda Ecológica Burle Marx2518 – Santo Inácio",

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
    #make_matrix(endereco)

    distancias = [[0, 10.41, 11.413, 9.057, 9.84, 7.427, 10.047, 5.02, 12.817, 15.772, 20.294],
                  [10.364, 0, 9.416, 4.098, 6.538, 10.531,
                   15.427, 12.598, 14.915, 27.946, 25.386],

                  [12.163, 11.835, 0, 7.355, 15.988, 16.604,
                   18.246, 15.055, 25.383, 38.414, 35.854],
                  [10.518, 5.045, 8.722, 0, 9.081, 10.092,
                   15.581, 12.752, 17.104, 18.718, 27.575],
                  [9.906, 6.8, 15.362, 9.359, 0, 7.108,
                   13.979, 12.14, 4.096, 12.752, 17.135],
                  [8.081, 10.079, 18.939, 11.311, 6.926, 0,
                   7.666, 9.65, 7.513, 10.176, 14.698],
                  [9.35, 16.36, 17.905, 15.007, 13.875,
                   7.933, 0, 7.432, 22.229, 8.339, 18.293],
                  [4.778, 13.969, 14.972, 12.616, 13.399,
                   10.986, 7.554, 0, 16.376, 19.331, 23.853],
                  [15.063, 15.747, 25.004, 18.955, 4.154,
                   7.777, 14.648, 16.632, 0, 15.882, 13.322],
                  [15.939, 27.021, 36.278, 18.166, 13.781,
                   10.116, 8.965, 17.508, 13.807, 0, 9.871],
                  [20.339, 26.424, 35.681, 29.632, 18.83, 14.516, 17.685, 21.908, 13.21, 10.726, 0]]

    testes=0
    aux  = 101.444 #filtrar melhores resultados
    while(testes<=100000): #Número de execuções
        m= 0 #ponto de inicio
        n = random.sample(range(1,11), 10)
        print("Rota = " , n)
        save = fit(distancias,m,n,visitados)
        print("Distância total = ", save)
        print("Percurso = ",visitados)
        testes +=1
        visitados.clear() #limpa os pontos visitados para uma nova execução do loop
        if (aux > save): #filtra as melhor distãncias obtidas do total de execuções
            aux = save

    print("menor distancia = ",aux)

if __name__ == "__main__":
        main()
