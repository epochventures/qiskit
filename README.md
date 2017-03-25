## Introduction

Batch runner of QASM from https://github.com/IBM/qiskit-api-py, which allows experiments to be run and results plotted and stored. The aim is to take .inc files and run each one, then plot the results, so a hands off process compared to running from the command line or Jupyter. This is having some fun with the amazing python API that IBM have provided to their quantum computer.

## Running code

* python qm.py run

calling run will run your experiments, one by one and will also save to .json file in the /data folder. You can see the results if you need to, since it's just JSON format.

* python qm.py plot

will plot the last stored results. Useful if you don't want to keep running experiments/simulations all the time.

* python qm.py 

will run and then plot.
 
## Set-up

Place .inc files in the qinc folder. These are the files you want to run. Each experiment should be a separate file. All files will be executed. Your credentials and details are found in config.py. Here you are decide the number of shots and whether you want to run as simulation or on a device. Please see the API documentation. Plus here you will also need to include your token which can be found from your control panel. 

## Installation

Project needs you to install the qiskit from IBM which can be found at https://github.com/IBM/qiskit-api-py
You obviously need python and also matplotlib, which usually can be installed with pip install matplotlib or comes with conda for example.
	
## Contributors

Brett Donovan 2017

## License

MIT
