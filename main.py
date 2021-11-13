import re


def get_all_pow(number, str_number):
    return_array = list()
    max_len = len(re.split(r'^0*', str_number)[1])
    square_number = ''
    while len(square_number) <= max_len:
        square_number = bin(number ** len(return_array)).replace('0b', '')
        return_array.append(square_number)
    return return_array[::-1]


def find(number, str_number):
    if number < 0 or number > 100 or len(str_number) > 100:
        return -1
    array_of_pow = get_all_pow(number, str_number)
    count = 0
    while True:
        temp = ''
        for element in array_of_pow:
            if not str_number.find(element):
                temp, count = element, count + 1
                break
        if temp_len := len(temp):
            str_number = str_number[temp_len:]
        else:
            if not len(str_number):
                return count
            return -1


if __name__ == '__main__':
    number_of_iterations = int(input())
    for _ in range(number_of_iterations):
        i_str_number, i_number = [i for i in input().split(' ')][:2]
        print(find(int(i_number), i_str_number))
