
def DFS(x, g, lx, ly, visitx, visity, matchx, matchy):
    n = len(g)
    visitx[x] = 1
    for y in range(n):
        if lx[x] + ly[y] == g[x][y] and visity[y] == 0:
            visity[y] = 1
            if matchy[y] is False or DFS(matchy[y], g, lx, ly, visitx, visity, matchx, matchy):
                matchx[x] = y
                matchy[y] = x
                return True
    return False


def km(g):
    n = len(g)
    lx = [max(i) for i in g]
    ly = [0] * n
    matchx = [False] * n
    matchy = [False] * n
    for x in range(n):
        visitx = [0] * n
        visity = [0] * n
        while 1:
            if DFS(x, g, lx, ly, visitx, visity, matchx, matchy):
                break
            d = [lx[i//n]+ly[i % n]-g[i//n][i % n] for i in range(n*n) if lx[i//n]+ly[i % n]-g[i//n][i % n]]
            min_d = min(d)
            for j in range(n):
                if visitx[j]:
                    lx[j] -= min_d
                if visity[j]:
                    ly[j] += min_d
    return matchx


if __name__ == '__main__':

    g = [[3, 5, 5, 4, 1],
         [2, 2, 0, 2, 2],
         [2, 4, 4, 1, 0],
         [0, 1, 1, 0, 0],
         [1, 2, 1, 3, 3]]
    match = km(g)
    print("最优匹配为：", match)

