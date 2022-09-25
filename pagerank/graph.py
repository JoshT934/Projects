class Node(object):
    #Node object to be used within the graph
    def __init__(self, inbound=None, outbound=None):
        self.name = ''

        if inbound:
            self.inbound = inbound
        else:
            self.inbound = []

        if outbound:
            self.outbound = outbound
        else:
            self.outbound = []


    #TODO add weights to unique edges (bias)
    def add_outbound_edge(self, node):
        #Creates edges coming out of the object node
        self.outbound.append(node)
        node.inbound.append(self)

    def add_inbound_edge(self, node):
        #Creates edges entering the object node
        self.inbound.append(node)
        node.outbound.append(self)


class Graph(object):

    def __init__(self, nodes=None):
        if nodes:
            self.nodes = nodes
        else:
            self.nodes = {} # Dict of nodes, key is node name


    def add_node(self, node_name, node):
        node.name = node_name
        self.nodes[node_name] = node
    #Creates a new node in the graph

    def add_edge(self, start_node, end_node):
        start = self.nodes[start_node]
        end = self.nodes[end_node]

        start.add_outbound_edge(end)
        #Creates edge start_node,end_node

    def get_neighbors(self, node_name):
        node = self.nodes[node_name]
        neighbors = node.outbound
        #returns adjacent nodes
        return neighbors

    def adjacency_matrix(self):
        matrix = []
        for key in self.nodes.keys():
            matrix.append(self.nodes[key].inbound())




    def get_nodes(self):
        nodes = list(self.nodes.values())
        #returns all nodes as a list
        return nodes