def insertion_sort(arr, reverse=False):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and (key < arr[j]) == reverse:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == '__main__':
    test_array = [10, 7, 8, 9, 1, 5]
    insertion_sort(test_array, reverse=True)
    print(test_array)
