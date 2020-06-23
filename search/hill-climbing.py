import math
class SearchProblem:
    def __init__(self, x: int, y: int, step_size: int, function_to_optimize):
        """
        The constructor of the search problem.
        x: the x coordinate of the current search state.
        y: the y coordinate of the current search state.
        step_size: size of the step to take when looking for neighbors.
        function_to_optimize: a function to optimize having the signature f(x, y).
        """
        self.x = x
        self.y = y
        self.step_size = step_size
        self.function = function_to_optimize
    def score(self) -> int:
        return self.function(self.x, self.y)
    def get_neighbors(self):
        """return a list of coordinates of neighbors adjacent to the current coordinates
        """
        step_size = self.step_size
        return [
            SearchProblem(x, y, step_size, self.function)
            for x, y in (
                (self.x - step_size, self.y - step_size),
                (self.x - step_size, self.y),
                (self.x - step_size, self.y + step_size),
                (self.x, self.y - step_size),
                (self.x, self.y + step_size),
                (self.x + step_size, self.y - step_size),
                (self.x + step_size, self.y),
                (self.x + step_size, self.y + step_size),
            )
        ]
    def __hash__(self):
        return hash(str(self))
    def __eq__(self, obj):
        if isinstance(obj, SearchProblem):
            return hash(str(self)) == hash(str(obj))
        return False

    def __str__(self):
        return f"x: {self.x} y: {self.y}"

def hill_climbing(
    search_prob: SearchProblem,
    find_max: bool = True,
    max_x: float = math.inf,
    min_x: float = -math.inf,
    max_y: float = math.inf,
    min_y: float = -math.inf,
    visualization: bool = False,
    max_iter: int = 10000,
) -> SearchProblem:
    """implmentation of the hill climbing algorithm.
    We start with a given state, find all its neighbors,
    move towards the neighbor which provides the maximum change.
    We keep doing this until we are at a state where do not have any neighbors which can improve the solution.

    Args:
        search_prob ([type]): [description]
        find_max (bool, optional): [description]. Defaults to True.
        max_x (float, optional): [description]. Defaults to math.inf.
        min_x (float, optional): [description]. Defaults to -math.inf.
        max_y (float, optional): [description]. Defaults to math.inf.
        min_y (float, optional): [description]. Defaults to -math.inf.
        visualization (bool, optional): [description]. Defaults to False.
        max_iter (int, optional): [description]. Defaults to 10000.

    Returns:
        SearchProblem: [description]
    """
    current_state = search_prob
    scores = []
    iterations = 0
    solution_found = False
    visited = set()
    while not solution_found and iterations < max_iter:
        visited.add(current_state)
        iterations += 1
        current_score = current_state.score()
        scores.append(current_score)
        neighbors = current_state.get_neighbors()
        max_change = -math.inf
        min_change = math.inf
        next_state = None  # to hold the next best neighbor
        for neighbor in neighbors:
            if neighbor in visited:
                continue
            if (
                neighbor.x > max_x
                or neighbor.x < min_x
                or neighbor.y > max_y
                or neighbor.y < min_y
            ):
                continue # neighbor outside bound
            change = neighbor.score() - current_score
            if find_max:
                if change > max_change and change > 0:
                    max_change = change
                    next_state = neighbor
            else:
                if change < min_change and change < 0:
                    min_change = change
                    next_state = neighbor

        if next_state is not None:
            current_state = next_state
        else:
            solution_found = True

    if visualization:
        import matplotlib.pyplot as plt

        plt.plot(range(iterations), scores)
        plt.xlabel("Iterations")
        plt.ylabel("Function values")
        plt.show()

    return current_state

if __name__ == "__main__":
    import doctest

    doctest.testmod()

    def test_f1(x, y):
        return (x ** 2) + (y ** 2)

    # starting the problem with initial coordinates (3, 4)
    prob = SearchProblem(x=3, y=4, step_size=1, function_to_optimize=test_f1)
    local_min = hill_climbing(prob, find_max=False)
    print(
        "The minimum score for f(x, y) = x^2 + y^2 found via hill climbing: "
        f"{local_min.score()}"
    )

    # starting the problem with initial coordinates (12, 47)
    prob = SearchProblem(x=12, y=47, step_size=1, function_to_optimize=test_f1)
    local_min = hill_climbing(
        prob, find_max=False, max_x=100, min_x=5, max_y=50, min_y=-5, visualization=True
    )
    print(
        "The minimum score for f(x, y) = x^2 + y^2 with the domain 100 > x > 5 "
        f"and 50 > y > - 5 found via hill climbing: {local_min.score()}"
    )

    def test_f2(x, y):
        return (3 * x ** 2) - (6 * y)

    prob = SearchProblem(x=3, y=4, step_size=1, function_to_optimize=test_f1)
    local_min = hill_climbing(prob, find_max=True)
    print(
        "The maximum score for f(x, y) = x^2 + y^2 found via hill climbing: "
        f"{local_min.score()}"
    )