def random_int(n):
    if n <= 0:
        return 0
    k = n.bit_length()
    num_bytes = (k + 7) // 8
    while True:
        r = int.from_bytes(random_bytes(num_bytes), 'big')
        r >>= num_bytes * 8 - k
        if r < n:
            return r


def random_bytes(n):
    with open('/dev/urandom', 'rb') as file:
        return file.read(n)


def is_sorted(arr, reverse):
    for i in range(1, len(arr)):
        if (arr[i - 1] > arr[i]) == reverse:
            return False
    return True


def random_sort(arr, reverse=False):
    while not is_sorted(arr, reverse):
        a = random_int(len(arr))
        b = random_int(len(arr))
        arr[a], arr[b] = arr[b], arr[a]


if __name__ == '__main__':
    test_array = [10, 7, 8, 9, 1, 5]
    random_sort(test_array, reverse=True)
    print(test_array)
