'''

Input : 5
Output : 15


'''
def approach_1(n: int) -> int:
    return sum(range(1,n+1))


def approach_2(n: int) -> int:
    _sum = 0
    for i in range(1,n+1):
        _sum += i
    return _sum

def approach_3(n: int) -> int:
    _sum = 0
    while n:
        _sum += n
        n -= 1
    return _sum

# tail recursion option
def approach_4(n: int,_sum:int =0 ) -> int:

    if n==0:
        return _sum
    else:
        return approach_4(n-1, _sum + n)

# Recursion
def approach_5(n: int,_sum:int =0 ) -> int:

    if n==0:
        return 0
    else:
        return n + approach_5(n-1)


if __name__ == '__main__':
    n = 10
    result = approach_1(5)
    print(f'Total sum {result}')

    result = approach_2(10)
    print(f'Total sum {result}')

    result = approach_3(10)
    print(f'Total sum {result}')

    result = approach_4(10)
    print(f'Total sum {result}')

    result = approach_5(10)
    print(f'Total sum {result}')