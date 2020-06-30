class Solution(object):
    def rob(self, nums):
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