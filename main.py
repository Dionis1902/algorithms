import re


def get_all_pow(number, str_number):
    return_array = []
    max_len = len(re.split(r'^0*', str_number)[1])
    square_number = ''
    while len(square_number) <= max_len:
        square_number = bin(number ** len(return_array)).replace('0b', '')
        return_array.append(square_number)
    return return_array


def find(number, str_number):
    if number < 0 or number > 100 or len(str_number) > 100:
        return -1
    array_of_pow = get_all_pow(number, str_number)[::-1]
    i = 0
    while True:
        temp = ''
        for element in array_of_pow:
            if not str_number.find(element):
                temp, i = element, i + 1
                break
        if len(temp):
            str_number = str_number[len(temp):]
        else:
            if not len(str_number):
                return i
            return -1


if __name__ == '__main__':
    count = int(input())
    for _ in range(count):
        i_str_number, i_number = [i for i in input().split(' ')][:2]
        print(find(int(i_number), i_str_number))
