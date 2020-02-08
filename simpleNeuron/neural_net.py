import numpy as np

class NeuralNetwork():

    def __init__(self):
        np.random.seed(1)

        self.synaptic_weight = 2 * np.random.random((4,1)) - 1

    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    def sigmoidDot(self, x):
        return x * (1 - x)

    def train(self, training_inputs, training_outputs, training_iter):
        for iter in range(training_iter):
            output = self.think(training_inputs)
            error = training_outputs - output
            adjustments = np.dot(training_inputs.T, error * self.sigmoid(output))
            self.synaptic_weight += adjustments

    def think(self, inputs):
        inputs = inputs.astype(float)
        output = self.sigmoid(np.dot(inputs, self.synaptic_weight))
        return output

if __name__ == "__main__":
    neuralNetwork = NeuralNetwork()

    print("Random synaptic weights {}".format(neuralNetwork.synaptic_weight))

    training_inputs = np.array([[0, 0, 1, 0],
                                [1, 1, 1, 1],
                                [1, 0, 1, 1],
                                [0, 1, 0, 1],
                                [0, 0, 0, 0],])

    training_outputs = np.array([[0, 1, 1, 1, 0]]).T

    neuralNetwork.train(training_inputs, training_outputs, 30000)

    print("Synaptic weights after training {}".format(neuralNetwork.synaptic_weight))

    A = str(input("Input 1\n"))
    B = str(input("Input 2\n"))
    C = str(input("Input 3\n"))
    D = str(input("Input 4\n"))

    print("New test data {}, {}, {}".format(A,B,C,D))

    print(neuralNetwork.think(np.array([A,B,C,D])))