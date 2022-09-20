from layer import Layer

# inherits from class "layer"
class ActivationLayer(Layer):
    def __init__(self, activation, activation_prime):
        self.activation = activation
        self.activation_prime = activation_prime

    # returns the activated input
    def forward_prop(self, input_data):
        self.inp = input_data
        self.output = self.activation(self.inp)
        return self.output

    # Returns input_error=dE/dX for a given output_error=dE/dY.
    def backward_prop(self, output_error, learning_rate):
        return self.activation_prime(self.inp) * output_error