class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def searchFirstOccurance(nums):
            l = 0
            r = len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    while m > 0 and nums[m-1] == nums[m]:
                        m = m - 1
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1

            return -1
        def searchLastOccurance(nums):
            l = 0
            r = len(nums) - 1
            while l <= r:
                m = (l + r) // 2
                if nums[m] == target:
                    while m < len(nums) - 1 and nums[m+1] == nums[m]:
                        m = m + 1
                    return m
                elif nums[m] > target:
                    r = m - 1
                else:
                    l = m + 1

            return -1
        first = searchFirstOccurance(nums)
        last = searchLastOccurance(nums)
        return [first, last]
