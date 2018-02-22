from Neuron import *
from Synapsis import *


'''
Neuronet() class:
    Class which define neuronet

    create_neuronet(self,input_n,hidden_n,output_n):
        Method for creating neuronet
        Requires:
            input_n = amount of input neurons
            hidden_n = amount of hidden neurons
            output_n = amount of output neurons

    create_bias_layer(self):
        Method for creating bias neurons in input and hidden layer
'''
class Neuronet():
    def __init__(self):
        self.input_neurons_list = []
        self.hidden_neurons_list = []
        self.output_neurons_list = []
        self.bias_neurons = False

    def create_neuronet(self,input_n, hidden_n, output_n):
        for _ in range(int(input_n)):
            n = InputNeuron('i')
            self.input_neurons_list.append(n)

        for _ in range(int(hidden_n)):
            n = HiddenNeuron('h')
            self.hidden_neurons_list.append(n)

        for _ in range(int(output_n)):
            n = OutputNeuron('o')
            self.output_neurons_list.append(n)

        for input_neuron in self.input_neurons_list:
            for hidden_neuron in self.hidden_neurons_list:
                s = Synapsis(input_neuron,hidden_neuron)
                input_neuron.syn_list_out.append(s)
                hidden_neuron.syn_list_in.append(s)
                for output_neuron in self.output_neurons_list:
                    s = Synapsis(hidden_neuron,output_neuron)
                    hidden_neuron.syn_list_out.append(s)
                    output_neuron.syn_list_in.append(s)

    def create_bias_layer(self):
        bias_neuron1 = BiasNeuron('b')
        bias_neuron2 = BiasNeuron('b')
        for neuron in self.hidden_neurons_list:
            syn = Synapsis(bias_neuron1,neuron)
            bias_neuron1.syn_list_out.append(syn)
            neuron.syn_list_in.append(syn)
        self.input_neurons_list.append(bias_neuron1)
        for neuron in self.output_neurons_list:
            syn = Synapsis(bias_neuron2, neuron)
            bias_neuron2.syn_list_out.append(syn)
            neuron.syn_list_in.append(syn)
        self.hidden_neurons_list.append(bias_neuron2)
        self.bias_neurons = True
