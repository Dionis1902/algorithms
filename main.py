import datetime
import getopt
import random
import sys

count, swaps = 0, 0


def quick_sort(array: list[int], ascending: bool = True) -> list[int]:
    """
    :param array: array of integers
    :param ascending: True for ascending and False for descending
    :return: sorted array
    """

    global count, swaps
    if len(array) <= 1:
        return array

    current_position = 0

    for i in range(1, len(array)):
        count += 1
        if (array[i] <= array[0] and ascending) or (array[i] >= array[0] and not ascending):
            current_position += 1
            swaps += 1
            array[i], array[current_position] = array[current_position], array[i]
    array[0], array[current_position] = array[current_position], array[0]

    return [*quick_sort(array[:current_position], ascending),
            array[current_position],
            *quick_sort(array[current_position + 1:], ascending)]


def random_array(number_of_elements: int, min_value: int = -100, max_value: int = 100) -> list[int]:
    """
    :param number_of_elements: number of elements in array
    :param min_value: minimum value of element
    :param max_value: maximum value of element
    :return: array of random integers
    """
    return [random.randint(min_value, max_value) for i in range(number_of_elements)]


def main(argv):
    _array_for_sort, _ascending = [], None
    try:
        opts, args = getopt.getopt(argv, "ha:o:r:", ["array=", "order=", "random="])
    except getopt.GetoptError:
        print('main.py -a <int array> or -r <number of elements> -o <asc/desc>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -a <int array> or -r <number of elements> -o <asc/desc>')
            sys.exit(2)
        if opt in ("-a", "--array"):
            try:
                _array_for_sort = [int(i) for i in arg.split(',') if i]
            except ValueError:
                print('main.py -a <int array> or -r <number of elements> -o <asc/desc>')
                sys.exit(2)
        if opt in ("-o", "--order"):
            if arg in ('asc', 'desc'):
                _ascending = True if arg == 'asc' else False
            else:
                print('main.py -a <int array> or -r <number of elements> -o <asc/desc>')
                sys.exit(2)
        if opt in ("-r", "--random"):
            try:
                number_of_elements = int(arg)
                if number_of_elements > 0:
                    _array_for_sort = random_array(number_of_elements)
                else:
                    print('main.py -a <int array> or -r <number of elements> -o <asc/desc>')
                    sys.exit(2)
            except ValueError:
                print('main.py -a <int array> or -r <number of elements> -o <asc/desc>')
                sys.exit(2)
    if not _array_for_sort or _ascending is None:
        print('main.py -a <int array> or -r <number of elements> -o <asc/desc>')
        sys.exit(2)
    return _array_for_sort, _ascending


if __name__ == '__main__':
    array_for_sort, ascending = main(sys.argv[1:])

    start = datetime.datetime.now()
    sorted_array = quick_sort(array_for_sort, ascending)
    execution_time = datetime.datetime.now() - start
    print("QuickSort:\n"
          f"Execution time: {execution_time.total_seconds() * 1000:.2f} MS\n"
          f"Comparisons: {count}\n"
          f"Swaps: {swaps}\n"
          f"{sorted_array}")
