from Neuronet import *
from Actions import *


neuronet = Neuronet()
neuronet.create_neuronet(2,3,1)
neuronet.create_bias_layer()

filename = 'data2.txt'

training_set_list = create_training_data(filename)

print(training_set_list)

e = 0.2
a = 0.2

loop = 10000
point = [1,5,10,1000,10000]
neuronet = training(neuronet, training_set_list,e,a,loop,point)
