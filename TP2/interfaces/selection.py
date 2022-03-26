class Selection:
    def select(self, population, pop_size):
        return population

class StochasticSelection(Selection):
    def select(self, population, pop_size, prob):
        return population

class EliteSelection(Selection):
    def select(self, population, pop_size):
        population.sort()
        n = len(population) - pop_size
        selected_individuals = population[n:]
        return selected_individuals

class RouletteSelection(StochasticSelection):
    def select(self, population):
        return super().select(population)

class RankSelection(StochasticSelection):
    def select(self, population):
        return super().select(population)

class TournamentSelection(StochasticSelection):
    def select(self, population):
        return super().select(population)

class BoltzmannSelection(StochasticSelection):
    def select(self, population):
        return super().select(population)

class TruncatedSelection(StochasticSelection):
    def select(population):
        return super().select(population)