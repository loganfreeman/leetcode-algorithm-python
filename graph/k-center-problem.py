def k_centers(graph, n, vertices):
    centers = []
    # add an abitrary node, here, the first node to the centers list
    centers.append(vertices[0])
    vertices.pop(0)
    while len(vertices) > 0:
        city_dict = {}
        for v in vertices:
            min_dist = float("inf")
            for c in centers:
                min_dist = min(min_dist, graph[c][v])
            city_dict[v] = min_dist
        new_center = max(city_dict, key = lambda i : city_dict[i])
        centers.append(new_center)
        vertices.remove(v)
    return centers
