import re


def func(s):
    b = re.sub('\s|,|\.', ':', s)
    return b


s = input()
print(func(s))