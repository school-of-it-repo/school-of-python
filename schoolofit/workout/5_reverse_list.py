def approach_1(_numbers: list[int]) -> list[int]:
    return list(reversed(_numbers))


def approach_2(_numbers: list[int]) -> list[int]:
    return _numbers[::-1]


def approach_3(_numbers: list[int]) -> list[int]:
    _list = []
    for _number in _numbers:
        _list = [_number] + _list
    return _list


def approach_4(_numbers: list[int]) -> list[int]:
    _list = []
    for _number in _numbers:
        _list.insert(0, _number)
    return _list


# using tail recursion
def approach_5(_numbers: list[int], _reverse_list: list[int] = []) -> list[int]:
    if not _numbers:
        return _reverse_list
    else:
        _reverse_list.insert(0, _numbers[0])
        return approach_5(_numbers[1:], _reverse_list)


# using recursion
def approach_6(_numbers: list[int]) -> list[int]:
    if not _numbers:
        return _numbers
    else:
        return approach_6(_numbers[1:]) + [_numbers[0]]


if __name__ == '__main__':
    n = list(range(1, 11))
    # print(n)
    result = approach_1(n)
    print(result)
    result = approach_2(n)
    print(result)
    result = approach_3(n)
    print(result)
    result = approach_4(n)
    print(result)
    result = approach_5(n)
    print(result)

    result = approach_6(n)
    print(result)
