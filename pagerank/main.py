from graph import Node,Graph
from pagerank import pagerank

a = Node()
b = Node()
c = Node()

g = Graph()

g.add_node('A',a)
g.add_node('B',b)
g.add_node('C',c)

g.add_edge('A','B')
g.add_edge('B','C')
g.add_edge('A','C')
g.add_edge('C','A')


ranks = pagerank(g)

for node,value in ranks.items():
  print(node.name,value)


print(g.adjacency_matrix())