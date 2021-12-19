def selection_sort(arr, reverse=False):
    arr_len = len(arr)

    for i in range(arr_len):
        min_element_index = i
        for j in range(i + 1, arr_len):
            if (arr[min_element_index] > arr[j]) == reverse:
                min_element_index = j
        arr[i], arr[min_element_index] = arr[min_element_index], arr[i]


if __name__ == '__main__':
    test_array = [10, 7, 8, 9, 1, 5]
    selection_sort(test_array, reverse=True)
    print(test_array)
