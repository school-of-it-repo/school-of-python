import collections
import re


def text_cleanup(sen: str) -> str:
    _cleaned_text = re.sub('[^A-Za-z0-9]+', '', sen)
    return _cleaned_text.lower()


if __name__ == '__main__':
    print('welcome to school of IT')
    sentences = ('Python is a high-level, '
                 'general-purpose programming language. '
                 'Its design philosophy emphasizes code readability with the use of significant '
                 'indentation via the off-side rule. Python is dynamically typed and garbage-collected')
    cleaned_text = text_cleanup(sentences)
    counter = dict(collections.Counter(cleaned_text).items())
    res = min(counter, key=counter.get)
    print(f'The first unique character is {res}')
