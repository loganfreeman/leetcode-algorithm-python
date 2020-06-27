# Python3 program to generate a graph
# for a given fixed degrees

# A function to print the adjacency matrix.
def printMat(degseq, n):

    # n is number of vertices
    mat = [[0] * n for i in range(n)]

    for i in range(n):
        for j in range(i + 1, n):

            # For each pair of vertex decrement
            # the degree of both vertex.
            if (degseq[i] > 0 and degseq[j] > 0):
                degseq[i] -= 1
                degseq[j] -= 1
                mat[i][j] = 1
                mat[j][i] = 1

    # Print the result in specified form
    print("      ", end = " ")
    for i in range(n):
        print(" ", "(", i, ")", end = "")
    print()
    print()
    for i in range(n):
        print(" ", "(", i, ")", end = "")
        for j in range(n):
            print("     ", mat[i][j], end = "")
        print()

# Driver Code
if __name__ == '__main__':
    degseq = [2, 2, 1, 1, 1]
    n = len(degseq)
    printMat(degseq, n)