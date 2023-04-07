'''

Input = [
        'apple'
        , 'orange'
        , 'apple'
        , 'bannana'
        , 'gauva'
        , 'apple'
        , 'orange'
        , 'apple'
        , 'bannana'
        , 'apple'
        , 'orange'
    ]
Output : [{'apple': 5}, {'bannana': 2}, {'gauva': 1}, {'orange': 3}]


'''

import itertools
if __name__ == '__main__':
    fruits = [
        'apple'
        , 'orange'
        , 'apple'
        , 'bannana'
        , 'gauva'
        , 'apple'
        , 'orange'
        , 'apple'
        , 'bannana'
        , 'apple'
        , 'orange'
    ]

    result  =[
        {fruit : len(list(_list_of_fruits))}
     for fruit,_list_of_fruits in itertools.groupby(sorted(fruits))
    ]

    print(result)
