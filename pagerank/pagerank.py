

def pagerank(graph):
    #initialises values
    n = len(graph.nodes)
    init_val = 1.0/n
    ranks = dict(zip(graph.get_nodes(), [init_val] * n))

    new_ranks = ranks
    #calculates new rank
    for node, prev_rank in ranks.items():
        rank_sum = 0.0
        #iterates through incoming nodes
        for incoming_node in node.inbound:
            numerator = ranks[incoming_node]
            denominator = len(incoming_node.outbound)
            transfer_amount = numerator / denominator

            #score transfer
            new_ranks[incoming_node] = new_ranks[incoming_node] - transfer_amount
            rank_sum = rank_sum + transfer_amount

        new_ranks[node] = ranks[node] + rank_sum

    ranks = new_ranks

    return ranks