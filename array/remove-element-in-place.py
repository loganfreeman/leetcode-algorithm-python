class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
        return j

    def removeDuplicates(self, arr):
        n = len(arr)
        if n == 0 or n == 1:
            return n

        # To store index of next
        # unique element
        j = 0

        # Doing same as done
        # in Method 1 Just
        # maintaining another
        # updated index i.e. j
        for i in range(0, n-1):
            if arr[i] != arr[i+1]:
                arr[j] = arr[i]
                j += 1

        arr[j] = arr[n-1]
        j += 1
        return j