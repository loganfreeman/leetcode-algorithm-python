# Finding Articulation Points in Undirected Graph
"""
Pick an arbitrary vertex of the graph root and run depth first search from it. Note the following fact (which is easy to prove):

1. Let's say we are in the DFS, looking through the edges starting from vertex v≠root. If the current edge (v,to) is such that none of the vertices to or its descendants in the DFS traversal tree has a back-edge to any of ancestors of v, then v is an articulation point. Otherwise, v is not an articulation point.

2. Let's consider the remaining case of v=root. This vertex will be the point of articulation if and only if this vertex has more than one child in the DFS tree.

Now we have to learn to check this fact for each vertex efficiently. We'll use "time of entry into node" computed by the depth first search.

So, let tin[v] denote entry time for node v. We introduce an array low[v] which will let us check the fact for each vertex v. low[v] is the minimum of tin[v], the entry times tin[p] for each node p that is connected to node v via a back-edge (v,p) and the values of low[to] for each vertex to which is a direct descendant of v in the DFS tree:

low[v]=min⎧⎩⎨tin[v]tin[p]low[to] for all p for which (v,p) is a back edge for all to for which (v,to) is a tree edge

Thus, the vertex v in the DFS tree is an articulation point if and only if low[to]≥tin[v].

"""
def computeAP(l):  # noqa: E741
    """
    visited[to]=false - the edge is part of DFS tree;
    visited[to]=true && to≠parent - the edge is back edge to one of the ancestors;
    to=parent - the edge leads back to parent in DFS tree.
    """
    n = len(l)
    outEdgeCount = 0
    low = [0] * n
    visited = [False] * n
    isArt = [False] * n

    def dfs(root, at, parent, outEdgeCount):
        if parent == root:
            outEdgeCount += 1
        visited[at] = True
        low[at] = at

        for to in l[at]:
            if to == parent:
                pass
            elif not visited[to]:
                outEdgeCount = dfs(root, to, at, outEdgeCount)
                low[at] = min(low[at], low[to])

                # AP found via bridge
                if at < low[to]:
                    isArt[at] = True
                # AP found via cycle
                if at == low[to]:
                    isArt[at] = True
            else:
                low[at] = min(low[at], to)
        return outEdgeCount

    for i in range(n):
        if not visited[i]:
            outEdgeCount = 0
            outEdgeCount = dfs(i, i, -1, outEdgeCount)
            isArt[i] = outEdgeCount > 1

    for x in range(len(isArt)):
        if isArt[x] is True:
            print(x)


# Adjacency list of graph
data = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3, 5],
    3: [2, 4],
    4: [3],
    5: [2, 6, 8],
    6: [5, 7],
    7: [6, 8],
    8: [5, 7],
}
computeAP(data)
