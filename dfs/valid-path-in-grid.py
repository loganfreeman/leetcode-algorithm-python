class Solution(object):
    def hasValidPath(self, grid):
        dic_pair = {}
        dic_pair[(1, 'L')] = [1, 4, 6]
        dic_pair[(1, 'R')] = [1, 3, 5]
        dic_pair[(2, 'D')] = [2, 5, 6]
        dic_pair[(2, 'U')] = [2, 3, 4]
        dic_pair[(3, 'L')] = [1, 4, 6]
        dic_pair[(3, 'D')] = [2, 5, 6]
        dic_pair[(4, 'R')] = [1, 3, 5]
        dic_pair[(4, 'D')] = [2, 5, 6]
        dic_pair[(5, 'U')] = [2, 3, 4]
        dic_pair[(5, 'L')] = [1, 4, 6]
        dic_pair[(6, 'U')] = [2, 3, 4]
        dic_pair[(6, 'R')] = [1, 3, 5]

        dic_dir = {}
        dic_dir[1] = ['L', 'R']
        dic_dir[2] = ['U', 'D']
        dic_dir[3] = ['L', 'D']
        dic_dir[4] = ['R', 'D']
        dic_dir[5] = ['L', 'U']
        dic_dir[6] = ['R', 'U']

        queue = []

        def verify():
            dic_visit = {}
            dic_visit[{0, 0}] = 1

            direction = {}
            direction['R'] = (0, 1)
            direction['L'] = (0, -1)
            direction['U'] = (-1, 0)
            direction['D'] = (1, 0)

            while(len(queue) > 0):
                x, y, d = queue.pop()
                if x == len(grid) - 1 and y == len(grid) - 1:
                    return True

                x1, y1 = direction[d]
                if x1 + x >= 0 and x1 + x < len(grid) and y + y1 >= 0 and y + y1 < len(grid[0]) \
                        and grid[x1 + x][y1 + y] in dic_pair[(grid[x][y], d)] and (x1 + x, y1 + y) not in dic_visit:
                    if d == 'L':
                        reversed_d = 'R'
                    elif d == 'R':
                        reversed_d = 'L'
                    elif d == 'U':
                        reversed_d = 'D'
                    else:
                        reversed_d = 'U'
                    inx = dic_dir[grid[x1 + x][y1 + y]].index(reversed_d)
                    if inx == 0:
                        d1 = dic_dir[grid[x1 + x][y1 + y]][1]
                    else:
                        d1 = dic_dir[grid[x1 + x][y1 + y]][0]
                    queue.append((x1 + x, y1 + y, d1))
                    dic_visit[(x1 + x, y1 + y)] = 1
            return False
        if grid[0][0] == 1:
            queue.append((0, 0, 'R'))
        elif grid[0][0] == 2:
            queue.append((0, 0, 'D'))
        elif grid[0][0] == 3:
            queue.append((0, 0, 'D'))
        elif grid[0][0] == 4:
            queue.append((0, 0, 'D'))
        elif grid[0][0] == 6:
            queue.append((0, 0, 'R'))
        return verify()
