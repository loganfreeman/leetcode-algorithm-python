class Solution(object):
    """
Given a set, write a Python program to generate all possible subset of size n of given set within a list.

Examples:

Input : {1, 2, 3}, n = 2
Output : [{1, 2}, {1, 3}, {2, 3}]

Input : {1, 2, 3, 4}, n = 3
Output : [{1, 2, 3}, {1, 2, 4}, {1, 3, 4}, {2, 3, 4}]
    """

    def subsets(self, nums):
        temp_result = []
        self.subsets_util(nums, [0 for i in range(len(nums))], temp_result, 0)
        main_result = []
        for lists in temp_result:
            temp = []
            for i in range(len(lists)):
                if lists[i] == 1:
                    temp.append(nums[i])

            main_result.append(temp)

        return main_result

    def subsets_util(self, nums, temp, result, index):
        if index == len(nums):
            result.append([i for i in temp])
            return
        temp[index] = 0
        self.subsets_util(nums, temp, result, index+1)
        temp[index] = 1
        self.subsets_util(nums, temp, result, index+1)


ob1 = Solution()
print(ob1.subsets([1, 2, 3, 4]))
