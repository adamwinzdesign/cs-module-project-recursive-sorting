# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # combined = [0] * elements

    # init a combined list that will house sorted elements from both A and B
    combined = []
    # init two pointers that start at each list
    pointer_a = 0
    pointer_b = 0

    while pointer_a < len(arrA) and pointer_b < len(arrB):
        # compare the two elements at each pointer
        # if the value at pointer_a is less than the value at pointer_B, append the value at pointer_a to combined.  If not, append the value at pointer_b.
        if arrA[pointer_a] < arrB[pointer_b]:
            combined.append(arrA[pointer_a])
            pointer_a += 1
        else:
            combined.append(arrB[pointer_b])
            pointer_b += 1
    
    # at this point, one of the lists has been completely traversed but the other has not, so we need to add the remaining value(s) from the other list to the combined list
    while pointer_a < len(arrA):
        combined.append(arrA[pointer_a])
        pointer_a += 1
    while pointer_b < len(arrB):
        combined.append(arrB[pointer_b])
        pointer_b += 1

    return combined


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # break the array down recursively by dividing the array in half until we are left with a bunch of arrays with only one element, then build a sorted array from there
    # base case: when the lists all have a length of 1
    if len(arr) > 1:
        left = merge_sort(arr[:len(arr) // 2])
        right = merge_sort(arr[len(arr) // 2:])
        arr = merge(left, right)

    return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # start 2 is the first element in the right half of the list
    start2 = mid + 1

    # If the two halves that we're merging are already sorted, no need to do anything.
    if arr[mid] <= arr[start2]:
        return
    
    # Two pointers to maintain the start of both arrays to merge
    while start <= mid and start2 <= end:

        # If element 1 is in the correct place
        if arr[start] <= arr[start2]:
            start += 1
        else:
            value = arr[start2]
            index = start2

            # Shift all elements between element 1 and element 2, right by element 1
            while index != start:
                arr[index] = arr[index - 1]
                index -= 1

            arr[start] = value

            # update pointers
            start += 1
            mid += 1
            start2 += 1


def merge_sort_in_place(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        # Sort first and second halves
        merge_sort_in_place(arr, left, mid)
        merge_sort_in_place(arr, mid + 1, right)
        merge_in_place(arr, left, mid, right)

    return arr



# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr
