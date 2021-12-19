def heapify(arr, arr_len, i, reverse):
    biggest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < arr_len and (arr[biggest] < arr[left]) == reverse:
        biggest = left

    if right < arr_len and (arr[biggest] < arr[right]) == reverse:
        biggest = right

    if biggest != i:
        arr[i], arr[biggest] = arr[biggest], arr[i]
        heapify(arr, arr_len, biggest, reverse)


def heap_sort(arr, reverse=False):
    arr_len = len(arr)

    for i in range(arr_len//2-1, -1, -1):
        heapify(arr, arr_len, i, reverse)

    for i in range(arr_len-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, reverse)


if __name__ == '__main__':
    test_array = [10, 7, 8, 9, 1, 5]
    heap_sort(test_array, reverse=True)
    print(test_array)
