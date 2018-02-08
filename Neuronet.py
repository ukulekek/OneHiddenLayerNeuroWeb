from Neuron import *
from Synapsis import *

def create_neuronet():
    input_n = input("Number of neurons in input layer = ")
    input_layer = []
    for i in range(int(input_n)):
        n = InputNeuron('i')
        input_layer.append(n)

    hidden_n = input("Number of neurons in hidden layer = ")
    hidden_layer = []
    for i in range(int(hidden_n)):
        n = HiddenNeuron('h')
        hidden_layer.append(n)


    output_n = input("Number of neurons in output layer = ")
    output_layer = []
    for i in range(int(output_n)):
        n = OutputNeuron('o')
        output_layer.append(n)

    for i in input_layer:
        for h in hidden_layer:
            s = Synapsis(i,h)
            i.syn_list_out.append(s)
            h.syn_list_in.append(s)
    for h in hidden_layer:
        for o in output_layer:
            s = Synapsis(h,o)
            h.syn_list_out.append(s)
            o.syn_list_in.append(s)

    layers = [input_layer,hidden_layer, output_layer]
    return layers

def create_bias_layer(neuronet):
    for i in range(2):
        b = BiasNeuron('b')
        for neuron in neuronet[i+1]:
            syn = Synapsis(b,neuron)
            b.syn_list_out.append(syn)
            neuron.syn_list_in.append(syn)
        neuronet[i].append(b)
    return neuronet
