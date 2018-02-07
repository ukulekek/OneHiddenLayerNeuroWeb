import math
import random


def mse(out_list, ideal_list):
    if len(out_list) != len(ideal_list):
        print('MSE ERROR: out_list != ideal_list')
    n = len(out_list)
    sum = 0
    for i in range(n):
        sum += (out_list[i] - ideal_list[i])**2
    result = sum / n
    return result

def f_sigmoid(out):
    return (1-out)*out



class Neuron:
    def __init__(self, n_type):
        self.type = n_type
        self.input = 0
        self.output = 0
        self.syn_list_in = []
        self.syn_list_out = []
        self.delta = 0

    def comp_input(self):
        sum = 0
        for syn in self.syn_list_in:
            #print(syn.weight, syn.n_in.output)
            sum += syn.weight * syn.n_in.output
            #print('sum = ', sum, syn.weight, syn.n_in.output)
        self.input = sum

    def act(self):
        self.output = 1/(1+ math.exp(-(self.input)))

    def delta(self, out_ideal = None):
        if self.type == 'h':
            self.delta_hidden()
            return
        elif self.type == 'i':
            self.delta_out()
            return
        else:
            print("Delta neuron_type Error")
            sys.exit(1)

    def delta_out(self, out_ideal):
        self.delta = (out_ideal - self.output) * f_sigmoid(self.output)

    def delta_hidden(self):
        sum = 0
        for syn in self.syn_list_out:
            sum += syn.weight * syn.n_out.delta
        self.delta = f_sigmoid(self.output) * sum



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


def create_neuronet():
    input_n = input("Number of neurons in input layer = ")
    input_layer = []
    for i in range(int(input_n)):
        n = Neuron('i')
        input_layer.append(n)

    hidden_n = input("Number of neurons in hidden layer = ")
    hidden_layer = []
    for i in range(int(hidden_n)):
        n = Neuron('h')
        hidden_layer.append(n)


    output_n = input("Number of neurons in output layer = ")
    output_layer = []
    for i in range(int(output_n)):
        n = Neuron('o')
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

def computing(neuronet,input_list):
    output_list = []
    if len(input_list) != len(neuronet[0]):
        print("Computing error: len(input_list) != len(neuronet[0])")
        sys.exit(1)
    for layer in range(3):
        for i in range(len(neuronet[layer])):
            if layer == 0:
                neuronet[0][i].output = input_list[i]
            else:
                neuron = neuronet[layer][i]
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
                neuronet[2][i].delta_out(out_ideal_list[i])


            for h_neuron in neuronet[1]:
                h_neuron.delta_hidden()

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



neuronet = create_neuronet()
filename = input("Write the filename of the dataset.\nDataset format:\niiii;oooo\niiii;oooo\n :")
training_set_list = create_training_data(filename)
print(training_set_list)
e = input('Speed of training(0-1) = ')
a = input('Momentum(0-1) = ')
loop = input("Era iteration = ")
point = input('Era information view:')
point = point.split(" ")
for i in range(len(point)):
    point[i] = int(point[i])
neuronet = training(neuronet, training_set_list,float(e),float(a),int(loop),point,)
