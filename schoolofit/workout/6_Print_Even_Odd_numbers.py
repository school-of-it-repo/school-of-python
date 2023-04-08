'''

School of IT - School of Python Series [ for training contact 98403 26240]

Create my_filter_engine method, it should perform all type filter based on input parameter

Input : [1,2,3,4,5,6,7,8,9,10]

for example
    1. Get only odd numbers
    2. Get Only even numbers
    3. Get the number which is divisible by 5
    4. Get the number which is greater than 5

'''

from typing import Callable


def my_filter_engine(_numbers: list[int], _filter: Callable[[int], bool]) -> list[int]:
    return list(filter(_filter, _numbers))


if __name__ == '__main__':
    _input = list(range(1, 11))

    _result = my_filter_engine(_numbers=_input, _filter=lambda a: a % 2 == 0)
    print(_result)
    _result = my_filter_engine(_numbers=_input, _filter=lambda a: a % 2 == 1)
    print(_result)

    _result = my_filter_engine(_numbers=_input, _filter=lambda a: True)
    print(_result)

    # another approach
    _result = my_filter_engine(_numbers=_input, _filter=lambda a: a / 1 == a)
    print(_result)

    _result = my_filter_engine(_numbers=_input, _filter=lambda a: a % 5 == 0)
    print(_result)

    _result = my_filter_engine(_numbers=_input, _filter=lambda a: a > 5)
    print(_result)
