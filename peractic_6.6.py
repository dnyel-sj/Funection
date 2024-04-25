# ساخت یک الگو شکلی با اعداد
def display_pattern(n):

# حلقه برای شمردن اعداد تا میزان وارد شده توسط کاربرو چاپ ان   
  for i in range(1, n + 1):
    for j in range(i, 0, -1):
      print(j, end=" ")
    print()

# گرفتن ورودی از کاربر
n = int(input("Yek add vared kn: "))
display_pattern(n)
