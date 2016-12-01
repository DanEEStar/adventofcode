import ctypes
import re
import json
import numbers
from copy import deepcopy


def rec_sum_numbers(json_dict):
    if isinstance(json_dict, numbers.Number):
        return json_dict
    elif isinstance(json_dict, dict) and not 'red' in json_dict.values():
        return sum(map(rec_sum_numbers, json_dict.values()))
    elif isinstance(json_dict, list):
        return sum(map(rec_sum_numbers, json_dict))
    return 0


def main():
    with open('input.txt') as input:
        input = json.loads(input.read())
        #input = json.loads('[1,"red",5]')
        print(input)
        print(rec_sum_numbers(input))


if __name__ == '__main__':
    main()

