def Warshall(w):
    assert (len(row) == len(w) for row in w)
    n = len(w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                w[i][j] = w[i][j] or (w[i][k] and w[k][j])
    return w
