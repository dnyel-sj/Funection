# برنامه چاپ حروف یا کارکتر ای تا زد

# تابع کارکتر
def printChars(ch1, ch2, n):

  i = ord(ch1)
  while i <= ord(ch2):
    ch = chr(i)
    print(ch, end=' ')
    i += 1
    if i % n == 0:
      print()

# خروجی برنامه
printChars('a', 'z', 10)
