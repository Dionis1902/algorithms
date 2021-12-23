def bubble_sort(arr, reverse=False):
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if (arr[j] < arr[j-1]) == reverse:
                arr[j-1], arr[j] = arr[j], arr[j-1]


if __name__ == '__main__':
    test_array = [10, 7, 8, 9, 1, 5]
    bubble_sort(test_array, reverse=True)
    print(test_array)
