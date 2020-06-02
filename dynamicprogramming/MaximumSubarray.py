from sys import maxsize


class Solution(object):
    """[summary]

  Kadane’s Algorithm:

  Initialize:
      max_so_far = 0
      max_ending_here = 0

  Loop for each element of the array
    (a) max_ending_here = max_ending_here + a[i]
    (b) if(max_ending_here < 0)
              max_ending_here = 0
    (c) if(max_so_far < max_ending_here)
              max_so_far = max_ending_here
  return max_so_far
    """

    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = -maxsize - 1
        max_ending_here = 0
        for i in range(0, len(nums)):
            max_ending_here = max_ending_here + nums[i]

            if (max_so_far < max_ending_here):
                max_so_far = max_ending_here
            if max_ending_here < 0:
                max_ending_here = 0
        return max_so_far


obj = Solution()
a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(obj.maxSubArray(a))
