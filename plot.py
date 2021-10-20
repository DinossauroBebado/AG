import matplotlib.pyplot as plt
import numpy as np

# Data for plotting


def plot(geracao, distancia):
    fig, ax = plt.subplots()
    ax.plot(geracao, distancia)

    ax.set(xlabel='Execuções', ylabel='Distance(Km)',
           title=' Aperfeiçoamento do algoritmo pelas execuções')
    ax.grid()

    # fig.savefig("DistanceXGeneration")
    plt.show()
