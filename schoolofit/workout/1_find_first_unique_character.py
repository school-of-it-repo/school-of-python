import collections
import re


def text_cleanup(sen: str) -> str:
    _cleaned_text = re.sub('[^A-Za-z0-9]+', '', sen)
    return _cleaned_text.lower()

def approach_1(text:str) -> str :
    counter = dict(collections.Counter(text).items())
    res = min(counter, key=counter.get)
    return res

def approach_2(text:str) -> str :
    res = { _ch:text.count(_ch) for _ch in text}
    return min(res,key=res.get)

def approach_3(text:str) -> str :
    counter = collections.Counter(text)
    for _index,_ch in enumerate(text):
        if text.count(_ch) == 1:
            return _ch


if __name__ == '__main__':
    print('welcome to school of IT')
    sentences = ('Python is a high-level, '
                 'general-purpose programming language. '
                 'Its design philosophy emphasizes code readability with the use of significant '
                 'indentation via the off-side rule. Python is dynamically typed and garbage-collected')
    cleaned_text = text_cleanup(sentences)
    result = approach_1(cleaned_text)
    print(f'The first unique character is {result}')

    result = approach_2(cleaned_text)
    print(f'The first unique character is {result}')

    result = approach_3(cleaned_text)
    print(f'The first unique character is {result}')
