def sort(array):
    if len(array) <= 1:
        return array

    current_position = 0

    for i in range(1, len(array)):
        if sum(array[0]) >= sum(array[i]):
            current_position += 1
            array[i], array[current_position] = array[current_position], array[i]
    array[0], array[current_position] = array[current_position], array[0]

    return [*sort(array[:current_position]),
            array[current_position],
            *sort(array[current_position + 1:])]


def normalize_time(array):
    array = sort(array)
    _array = []
    min_time = array[0][0]
    for i in range(len(array) - 1):
        if array[i][1] >= array[i + 1][0]:
            continue
        _array.append((min_time, array[i][1]))
        min_time = array[i + 1][0]
    _array.append((min_time, array[-1][1]))
    return _array


def pretty_print(array, time_block: int = 30, start_time: int = 540):
    array = normalize_time(array)
    text = "The team will be busy:\n"
    for time in array:
        start = start_time + time[0] * time_block
        end = start_time + time[1] * time_block
        text += f"    {start // 60:02d}:{start % 60:02d} - {end // 60:02d}:{end % 60:02d}\n"
    print(text)


if __name__ == '__main__':
    time_array = [(0, 1), (16, 17), (3, 5), (4, 8), (10, 12), (9, 10), (12, 15)]
    pretty_print(time_array)
