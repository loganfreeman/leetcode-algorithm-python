'''
BFS time complexity : O(|E| + |V|)
BFS space complexity : O(|E| + |V|)
do BFS from (0,0) of the grid and get the minimum number of steps needed to get to the lower right column
only step on the columns whose value is 1
if there is no path, it returns -1
Ex 1)
If grid is
[[1,0,1,1,1,1],
 [1,0,1,0,1,0],
 [1,0,1,0,1,1],
 [1,1,1,0,1,1]],
the answer is: 14
Ex 2)
If grid is
[[1,0,0],
 [0,1,1],
 [0,1,1]],
the answer is: -1
'''
from collections import deque
def maze_search(maze):
    BLOCKED, ALLOWED = 0, 1
    UNVISITED, VISITED = 0, 1

    initial_x, initial_y = 0, 0

    if maze[initial_x][initial_y] == BLOCKED:
        return -1

    directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]

    height, width = len(maze), len(maze[0])

    target_x, target_y = height - 1, width - 1

    queue = deque([(initial_x, initial_y, 0)])

    is_visited = [[UNVISITED for w in range(width)] for h in range(height)]
    is_visited[initial_x][initial_y] = VISITED

    while queue:
        x, y, steps = queue.popleft()
        if x == target_x and y == target_y:
            return steps
        for dx, dy in directions:
            nx = x + dx
            ny = y + dy
            if not ( 0 <= nx < height and 0 <= ny < width ):
                continue
            if maze[nx][ny] == ALLOWED and is_visited[nx][ny] == UNVISITED:
                queue.append((nx, ny, steps +1))
                is_visited[nx][ny] = VISITED

    return -1