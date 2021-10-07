import pandas as pd
import requests


def get_distance(origem, destino):
    # key bing maps api
    bingMapsKey = "AsNvItM2ty9tkDhoC-J69ttib9XJkpXN5iWUEcSM874piuq2gEeaqJS7E0r0BU5S"

    # abrir request ao servidor
    route = "http://dev.virtualearth.net/REST/V1/Routes/Driving?wp.0=" + \
        origem + "&wp.1=" + destino + "/&key=" + bingMapsKey

    print(route)

    # coletar distancia (em KM) e tempo (em Minutos)
    r = requests.get(url=route)
    result = r.json()
    distance = result["resourceSets"][0]["resources"][0]["travelDistance"]
    # print(distance)
    return distance


def make_matrix(endereco):
    distancias = []
    for origem in endereco:
        dist = []
        for destino in endereco:
            dist.append(get_distance(origem, destino))
        distancias.append(dist)
    print(distancias)


def main():
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
    make_matrix(endereco)


if __name__ == "__main__":
    main()
