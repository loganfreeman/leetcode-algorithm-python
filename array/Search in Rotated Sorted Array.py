def search (arr, l, h, key):
    if l > h:
        return -1

    mid = (l + h) // 2
    if arr[mid] == key:
        return mid

    # If arr[l...mid] is sorted
    if arr[l] <= arr[mid]:

        # As this subarray is sorted, we can quickly
        # check if key lies in half or other half
        if key >= arr[l] and key <= arr[mid]:
            return search(arr, l, mid-1, key)
        return search(arr, mid+1, h, key)

    # If arr[l..mid] is not sorted, then arr[mid... r]
    # must be sorted
    if key >= arr[mid] and key <= arr[h]:
        return search(a, mid+1, h, key)
    return search(arr, l, mid-1, key)

def search(nums, target):
    l = 0
    r = len(nums) - 1
    while (l <= r):
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if target >= nums[l] and target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if target >= nums[m] and target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1

arr = [4, 5, 6, 7, 8, 9, 1, 2, 3]
target = 6
i = search(arr, target)
print(i)
arr = [4,5,6,7,0,1,2]
target = 0
i = search(arr, target)
print(i)