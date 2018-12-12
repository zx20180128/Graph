
class Graph:
    def __init__(self):
        self.Vertices = set()
        self.Edges = {}

    def add_vertices(self, t):
        self.Vertices.add(t)

    def add_edges(self, s, t, capacity):
        self.Edges[(s, t)] = [capacity, 0]  #[c,f]

    def __str__(self):
        string = "Vertices: " + str(self.Vertices) + '\n'
        string += "Edges'capacity: " + str(self.Edges) + '\n'
        return string


def Dinic_BFS(g, s, t):
    global level
    level = {}.fromkeys(list(g.Vertices))
    level[s] = 0
    queue = [s]
    while queue:
        for _ in range(len(queue)):
            x = queue.pop(0)
            V = [i[1] for i, [c, f]in g.Edges.items() if i[0] == x and level[i[1]] is None and c > f]
            for v in V:
                level[v] = level[x] + 1
                queue.append(v)
    if level[t] is None:
        return False
    else:
        return True


def Dinic_DFS(g, s, t, min_flow):
    if s == t:
        return min_flow
    V = {i[1]: [c, f] for i, [c, f]in g.Edges.items() if i[0] == s and level[i[1]] == level[i[0]] + 1}
    min_return = 0
    for v, [c, f] in V.items():
        min_return = Dinic_DFS(g, v, t, min(c-f, min_flow))
        g.Edges[(s, v)][0] -= min_return
        if (v, s) in g.Edges:
            g.Edges[(v, s)][0] += min_return
        else:
            g.Edges[(v, s)] = [min_return, 0]
    return min_return



def Dinic(g, s, t):
    max_flow = 0
    while Dinic_BFS(g, s, t):
        Dinic_DFS(g, s, t, 10000)
    f = [c for i, [c, f] in g.Edges.items() if i[1] == s]
    for i in f:
        max_flow += i
    return max_flow


if __name__ == '__main__':
    g = Graph()
    g.add_vertices('s')
    g.add_vertices('v1')
    g.add_vertices('v2')
    g.add_vertices('v3')
    g.add_vertices('v4')
    g.add_vertices('t')
    # s
    g.add_edges('s', 'v1', 8)
    g.add_edges('s', 'v2', 7)
    # v1
    g.add_edges('v1', 'v2', 5)
    g.add_edges('v1', 'v3', 9)
    # v2
    g.add_edges('v2', 'v4', 9)
    # v3
    g.add_edges('v3', 'v2', 2)
    g.add_edges('v3', 't', 5)
    # v4
    g.add_edges('v4', 'v3', 6)
    g.add_edges('v4', 't', 10)

    print(g)

    max_flow = Dinic(g, 's', 't')
    print("最大流为：", max_flow)