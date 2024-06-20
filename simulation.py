
import numpy as np
import random
import math

class Agent:
    def __init__(self, ID, agent_type=0):
        self.ID = ID
        self.type = agent_type

class Game:
    def __init__(self, game_type, a, b, c, d):
        self.game_type = game_type
        self.mat = self._init_payoff_matrix(a, b, c, d)

    def _init_payoff_matrix(self, a, b, c, d):
        mat = [[0, 0], [0, 0]]
        if self.game_type == 0:
            mat[0][0] = b - c
            mat[0][1] = -c
            mat[1][0] = b
        elif self.game_type == 1:
            mat[0][0] = b - c / 2
            mat[0][1] = b - c
            mat[1][0] = b
        elif self.game_type == 2:
            mat[0][0] = a
            mat[1][1] = d
        return mat

    def getpi(self, agent_type, x):
        if agent_type:
            return x * self.mat[1][0] + (1 - x) * self.mat[1][1]
        else:
            return x * self.mat[0][0] + (1 - x) * self.mat[0][1]

class Simulation:
    def __init__(self, gamma, game_type, a, b, c, d, time_steps, s, N, n, init_x):
        self.gamma = gamma
        self.game_type = game_type
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.s = s
        self.t = time_steps
        self.N = N
        self.n = n
        self.init_x = init_x
        self.population = self._init_population()
        self.game = Game(self.game_type, self.a, self.b, self.c, self.d)
        self.freq = []
        self.dist = []

    def _init_population(self):
        population = [Agent(ID=i) for i in range(self.N)]
        init_y_num = round(self.N * (1 - self.init_x))
        init_y_pop = np.random.choice(population, init_y_num, replace=False)
        for agent in init_y_pop:
            agent.type = 1
        return population

    def run(self):
        for _ in range(self.t):
            current_freq = 1 - np.mean([agent.type for agent in self.population])
            candidate = random.choice(self.population)
            if self._evolution(candidate):
                candidate.type = 1 - candidate.type
            self.freq.append(current_freq)

    def _evolution(self, candidate):
        neighbors_ID = random.sample(range(self.N), self.n)
        xi = np.mean([self.population[i].type == 0 for i in neighbors_ID])
        M = np.random.power(self.gamma)

        if candidate.type == 0 and M < 1 - xi:
            return np.random.uniform() < 1 / (1 + math.exp(self.s * (self.game.getpi(0, xi) - self.game.getpi(1, xi))))
        elif candidate.type == 1 and M < xi:
            return np.random.uniform() < 1 / (1 + math.exp(-self.s * (self.game.getpi(0, xi) - self.game.getpi(1, xi))))
        return False
