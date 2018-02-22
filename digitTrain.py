from NeuroNet import *
from Actions import *
from NeuroSave import *
from PIL import Image

#60-71

def bw_image_to_bin(filename):
	im = Image.open(filename)
	width, height = im.size
	bin_str = ''
	for x in range(width):
		for y in range(height):
			r,g,b,a = im.getpixel((x,y))
			gray = (r + g + b)/3
			if gray > 50:
				bin_str += '1'
			else:
				bin_str += '0'
	return bin_str

def image_parse(dirname,filename):
    f = open(filename,'w')
    for i in range(48,58):
        print(chr(i))
        filename = dirname +'/' + chr(i) +'.png'
        bin_str = bw_image_to_bin(filename)
        f.write(bin_str + ';' + chr(i)+'\n')


#dirname = 'data'
#filename = 'digitdata.txt'
#image_parse(dirname,filename)

neuronet = Neuronet()
neuronet.create_neuronet(400,10,4)
neuronet.create_bias_layer()

filename = 'digitdata.txt'

training_set_list = create_training_data(filename)

print(training_set_list)

e = 0.2
a = 0.2

loop = 10000
point = [1,5,10,1000,10000]
neuronet = training(neuronet, training_set_list,e,a,loop,point)

flag = save_current_neuronet(neuronet)

print("Save flag = ",flag)
