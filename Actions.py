from Neuron import *
from Synapsis import *
from NeuroMath import mse

def computing(neuronet,input_list):
    output_list = []
    for layer in range(3):
        for i in range(len(neuronet[layer])):
            if layer == 0:
                if neuronet[0][i].type != 'b':
                    neuronet[0][i].output = input_list[i]
            else:
                neuron = neuronet[layer][i]
                if neuron.type != 'b':
                    neuron.comp_input()
                    neuron.act()
                    if layer == 2:
                        output_list.append(neuron.output)
    return output_list


def training(neuronet, training_set_list,E ,A ,itera,point):
    for loop in range(itera):
        printing = False
        if loop in point: printing = True
        if printing == True: print("iter, input_list; out_ideal, out_list, err")
        for training_set in training_set_list:
            input_list = training_set[0]
            out_ideal_list = training_set[1]
            result_list = computing(neuronet, input_list)
            err = mse(result_list, out_ideal_list)

            if printing == True: print(itera,input_list, out_ideal_list, result_list, err)
            for i in range(len(neuronet[2])):
                neuronet[2][i].compute_delta(out_ideal_list[i])


            for h_neuron in neuronet[1]:
                if h_neuron.type != 'b':
                    h_neuron.compute_delta()

            for h_neuron in neuronet[1]:
                for syn in h_neuron.syn_list_out:
                    syn.gradient()

            for i_neuron in neuronet[0]:
                for syn in i_neuron.syn_list_out:
                    syn.gradient()
                for syn in i_neuron.syn_list_out:
                    syn.change_weight(E,A)

            for h_neuron in neuronet[1]:
                for syn in h_neuron.syn_list_out:
                    syn.change_weight(E,A)

            if printing == True: print()
        if printing == True: print('----')
    return neuronet


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
