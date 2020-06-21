def create_state_space_tree(sequence, current, index):
    if index == len(sequence):
        print(current)
        return
    create_state_space_tree(sequence, current, index+1)
    current.append(sequence[index])
    create_state_space_tree(sequence, current, index+1)
    current.pop()

def generate_all_subsequences(sequence):
    create_state_space_tree(sequence, [], 0)

"""
remove the comment to take an input from the user
print("Enter the elements")
sequence = list(map(int, input().split()))
"""

sequence = [3, 1, 2, 4]
generate_all_subsequences(sequence)

sequence = ["A", "B", "C"]
generate_all_subsequences(sequence)