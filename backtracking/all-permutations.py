def craete_state_space_tree(sequence, current, index, index_used):
    """using DFS to traverse through the space.
    We know that each state has exactly (len(sequence) - index) children.
    It termiates when it reaches the end
    """
    if index == len(sequence):
        print(current)
        return
    for i in range(len(sequence)):
        if not index_used[i]:
            current.append(sequence[i])
            index_used[i] = True
            craete_state_space_tree(sequence, current, index+1, index_used)
            current.pop()
            index_used[i] = False

def generate_all_permutations(sequence):
    craete_state_space_tree(sequence, [], 0, [False for i in range(len(sequence))])

def perm_generator(lst):
    res = []
    if len(lst) == 1:
        return [lst]
    else:
        for i in range(len(lst)):
            for perm in perm_generator(lst[:i] + lst[i+1:]):
                res.append([lst[i]] + perm)
    return res

gen = perm_generator([1,2,3])

"""
remove the comment to take an input from the user
print("Enter the elements")
sequence = list(map(int, input().split()))
"""

sequence = [3, 1, 2, 4]
generate_all_permutations(sequence)

sequence = ["A", "B", "C"]
generate_all_permutations(sequence)
print(gen)
print(perm_generator(list(range(1, 5))))