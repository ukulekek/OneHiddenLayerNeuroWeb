from Neuron import *
from Synapsis import *
from NeuroMath import mse


'''
computing(neuronet, input_list):
    Calculate and return outputs of out neurons.
    Requires:
        neuronet =  object of Neuronet() class
        input_list = list of input values
'''
def computing(neuronet,input_list):
    for i in range(len(neuronet.input_neurons_list)):
        if neuronet.input_neurons_list[i].type != 'b':
            neuronet.input_neurons_list[i].output = input_list[i]
    for layer in [neuronet.hidden_neurons_list, neuronet.output_neurons_list]:
        for i in range(len(layer)):
            neuron = layer[i]
            if neuron.type != 'b':
                neuron.comp_input()
                neuron.act()
    output_list = []
    for neuron in neuronet.output_neurons_list:
            output_list.append(neuron.output)
    return output_list

'''
training(neuronet, training_set_list,E ,A ,iter,point):
    Training and return your neuronet.
    Requires:
        neuronet = object of Neuronet() class
        training_set_list = list of training sets
            Format:[input_list, ideal_output_list]
            Recommended to use create_training_data() function
        E = speed of training
        A = momentum
            For more information, see "gradient descent"
        iter = amount of iterations
        point = list of numbers iterations for which the neuronet state will be displayed

'''
def training(neuronet, training_set_list,E ,A ,iter,point):
    for loop in range(iter+1):
        printing = False
        if loop in point: printing = True
        if printing == True: print("iter, input_list; out_ideal, out_list, err")
        for training_set in training_set_list:
            input_list = training_set[0]
            out_ideal_list = training_set[1]
            result_list = computing(neuronet, input_list)
            err = mse(result_list, out_ideal_list)

            if printing == True: print(loop,input_list, out_ideal_list, result_list, err)
            for i in range(len(neuronet.output_neurons_list)):
                neuronet.output_neurons_list[i].compute_delta(out_ideal_list[i])

            for hidden_neuron in neuronet.hidden_neurons_list:
                if hidden_neuron.type != 'b':
                    hidden_neuron.compute_delta()

            for h_neuron in neuronet.hidden_neurons_list:
                for syn in h_neuron.syn_list_out:
                    syn.gradient()

            for input_neuron in neuronet.input_neurons_list:
                for syn in input_neuron.syn_list_out:
                    syn.gradient()
                for syn in input_neuron.syn_list_out:
                    syn.change_weight(E,A)

            for hidden_neuron in neuronet.hidden_neurons_list:
                for syn in hidden_neuron.syn_list_out:
                    syn.change_weight(E,A)

            if printing == True: print()
        if printing == True: print('----')
    return neuronet

'''
create_training_data(file):
    Create and return list of training sets.
    Requires:
        file = name of file from which dataset will be read
        Format of data in file: iiii;oooo
            i - input for neuron (0/1)
            o - ideal output of output neuron
            For example:
                00;0
                01;1
                10;1
                11;0
'''
def create_training_data(file):
    f = open(file,'r')
    training_set_list = []
    for line in f:
        data = line.split(';')
        data[1] = data[1][:len(data[1])-1]
        input_list = list(data[0])
        output_list = list(data[1])
        for i in range(len(input_list)):
            input_list[i] = int(input_list[i])
        for i in range(len(output_list)):
            output_list[i] = int(output_list[i])
        training_set_list.append([input_list,output_list])
    f.close()
    return training_set_list
