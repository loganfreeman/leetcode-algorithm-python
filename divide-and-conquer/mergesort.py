def merge(arr, left, mid, right):
    left_arr = arr[left: mid+1]
    right_arr = arr[mid+1: right+1]
    k = left
    i = 0
    j = 0
    while i < len(left_arr) and j < len(right_arr):
        if left_arr[i] < right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < len(right_arr):
        arr[k] = right_arr[j]
        j += 1
        k += 1
    return arr
def mergesort(arr, left, right):
    if left < right:
        mid = (left + right) // 2
        mergesort(arr, left, mid)
        mergesort(arr, mid+1, right)
        merge(arr, left, mid, right)
        return arr
if __name__ == "__main__":
    import doctest

    doctest.testmod()