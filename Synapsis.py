import random


'''
Synapsis class
Class which define synapsis between neurons
'''
class Synapsis:
    def __init__(self, n_in, n_out):
        self.weight = random.random() - 0.5
        self.n_out = n_out
        self.n_in = n_in
        self.grad = 0
        self.delta_w = 0

    def gradient(self):
        self.grad = self.n_out.delta * self.n_in.output

    def change_weight(self, E, A):
        self.delta_w = E*self.grad + A*self.delta_w
        self.weight +=self.delta_w
