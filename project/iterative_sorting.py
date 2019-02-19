# Complete the selection_sort() function below in class with your instructor


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        for j in range(i, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

        # TO-DO: swap
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]

    return arr


# TO-DO: implement the Insertion Sort function below
def insertion_sort(arr):
    for i in range(1, len(arr)):

        currentVal = arr[i]
        pos = i

        while pos > 0 and arr[pos - 1] > currentVal:
            arr[pos] = arr[pos - 1]
            pos = pos - 1

        arr[pos] = currentVal

    return arr


print(insertion_sort([1, 54, 18, 12, 23, 9, 13, 0, 10, 79]))

# STRETCH: implement the Bubble Sort function below


def bubble_sort(arr):
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr
