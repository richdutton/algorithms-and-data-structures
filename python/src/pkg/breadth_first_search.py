# pylint:disable=C0103

from collections import namedtuple, deque

Graph = namedtuple('Graph', 'nodes connections')
_NodeAndParent = namedtuple('NodeAndParent', 'node parent')


def simple_breadth_first_search(graph, node_1, node_2):
    visited = set()
    queue = deque([node_1])

    while queue:
        node = queue.pop()

        if node not in visited:
            visited.add(node)

            if node == node_2:
                return len(visited)

            for next_node in graph.connections[node]:
                queue.appendleft(next_node)

    return 0


def tracking_breadth_first_search(graph, node_1, node_2):
    visited = {}
    queue = deque([_NodeAndParent(node_1, None)])

    while queue:
        node, parent = queue.pop()

        if node not in visited:
            # todo: will this be correct in the face of overwrites?
            # when could overwrite happen?
            # A->B1; A->B2; B1->D1; B2->C2; -> c2 -> D1
            # write a test to verify this case breaks and then fix to check node is not already in visited
            visited[node] = parent

            if node == node_2:
                path = []
                while True:
                    path.append(node)
                    node = visited[node]
                    if node is None:
                        break
                path.reverse()
                return path

            for next_node in graph.connections[node]:
                queue.appendleft(_NodeAndParent(next_node, node))

    return None


# todo: why isn't this faster?
def bidirectional_breadth_first_search(graph, node_1, node_2):
    visited = set()
    visited_alternate = set()
    queue = deque([node_1])
    queue_alternate = deque([node_2])

    while queue:
        node = queue.pop()

        if node not in visited:
            # todo: this could really be moved below the comparison in all but tracking,
            # and maybe even in that
            visited.add(node)

            if node == node_2:
                # todo: this len thing is a hack
                return len(visited) + len(visited_alternate)

            for next_node in graph.connections[node]:
                queue.appendleft(next_node)

        queue, queue_alternate = queue_alternate, queue
        visited, visited_alternate = visited_alternate, visited
        node_1, node_2 = node_2, node_1

    return 0
