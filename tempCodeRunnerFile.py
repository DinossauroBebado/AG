populacao.geracao = 0
    grafico_geração.append(populacao.geracao)
    populacao.fitness(distancias)
    grafico_distance.append(populacao.populacao[0].distancia)
    
    # repeat for all generations
    for geração in range(1, n_geraçoes):

        populacao.geracao = geração
        grafico_geração.append(populacao.geracao)
        populacao.fitness(distancias)

        populacao.populacao.sort()
        grafico_distance.append(populacao.populacao[0].distancia)
        next_generation = select_parents(populacao)
        populacao.populacao = next_generation
        populacao.mutate(prop_mut, n_individuo)