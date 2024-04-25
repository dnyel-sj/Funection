# نشان دادن معکوس عدد وارد شده توسط کاربر
def reverse_number(n):
  
# تعریف متغیر جدید
  reversed_num = 0

# استفاده از حلقه برای استخراج اعداد و معکوس کردن ان
  while n > 0:

    remainder = n % 10
    reversed_num = (reversed_num * 10) + remainder
    n //= 10

  return reversed_num

# دریافت عدد از کاربر
number = int(input("Yek add vared konid: "))

# معکوس شده عدد داخل متغییر
reversed_number = reverse_number(number)

# نمایش عدد معکوس شده
print(f"Add makos shode: {reversed_number}")
