import random
from Neuronet import *
from Actions import *






neuronet = create_neuronet()
neuronet = create_bias_layer(neuronet)
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
