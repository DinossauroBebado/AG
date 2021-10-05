from keys import API

import requests

centros_vacina = {
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


def fit():
    # base url
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&"

    # get response
    r = requests.get(url + "origins=" + endereco[0] +
                     "&destinations=" + endereco[1] + "&key=" + API)

    # return time as text and as seconds
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]

    # print the travel time
    print("\nThe total travel time from home to work is", time)
