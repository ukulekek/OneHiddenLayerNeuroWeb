import pickle
import NeuroNet

def save_current_neuronet(neuronet):
	try:
		pickle.dump(neuronet, open("neuronet.p",'wb'))
		return 0
	except:
		return 1

def load_neuronet():
	try:
		neuronet = pickle.load(open("neuronet.p",'rb'))
		return neuronet
	except:
		return None
