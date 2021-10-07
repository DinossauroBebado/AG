class Individuo:
    def __init__(self, genes) -> None:
        self.genes = genes
        self.distancia = 0

    def __repr__(self) -> str:
        return f"\nGenes :{self.genes}, Fit: {self.distancia}"

    def calc_dist(self, distancia) -> int:
        # reseta para não haver interferencia entre gerações
        self.distancia = 0
        for i, gene in enumerate(self.genes[:-1]):
            self.distancia += distancia[gene][i+1]


class Populacao:
    def __init__(self, populacao) -> None:
        self.populacao = populacao
        self.parent = None
        self.geracao = 0

    def __repr__(self) -> str:
        return f"Geração :{self.geracao}\nPopulação: {self.populacao}"

    def fitness(self, distancia):
        """
            Função para verificar quão bom é o indivio em relação a solução ótima
            somando as distancias entre as cidades 
            busca distancia = 0

        """
        for indivio in self.populacao:
            indivio.calc_dist(distancia)

        print(self)
