import random
import numpy as np
from NeuralNetwork import *

class Player:

    def __init__(self, bird):
        self.bird = bird
        self.nn = NeuralNetwork(6, 1)
        self.nn.addLayerNumber(5)
        self.nn.addLayerNumber(6)
        self.fit = fitness()
        self.initial_weights_hidden = self.fit.first_weights_hid()
        self.initial_weights_out = self.fit.first_weights_out()
        #self.nn.addLayer(5)


    def do_i_jump(self, i, pipes):
        lowprio_first_item = False #true if the first pipe is behind the bird already which means it is less worth than the next one
        p_x, p_y = i.get_coordinates()

        x_dists = []
        for pipe in pipes:
            topx, topy, botx, boty = pipe.get_coordinates()
            x_dists.append(topx - p_x)

        sorted_indexes = np.argsort(x_dists)
        lowprio_first_item = (x_dists[sorted_indexes[0]] <= -100)  # -100 is the threshhold where the bird leaves the pipe

        if lowprio_first_item:
            sorted_indexes = [sorted_indexes[(j + 1) % 3] for j, something in enumerate(sorted_indexes)] #shit array

        sorted = [x_dists[j] for j in sorted_indexes]

        distances = []
        for j in sorted_indexes:
            topx, topy, botx, boty = pipes[j].get_coordinates()
            distances.append(np.sqrt((topx - p_x)**2 + (topy - p_y)**2))
            distances.append(np.sqrt((botx - p_x)**2 + (boty - p_y)**2))

        self.nn.setInputs(distances)
        #print(self.nn.calcOutputs())