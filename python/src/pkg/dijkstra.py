from collections import namedtuple

WeightedGraph = namedtuple('WeightedGraph', 'nodes connections_and_weights')
ConnectionAndWeight = namedtuple('ConnectionAndWeight', 'connection weight')
PathAndCost = namedtuple('PathAndCost', 'path cost')


def dijkstra_cost(weighted_graph, start, end):
    costs = {node: float('inf') for node in weighted_graph.nodes}
    costs[start] = 0
    nodes_left_to_explore = set(weighted_graph.nodes)
    nodes_left_to_explore.remove(end)

    while nodes_left_to_explore:
        cheapest_node, cheapest_node_cost = min(costs.items(), key=lambda x: x[1] if x[0] in nodes_left_to_explore else float('inf'))

        for connection, weight in weighted_graph.connections_and_weights[cheapest_node]:
            total_cost = weight + cheapest_node_cost
            if total_cost < costs[connection]:
                costs[connection] = total_cost

        nodes_left_to_explore.remove(cheapest_node)

    return costs[end]
