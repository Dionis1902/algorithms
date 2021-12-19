def partition(arr, start, end):
    pivot = arr[end]
    pivot_index = start-1
    for i in range(start, end):
        if arr[i] < pivot:
            pivot_index += 1
            arr[pivot_index], arr[i] = arr[i], arr[pivot_index]
    arr[pivot_index+1], arr[end] = arr[end], arr[pivot_index+1]
    return pivot_index+1


def quick_sort(arr, start, end):
    if start > end:
        return
    partition_index = partition(arr, start, end)
    quick_sort(arr, start, partition_index-1)
    quick_sort(arr, partition_index+1, end)


if __name__ == '__main__':
    test_array = [10, 7, 8, 9, 1, 5]
    quick_sort(test_array, 0, len(test_array)-1)
    print(test_array)
