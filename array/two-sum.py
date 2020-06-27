class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = dict()
        for i in range(len(nums)):
            if target - nums[i] in map:
                return [i, map[target - nums[i]]]
            else:
                map[nums[i]] = i
        return None
