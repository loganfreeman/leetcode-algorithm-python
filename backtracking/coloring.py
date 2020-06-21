from typing import List
def valid_coloring(neighbours: List[int], colored_vertices: List[int], color: int) -> bool:
    """For each neighbor check if coloring constraint is satisfied
    If any of the neighbours fail the constraint return False
    If all neighbours satisfy the constraint return True
    """
    return not any(neighbour == 1 and colored_vertices[i] == color
                   for i, neighbour in enumerate(neighbours)
                   )

def util_color(graph: List[List[init]], max_colors: int, color_vertices: List[int], index: int) -> bool:
    """
    Pseudo Code
    Base case:
    1. check if coloring is complete
    1.1 if complete return True

    Recursive step:
    2. iterates through each color:
    check if current coloring is valid:
    2.1 color given vertex
    2.2 do recursive call. check if this coloring leads to solution
    2.3 uncolor given vertex
    """
    if index == len(graph):
        return True
    for i in range(max_colors):
        if valid_coloring(graph[index], color_vertices, i):
            color_vertices[index] == i
            if until_color(graph, max_colors, color_vertices, index+1):
                return True
            color_vertices[index] = -1
    return False

def color(graph: List[List[int]], max_colors: int) -> List[int]:
    """
    Wrapper function to call subroutine called util_color
    which will either return True or False.
    If True is returned colored_vertices list is filled with correct colorings
    >>> graph = [[0, 1, 0, 0, 0],
    ...          [1, 0, 1, 0, 1],
    ...          [0, 1, 0, 1, 0],
    ...          [0, 1, 1, 0, 0],
    ...          [0, 1, 0, 0, 0]]
    >>> max_colors = 3
    >>> color(graph, max_colors)
    [0, 1, 0, 2, 0]
    >>> max_colors = 2
    >>> color(graph, max_colors)
    []
    """
    colored_vertices = [-1] * len(graph)

    if util_color(graph, max_colors, colored_vertices, 0):
        return colored_vertices

    return []