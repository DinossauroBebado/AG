import random


class Individuo:
    def __init__(self, genes) -> None:
        self.genes = genes
        self.distancia = 0

    def __repr__(self) -> str:
        return f"\nGenes :{self.genes}, Fit: {self.distancia}"

    def __lt__(self, other):
        return self.distancia < other.distancia

    def sum_dist(self, distancia) -> int:
        "Soma as distancia entre as cidades"
        # reseta para não haver interferencia entre gerações
        self.distancia = 0
        for i, gene in enumerate(self.genes[:-1]):
            self.distancia += distancia[gene][i+1]

    def mutacao(self, prop_mut, n_individuo):
        if random.random() < prop_mut:
            # print("MUTATE")
            mutacao1 = random.randint(1, n_individuo-3)
            mutacao2 = random.randint(1, n_individuo-3)
            hold = self.genes[mutacao1]
            self.genes[mutacao1] = self.genes[mutacao2]
            self.genes[mutacao2] = hold


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
            indivio.sum_dist(distancia)

    def mutate(self, prop_mut, n_individuo):
        """
            passa por toda a população e fez um check de possibilidade
            modifica dois genes aleatorios
            coloca eles na população

        """
        for individos in self.populacao:
            individos.mutacao(prop_mut, n_individuo)
