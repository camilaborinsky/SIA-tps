class AlgorithmBreak:
    def checkBreak(self, config):
        return True


class GenerationCountBreak(AlgorithmBreak):
    def checkBreak(self, population, population_count):
        return 