
def color(g):
    num_edges = sum([sum(i)for i in g])
    e = []
    for i in range(len(g)):
        for j in range(len(g[0])):
            if g[i][j]:
                for k in range(g[i][j]):
                    e.append([i+1, j+1])
    c = 0
    colors = [0] * num_edges
    P = set()
    Q = set()
    for i in range(num_edges):
        P.clear()
        Q.clear()
        if colors[i] == 0:
            c = c + 1
            j = i
            while j < num_edges:
                if e[j][0] not in P and e[j][1] not in Q and colors[j] == 0:
                    colors[j] = c
                    P.add(e[j][0])
                    Q.add(e[j][1])
                j = j + 1
    print("共", c, "节课")
    for i in range(1, c+1):
        class_i = [e[j] for j in range(num_edges) if colors[j] == i]
        print(class_i)


if __name__ == "__main__":
    g = [[2, 0, 1, 1, 0],
         [0, 1, 0, 1, 0],
         [0, 1, 1, 1, 0],
         [0, 0, 0, 1, 1]]
    color(g)

