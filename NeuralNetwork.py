import random
import pygame
import numpy as np
import pandas as pd

class Color:
    white = (255, 255, 255)
    black = (0, 0, 0)
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)

class Node:

    def __init__(self, layer):
        self.inputs = []
        self.inputWeights = []
        self.outputs = []
        self.outputWeights = []

        self.layer = layer

    def connectToNextLayer(self, layerNodes):
        for node in layerNodes:
            weight = random.random()
            self.outputs.append(node)
            self.outputWeights.append(weight)
            node.inputs.append(self)
            node.inputWeights.append(weight)

    def disconnectNextLayer(self):
        for node in self.outputs:
            index = node.inputs.index(self)
            node.inputs.pop(index)
            node.inputWeights.pop(index)

        self.outputs = []
        self.outputWeights = []

    def value(self):
        value = 0
        for i, node in enumerate(self.inputs):
            value += node.value() * self.inputWeights[i]

        return 1 if value > 0 else -1 if value < 0 else 0

    def getAllInputs(self):         #returns all input nodes i.e. the previous layer
        result = []
        for k, v in self.inputs:
            result.append(k)
        return result

    def getAllOutputs(self):        #returns all output nodes i.e. the next layer
        result = []
        for k, v in self.outputs:
            result.append(k)
        return result

    def draw(self, screen, font, x, y):
        pygame.draw.circle(screen, Color.black, (x, y), 75)
        screen.blit(font.render(str(hex(id(self))), False, Color.green), (x - 25, y - 50))
        for i, node in enumerate(self.inputs):
            textsurface = font.render(hex(id(node)), False, Color.blue)
            screen.blit(textsurface, (x - 100, y - 30 + 20 * i))
        for i, node in enumerate(self.outputs):
            screen.blit(font.render(str(hex(id(node)) + " - " + str(self.outputWeights[i])[0:4]), False, Color.red), (x + 20, y - 30 + 20 * i))
        screen.blit(font.render(str(self.value()), False, Color.white), (x - 20, y - 70))

class InputNode(Node):
    def __init__(self):
        super().__init__(0)

    def value(self):
        return self.inputs[0]


class NeuralNetwork:
    inputs = []  # list of Inputnodes
    outputs = []  # list of Outputnodes
    hiddenLayers = []  # list of hiddenlayer nodes
    cHiddenLayers = 0  # count of hidden layers

    def __init__(self, cInputs, cOutputs):
        for i in range(cInputs):
            self.inputs.append(InputNode())

        for i in range(cOutputs):
            self.outputs.append(Node(-1))

        self.connectLayers(self.inputs, self.outputs)

    def setInputs(self, inputValues):
        for i, value in enumerate(inputValues):
            if(len(self.inputs[i].inputs) == 0):
                self.inputs[i].inputs.append(value)
            else:
                self.inputs[i].inputs[0] = value

    def calcOutputs(self):
        outputValues = []
        for node in self.outputs:
            outputValues.append(node.value())
        return outputValues

    def getLayer(self, layerIndex):
        if layerIndex > self.cHiddenLayers:
            return []
        elif self.cHiddenLayers == 1 and layerIndex == 1:
            return self.hiddenLayers
        else:
            result = []
            for node in self.hiddenLayers:
                if node.layer == layerIndex:
                    result.append(node)
            return result

    def connectLayers(self, layer1Nodes, layer2Nodes):
        for node in layer1Nodes:
            node.connectToNextLayer(layer2Nodes)

    def disconnectNextLayer(self, layerIndex1):
        layer1 = self.getLayer(layerIndex1)
        for node in layer1:
            node.disconnectNextLayer()

    def disconnectInput(self):
        for node in self.inputs:
            node.disconnectNextLayer()

    def addLayerNumber(self, cNodes):
        newLayer = []
        for i in range(cNodes):
            newLayer.append(Node(self.cHiddenLayers + 1))
        self.addLayer(layerNodes=newLayer)

    def addLayer(self, layerNodes):
        if self.cHiddenLayers == 0:
            self.disconnectInput()
            self.connectLayers(self.inputs, layerNodes)
        else:
            self.disconnectNextLayer(self.cHiddenLayers)
            self.connectLayers(self.getLayer(self.cHiddenLayers), layerNodes)
        for node in layerNodes:
            self.hiddenLayers.append(node)
        self.cHiddenLayers += 1
        self.connectLayers(layerNodes, self.outputs)

    def draw(self):
        width = 1200
        height = 800
        black = (0, 0, 0)
        white = (255, 255, 255)
        red = (255, 0, 0)
        green = (0, 255, 0)
        pygame.font.init()
        myfont = pygame.font.SysFont('Cosmic Sans MS', 20)

        pygame.init()
        screen = pygame.display.set_mode((width, height))
        screen.fill(white)

        cInputs = len(self.inputs)
        distance = height / cInputs
        for i, node in enumerate(self.inputs):
            node.draw(screen, myfont, 75, int(distance / 2 + distance * i))

        spaceForHidden = width - 300
        if self.cHiddenLayers == 0:
            spaceForOneHidden = spaceForHidden
        else:
            spaceForOneHidden = spaceForHidden / self.cHiddenLayers
        middleStartPoint = int(spaceForOneHidden / 2) + 150
        for layerIndex in range(self.cHiddenLayers):
            layerIndex += 1
            hiddenLayer = self.getLayer(layerIndex)
            distance = height / len(hiddenLayer)
            for i, node in enumerate(hiddenLayer):
                node.draw(screen, myfont, middleStartPoint + int(spaceForOneHidden) * (layerIndex - 1), int(distance/2 + distance * i))

        distance = height / len(self.outputs)
        for i, node in enumerate(self.outputs):
            node.draw(screen, myfont, width - 75, int(distance / 2 + distance * i))

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    break
                pygame.display.update()

var = NeuralNetwork(4, 2)
#var.addLayerNumber(3)
#var.addLayerNumber(4)
#var.addLayerNumber(5)
var.setInputs([1, 2, 3, 4])
print(var.calcOutputs())
#var.draw()
while True:
    newlist = input("New Inputs: ").split()
    for i, value in enumerate(newlist):
        newlist[i] = int(value)
    var.setInputs(newlist)
    print(var.calcOutputs())
    var.draw()

class fitness:

    def read_out_coords(self, pipe_input, posish):
        pipe_coords = []
        birdx, birdy = posish
        for i, coords in enumerate(pipe_input):
            xtop, ytop, xbot, ybot = coords.get_coordinates()
            pipe_coords.append([xtop - birdx, ytop - birdy + 820, ybot - birdy])
        pipe_coords = np.array(pipe_coords)

        return pipe_coords

    def first_weights_hid():
        layw1 = np.random.randint(low=-500, high=500, size=[9], dtype="int64")
        layw2 = np.random.randint(low=-500, high=500, size=[9], dtype="int64")
        layw3 = np.random.randint(low=-500, high=500, size=[9], dtype="int64")

        return [layw1, layw2, layw3]

    def first_weights_out():
        return out_layw = np.random.randint(low=-500, high=500, size=[3], dtype="int64")

    def calc_lay(self, vals, weights):
        hidden_layer_vals = []
        for i in weights:
            hidden_layer_vals.append(np.dot(vals, i))

        return hidden_layer_vals

    def adjust_weights(self, weights, gen):
        high_val = 100/gen
        low_val = -100/gen
        new_weights = (np.random.randint(high=high_val,low=low_val, size=np.shape(weights))/100)*weights

        return new_weights








