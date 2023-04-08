'''

School of IT - School of Python Series [ for training contact 98403 26240]

Input = do_print_hai_bye(4)
Output = Hai,Bye,Hai,BYE  # Last word should be upper-case

Input = do_print_hai_bye(2)
Output = Hai,BYE  # Last word should be upper-case

Input = do_print_hai_bye(1)
Output = HAI  # Last word should be upper-case

Input = do_print_hai_bye(0)
Output = None
'''

def do_print_hai_bye(n: int) -> str:
    _result = [
        'Hai' if i % 2 == 0 else 'Bye'
        for i in range(n)

    ]

    if _result:
        _result[-1] = _result[-1].upper()
        return ','.join(_result)
    return None


if __name__ == '__main__':
    print(do_print_hai_bye(4))
    print(do_print_hai_bye(1))
    print(do_print_hai_bye(0))
