from IBMQuantumExperience import IBMQuantumExperience
import matplotlib.pyplot as plt
import os, json, datetime, sys
import numpy as np
from config import *


"""qm.py: Simple batch runner to run qinc files using IBM QASM API"""

__author__      = "Brett Donovan"
__copyright__   = "Copyright 2016"
__license__ = "MIT"
__version__ = "1.0.1"
__maintainer__ = "Brett Donovan"
__email__ = "brettdonovan@gmail.com"
__status__ = "Production"


def compute():
	api = IBMQuantumExperience(TOKEN, CONFIG_URL)
	file_list = [z[2] for z in os.walk(PATH)][0]
	qasms = []
	completed_experiments = []
	for EXPERIMENT in file_list:
		with open(os.path.join(PATH, EXPERIMENT), 'r') as fopen:
			qasm = fopen.read()
			qasms.append(qasm)
			print "Running " +EXPERIMENT+ "..."
			runit = api.run_experiment(qasm, DEVICE, SHOTS, EXPERIMENT, TIMEOUT)
			runit['fullname'] = os.path.join(PATH, EXPERIMENT)
			runit['name'] = EXPERIMENT
			completed_experiments.append(runit)
	exp_json = json.dumps(completed_experiments)
	with open(os.path.join(DATA_PATH, DATA_FILENAME), 'w') as fopen:
		fopen.write(exp_json)
	
def plot():
	with open(os.path.join(DATA_PATH, DATA_FILENAME), 'r') as fopen:
		qasms = json.loads(fopen.read())
		for experiment in qasms:
			try:
				title = experiment['name']
				plt.title(title)
				labels = experiment["result"]["measure"]["labels"]
				values = experiment["result"]["measure"]["values"]
				width = 0.85
				ind = np.arange(len(values))
				plt.xticks(ind + width / 2, labels)       
				_op = plt.bar(ind, values, width, color='r')
				plt.grid(True)		
				plt.xlabel("qubits")
				plt.xticks(rotation=90)
				plt.savefig(os.path.join(RESULTS_PATH, title.split('.')[0]+'.png'), bbox_inches='tight', pad_inches=0.5)
				plt.close()
			except Exception as e:
				print e

if __name__ == "__main__":	
	if len(sys.argv) > 1:
		if sys.argv[1] == "run":
			compute()
		elif sys.argv[1] == "plot":
			plot()
	else: # do everything
		compute()
		plot()	

	
	
