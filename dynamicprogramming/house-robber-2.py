class Solution(object):
    def _rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        rob = 0
        notRob = 0
        for n in nums:
            currentRob = notRob + n
            notRob = max(notRob, rob)
            rob = currentRob
        return max(rob, notRob)
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        rob1 = self._rob(nums[0:len(nums)-1])
        rob2 = self._rob(nums[1:len(nums)])
        return max(rob1, rob2)
