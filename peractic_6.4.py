# برنامه بررسی اینکه یک عدد پالیندروم است یا خیر

# تابع برای تشخیص درست یا غلط بودن پالیندروم

def is_palindrome(num):

# تبدیل عدد به لیست ارقام
  digits = [int(d) for d in num]

# بررسی اینکه آیا ارقام در دو انتهای رشته برابر هستند
  for i in range(len(digits) // 2):
    if digits[i] != digits[~i]:
      return False

  return True

# تابع اصلی برای گرفتن ورودی و بررسی عدد
def main():

  num = input("Yek add vared kn: ")

  if is_palindrome(num):
    print(f"{num} Add palindrome ast!")
  else:
    print(f"{num} Add palindrome nist!")

if __name__ == "__main__":
  main()
