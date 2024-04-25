# مرتب سازی اعداد به ترتیب از صعودی
def display_sorted_numbers(num1, num2, num3):

# مرتب سازی اعداد
  sorted_numbers = sorted([num1, num2, num3])

# نمایش اعداد مرتب شده
  print("Adad moratab shode", sorted_numbers)

# دریافت اعداد از کاربر
num1 = eval(input("Add aval vared kn: "))
num2 = eval(input("Add dovom vared kn: "))
num3 = eval(input("Add sevom vared kn: "))

# نمایش اعداد مرتب شده
display_sorted_numbers(num1, num2, num3)
