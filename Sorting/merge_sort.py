def merge(arr, start, middle, end, reverse):
    temp = [0]*(end-start+1)
    i = start
    j = middle+1
    k = 0
    while i <= middle and j <= end:
        if (arr[i] <= arr[j]) == reverse:
            temp[k] = arr[i]
            k += 1
            i += 1
        else:
            temp[k] = arr[j]
            k += 1
            j += 1

    while i <= middle:
        temp[k] = arr[i]
        k += 1
        i += 1

    while j <= end:
        temp[k] = arr[j]
        k += 1
        j += 1

    for i in range(start, end+1):
        arr[i] = temp[i - start]


def merge_sort(arr, start, end, reverse=False):
    if start >= end:
        return
    middle = (start+end)//2
    merge_sort(arr, start, middle, reverse)
    merge_sort(arr, middle+1, end, reverse)
    merge(arr, start, middle, end, reverse)


if __name__ == '__main__':
    test_array = [10, 7, 8, 9, 1, 5]
    merge_sort(test_array, 0, len(test_array) - 1, reverse=True)
    print(test_array)
