
class Graph:
    def __init__(self):
        self.Vertices = set()
        self.Edges = {}

    def add_vertices(self, t):
        self.Vertices.add(t)

    def add_edges(self, s, t, distance):
        self.Edges[(s, t)] = distance

    def __str__(self):
        string = "Vertices: " + str(self.Vertices) + '\n'
        string += "Edges: " + str(self.Edges) + '\n'
        return string


def Dijkstra(g, s):
    path = {}.fromkeys(list(g.Vertices), [])
    P = {}
    distance = {}.fromkeys(list(g.Vertices), float('inf'))
    distance[s] = 0
    while P.keys() != g.Vertices:
        Q = {i: d for i, d in distance.items() if (i in P)is False}
        val, u = min(zip(Q.values(), Q.keys()))
        P[u] = val
        v_set = {k[1]: v for k, v in g.Edges.items() if k[0] == u}
        for v, dis in v_set.items():
            if distance[u] + dis < distance[v]:
                path[v] = path[u] + [u]
                distance[v] = distance[u] + dis
    for v, p in path.items():
        p.append(v)
    return P, path


if __name__ == '__main__':
    g = Graph()
    g.add_vertices('u0')
    g.add_vertices('v1')
    g.add_vertices('v2')
    g.add_vertices('v3')
    g.add_vertices('v4')
    g.add_vertices('v5')
    g.add_vertices('v6')
    g.add_vertices('v7')
    # u0
    g.add_edges('u0', 'v1', 1)
    g.add_edges('u0', 'v2', 2)
    g.add_edges('u0', 'v3', 7)
    g.add_edges('u0', 'v5', 4)
    g.add_edges('u0', 'v6', 8)
    # v1
    g.add_edges('v1', 'u0', 1)
    g.add_edges('v1', 'v2', 2)
    g.add_edges('v1', 'v6', 7)
    g.add_edges('v1', 'v7', 3)
    # v2
    g.add_edges('v2', 'u0', 2)
    g.add_edges('v2', 'v1', 2)
    g.add_edges('v2', 'v3', 5)
    g.add_edges('v2', 'v7', 1)
    # v3
    g.add_edges('v3', 'u0', 7)
    g.add_edges('v3', 'v2', 5)
    g.add_edges('v3', 'v4', 4)
    g.add_edges('v3', 'v5', 3)
    g.add_edges('v3', 'v7', 3)
    # v4
    g.add_edges('v4', 'v3', 4)
    g.add_edges('v4', 'v5', 6)
    g.add_edges('v4', 'v6', 4)
    g.add_edges('v4', 'v7', 6)
    # v5
    g.add_edges('v5', 'u0', 4)
    g.add_edges('v5', 'v3', 3)
    g.add_edges('v5', 'v4', 6)
    g.add_edges('v5', 'v6', 2)
    # v6
    g.add_edges('v6', 'u0', 8)
    g.add_edges('v6', 'v1', 7)
    g.add_edges('v6', 'v4', 4)
    g.add_edges('v6', 'v5', 2)
    # v7
    g.add_edges('v7', 'v1', 3)
    g.add_edges('v7', 'v2', 1)
    g.add_edges('v7', 'v3', 3)
    g.add_edges('v7', 'v4', 6)

    print(g)

    P, path = Dijkstra(g, 'u0')
    print('到每个点的最距离：', P)
    print(path)