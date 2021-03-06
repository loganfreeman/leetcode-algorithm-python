class Solution(object):
    def threeSum(self, nums):
      """[summary]

      Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

      Note:

      The solution set must not contain duplicate triplets.
      """
      nums.sort()
      result = []
      for i in range(len(nums)-2):
         if i> 0 and nums[i] == nums[i-1]:
            continue
         l = i+1
         r = len(nums)-1
         while(l<r):
            sum = nums[i] + nums[l] + nums[r]
            if sum<0:
               l+=1
            elif sum >0:
               r-=1
            else:
               result.append([nums[i],nums[l],nums[r]])
               while l<len(nums)-1 and nums[l] == nums[l + 1] : l += 1
               while r>0 and nums[r] == nums[r - 1]: r -= 1
               l+=1
               r-=1
      return result

    def threeSumClosest(self, num, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num.sort()
        error = float("infinity")
        if len(num)<3:
            return 0
        for i in range(0, len(num)-2):
            begin = i+1
            end = len(num)-1
            while begin<end:
                if abs(num[i]+num[begin]+num[end]-target) < error:
                    error = abs(num[i]+num[begin]+num[end]-target)
                    solution = num[i]+num[begin]+num[end]
                if num[i]+num[begin]+num[end] > target:
                    end -= 1
                else:
                    begin += 1
        return solution
ob1 = Solution()
print(ob1.threeSum([-1,0,1,2,-1,-4]))
print(ob1.threeSumClosest([-1,0,1,2,-1,-4], 2))