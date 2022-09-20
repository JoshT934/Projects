# Base layer class for other classes to inherit from
class Layer:
    def __init__(self):
        self.inp = None
        self.output = None

    # computes the output Y of a layer for a given input X
    def forward_prop(self, input):
        pass

    # computes dE/dX for a given dE/dY (and update parameters if any)
    def backward_prop(self, output_error, learning_rate):
        pass

