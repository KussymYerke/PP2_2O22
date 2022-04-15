from re import sub
def func(s):
  return '_'.join(
    sub('([A-Z][a-z]+)', r' \1',sub('([A-Z]+)', r' \1',s.replace('-', ' '))).split()).lower()

s = input()
print(func(s))