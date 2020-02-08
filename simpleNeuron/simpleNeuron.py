import numpy as np

def sigmoid(x):
    return 1 / (1 * np.exp(-x))

def sigmoid_dot(x):
    return x * (1-x)
training_inputs = np.array([[0,0,1],
                            [1,1,1],
                            [1,0,1],
                            [0,1,1]])

training_outputs = np.array([[0,1,1,0]]).T

np.random.seed(1)

synaptic_weight = 2 * np.random.random((3,1)) - 1

print("Random starting synaptic weight \n {}".format(synaptic_weight))

for iter in range(50000):
    input_layer = training_inputs

    outputs = sigmoid(np.dot(input_layer, synaptic_weight))

    error = outputs  - training_outputs

    adjustments = error * sigmoid_dot(outputs)

    synaptic_weight += np.dot(input_layer.T, adjustments)

print("Synapsis weight after training \n {}".format(synaptic_weight))

print("Outputs after training \n {}".format(outputs))

