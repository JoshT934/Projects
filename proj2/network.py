class Network:
    def __init__(self):
        self.layers = []
        self.loss = None
        self.loss_prime = None

    # add layer to network
    def add(self, layer):
        self.layers.append(layer)

    # set loss function to use
    def use(self, loss, loss_prime):
        self.loss = loss
        self.loss_prime = loss_prime

    # predict output y for given input x
    def predict(self, input_data):
        # sample dimension first
        set = len(input_data)
        result = []

        # run network over inputs
        for i in range(set):
            # forward propagation
            output = input_data[i]
            for eachlayer in self.layers:
                output = eachlayer.forward_prop(output)
            result.append(output)

        return result

    # train the network
    def fit(self, x_train, y_train, epochs, learning_rate):
        # get inputs dimension first
        ent = len(x_train)

        # training loop
        for i in range(epochs):
            err = 0
            for j in range(ent):
                # forward prop
                output = x_train[j]
                for layer in self.layers:
                    output = layer.forward_prop(output)

                # compute loss
                err += self.loss(y_train[j], output)

                # backward propa
                error = self.loss_prime(y_train[j], output)
                for layer in (self.layers)[::-1]:
                    error = layer.backward_prop(error, learning_rate)

            # calculate average error
            err /= ent
            print('epoch %d/%d   error=%f' % (i+1, epochs, err))