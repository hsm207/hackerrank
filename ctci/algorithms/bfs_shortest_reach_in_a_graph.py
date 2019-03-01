# problem description: https://www.hackerrank.com/challenges/ctci-bfs-shortest-reach/problem

# store a graph as a dictionary of sets
class Graph:
    def __init__(self, n):
        # n is the number of nodes
        # store the connections between each node
        self.edges = {i: set() for i in range(n)}

        # store the shortest distance between node s(given) and any other node
        self.dist = {i: -1 for i in range(n)}

    def connect(self, i, j):
        # this is an undirected graph, so node i connect to node j and node j
        # connects to node i

        self.edges[i].add(j)
        self.edges[j].add(i)

    def find_all_distances(self, s):
        # do breadth first search
        queue = [s]

        # the distance of s to itself is 0
        self.dist[s] = 0

        while queue:
            start_node = queue.pop(0)
            # do not include neighbours that have been visitied i.e. distance from s is not -1
            neighbours = [neighbour for neighbour in self.edges[start_node]
                          if self.dist[neighbour] == -1]

            for node in neighbours:
                # update the distance of each neighbour from s
                self.dist[node] = self.dist[start_node] + 6
                # add the neighbour to the queue
                queue.append(node)

        print(*[v for k, v in self.dist.items() if k != s])


n, m = 4, 2
graph = Graph(n)
for node_pair in [(1, 2), (1, 3)]:
    x, y = node_pair
    graph.connect(x - 1, y - 1)
s = 1
graph.find_all_distances(s - 1)
