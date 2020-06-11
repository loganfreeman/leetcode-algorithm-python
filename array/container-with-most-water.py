"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

"""

class Solution(object):
    def maxArea(self, height):
        """
        The idea is quite simple and involves checking every pair of boundaries and find out the maximum area under any pair of boundaries
        """
        l = 0
        r = len(height) - 1
        area = 0
        while(l < r):
            area = max(area, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return area

obj = Solution()
a = [1, 5, 4, 3]
b = [3, 1, 2, 4, 5]
print(obj.maxArea(a))
print(obj.maxArea(b))