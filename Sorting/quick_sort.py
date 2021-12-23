def partition(arr, start, end, reverse):
    pivot = arr[end]
    pivot_index = start-1

    for i in range(start, end):
        if (arr[i] < pivot) == reverse:
            pivot_index += 1
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
    arr[pivot_index+1], arr[end] = arr[end], arr[pivot_index+1]

    return pivot_index+1


def quick_sort(arr, start, end, reverse=False):
    if start >= end:
        return
    partition_index = partition(arr, start, end, reverse)
    quick_sort(arr, start, partition_index-1, reverse)
    quick_sort(arr, partition_index+1, end, reverse)


if __name__ == '__main__':
    test_array = [10, 7, 8, 9, 1, 5]
    quick_sort(test_array, 0, len(test_array)-1, reverse=True)
    print(test_array)
