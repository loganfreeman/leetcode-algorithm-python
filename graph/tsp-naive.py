"""
Travelling Salesman Problem (TSP): Given a set of cities and distance between every pair of cities, the problem is to find the shortest possible route that visits every city exactly once and returns back to the starting point.
A naive implementation would be:
1. Consider city 1 as the starting and ending point. Since route is cyclic, we can consider any point as starting point.
2. Generate all (n-1)! permutations of cities.
3. Calculate cost of every permutation and keep track of minimum cost permutation.
4. Return the permutation with minimum cost.

"""

from sys import maxsize
V = 4
def perm_generator(lst):
    res = []
    if len(lst) == 1:
        return [lst]
    else:
        for i in range(len(lst)):
            for perm in perm_generator(lst[:i] + lst[i+1:]):
                res.append([lst[i]] + perm)
    return res


def tsp(graph):
    min_path = maxsize
    for vertex in perm_generator(list(range(V))):
        k = 0
        current_pathweight = 0
        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)
    return min_path


def travellingSalesmanProblem(graph, s):

    # store all vertex apart from source vertex
    vertex = []
    for i in range(V):
        if i != s:
            vertex.append(i)

    # store minimum weight Hamiltonian Cycle
    min_path = maxsize

    while True:

        # store current Path weight(cost)
        current_pathweight = 0

        # compute current path weight
        k = s
        for i in range(len(vertex)):
            current_pathweight += graph[k][vertex[i]]
            k = vertex[i]
        current_pathweight += graph[k][s]

        # update minimum
        min_path = min(min_path, current_pathweight)

        if not next_permutation(vertex):
            break

    return min_path

def next_permutation(L):

    n = len(L)

    i = n - 2
    while i >= 0 and L[i] >= L[i + 1]:
        i -= 1

    if i == -1:
        return False

    j = i + 1
    while j < n and L[j] > L[i]:
        j += 1
    j -= 1

    L[i], L[j] = L[j], L[i]

    left = i + 1
    right = n - 1

    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1

    return True

# Driver Code
if __name__ == "__main__":

    # matrix representation of graph
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(travellingSalesmanProblem(graph, s))
    print(tsp(graph))
