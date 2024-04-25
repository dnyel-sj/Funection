# محاسبه جمع اعداد یک عدد صحیح
def sum_digits(n):

# شرط اگر مقدار صفر بود که هیچ وگرنه بیاد با استفاده از عملگر ها اعداد یک عدد صحیح را استخراج کند 
  if n == 0:
    return 0
  else:
    return n % 10 + sum_digits(int(n / 10))

# تعریف تابع جدید برای تعامل با کاربر
def main():

# گرفتن ورودی عدد از کاربر
  number = int(input("Yek add vared kn: "))

# تعریف شرط که عدد وارد شده منفی نباشد و اگر نبود جمع اعداد نمایش دهد
  if number < 0:
    print("Add byd manfi nabashad")
  else:
    sum_of_digits = sum_digits(number)
    print(f"Jame adad {number} barabar ba {sum_of_digits} ast.")

# برای اجرای برنامه استفاده میشود
if __name__ == "__main__":
  main()
