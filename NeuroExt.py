
from PIL import Image

def bw_image_to_bin(filename):
	im = Image.open(filename
	width, height = im.size
	bin_list = []
	for x in range(width):
		for y in range(height):
			(r,g,b) = im.getpixel((x,y))
			gray = (r + g + b)/3
			if gray > 50:
				bin_list.append(1)
			else:
				bin_list.append(0)
	return bin_list

ef create_training_file			
