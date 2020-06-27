from queue import Queue

def isBipartiteUntil(G, src, colorArr):
    global V
    colorArr[src] = 1
    q = Queue()
    q.put(src)
    while (not q.empty()):
        u = q.get()
        for v in range(V):
            if (G[u][v] and colorArr[v] == -1):
                colorArr[v] = 1 - colorArr[u]
                q.put(v)
            elif (G[u][v] and colorArr[v] == colorArr[u]):
                return False
    return True

def isBipartite(G):
    global V

    colorArr = [-1] * V
    for i in range(V):
        if(colorArr[i] == -1):
            if(isBipartiteUntil(G, i, colorArr) == False):
                return False
    return True

def canBeDividedInTowCliques(G):
    global V
    CG = [[None] * V for i in range(V)]
    for i in range(V):
        for j in range(V):
            CG[i][j] = not G[i][j] if i != j else 0

    return isBipartite(CG)

# Driver Code
V = 5

G = [[0, 1, 1, 1, 0],
     [1, 0, 1, 0, 0],
     [1, 1, 0, 0, 0],
     [0, 1, 0, 0, 1],
     [0, 0, 0, 1, 0]]

if canBeDividedInTowCliques(G):
    print("Yes")
else:
    print("No")