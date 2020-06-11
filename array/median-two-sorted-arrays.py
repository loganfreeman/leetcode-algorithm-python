"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Input : ar1[] = {-5, 3, 6, 12, 15}
        ar2[] = {-12, -10, -6, -3, 4, 10}
        The merged array is :
        ar3[] = {-12, -10, -6, -5 , -3,
                 3, 4, 6, 10, 12, 15}
Output : The median is 3.

Input : ar1[] = {2, 3, 5, 8}
        ar2[] = {10, 12, 14, 16, 18, 20}
        The merged array is :
        ar3[] = {2, 3, 5, 8, 10, 12, 14, 16, 18, 20}
        if the number of the elements are even,
        so there are two middle elements,
        take the average between the two :
        (10 + 12) / 2 = 11.
Output : The median is 11.
"""
median = 0
i = 0
j = 0

def maximum(a, b):
    return a if a > b else b

def minimum(a, b):
    return a if a < b else b

def findMedianSortedArrays(a, n, b, m):
    global median, i, j
    min_index = 0
    max_index = n
    while(min_index <= max_index):
        i = int((min_index + max_index) / 2)
        j = int(((n + m + 1) / 2) - i)

        if (i < n and j > 0 and b[j - 1] > a[i]):
            min_index = i + 1
        else:
            if(i == 0):
                median = b[j - 1]
            elif (j == 0):
                median = a[i - 1]
            else:
                median = maximum(a[i - 1], b[j - 1])
            break

    # calculating the median.
    # If number of elements
    # is odd there is
    # one middle element.

    if ((n + m) % 2 == 1) :
        return median

    # Elements from a[] in the
    # second half is an empty set.
    if (i == n) :
        return ((median + b[j]) / 2.0)

    # Elements from b[] in the
    # second half is an empty set.
    if (j == m) :
        return ((median + a[i]) / 2.0)

    return ((median + minimum(a[i], b[j])) / 2.0)

# Driver code
a = [900]
b = [10, 13, 14]
n = len(a)
m = len(b)

# we need to define the
# smaller array as the
# first parameter to make
# sure that the time complexity
# will be O(log(min(n,m)))
if (n < m) :
    print ("The median is : {}".format(findMedianSortedArrays(a, n, b, m)))
else :
    echo ("The median is : {}".format(findMedianSortedArrays(b, m, a, n)))