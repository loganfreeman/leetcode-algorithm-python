def generate_sum_of_subset(nums, max_sum):
    result = []
    path = []
    num_index = 0
    remaining_sum = sum(nums)
    create_state_space_tree(nums, max_sum, num_index, path, result, remaining_sum)
    return result

def create_state_space_tree(nums, max_sum, num_index, path, result, remaining_nums_sum):
    """iterate through each branch using DFS
    it terminates when
    1. the sum of the path is equal to target
    2. the sum of the path exceeds the target
    """
    if sum(path) > max_sum or \
        (remaining_nums_sum + sum(path)) < max_sum:
            return
    if sum(path) == max_sum:
        result.append(path)
        return
    for ni in range(num_index, len(nums)):
        create_state_space_tree(nums, max_sum, ni + 1, path + [nums[ni]], result, remaining_nums_sum - nums[ni])

"""
remove the comment to take an input from the user
print("Enter the elements")
nums = list(map(int, input().split()))
print("Enter max_sum sum")
max_sum = int(input())
"""
nums = [3, 34, 4, 12, 5, 2]
max_sum = 7
result = generate_sum_of_subset(nums, max_sum)
print(*result)