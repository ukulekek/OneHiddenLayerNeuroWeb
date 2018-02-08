from NeuroMath import f_sigmoid
import math

class Neuron:
    def __init__(self, n_type):
        self.type = n_type
        self.output = 0
        self.syn_list_out = []

    def comp_input(self):
        sum = 0
        for syn in self.syn_list_in:
            #print(syn.weight, syn.n_in.output)
            sum += syn.weight * syn.n_in.output
            #print('sum = ', sum, syn.weight, syn.n_in.output)
        self.input = sum

    def act(self):
        self.output = 1/(1+ math.exp(-(self.input)))


class InputNeuron(Neuron):
    def __init__(self, n_type):
        Neuron.__init__(self,n_type)
        self.syn_list_out = []


class HiddenNeuron(Neuron):
    def __init__(self, n_type):
        Neuron.__init__(self,n_type)
        self.syn_list_in = []
        self.syn_list_in = []
        self.input = 0

    def compute_delta(self):
        sum = 0
        for syn in self.syn_list_out:
            sum += syn.weight * syn.n_out.delta
        self.delta = f_sigmoid(self.output) * sum


class OutputNeuron(Neuron):
    def __init__(self, n_type):
        Neuron.__init__(self,n_type)
        self.syn_list_in = []
        self.input = 0

    def compute_delta(self, out_ideal):
        self.delta = (out_ideal - self.output) * f_sigmoid(self.output)


class BiasNeuron(Neuron):
    def __init__(self, n_type):
        Neuron.__init__(self,n_type)
        self.output = 1
        self.syn_list_out = []
