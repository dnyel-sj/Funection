# نوشتن اعدا 5 ضلعی با استفاده از فرمول مربوطه
def get_pentagonal_number(n):
# یک عدد طبیعی مثبت است n 

# فرمول یافتن اعدا 5 ضلعی
  return n * (3 * n - 1) // 2

# تابع جدید برای نمایش اعداد بدست امده بصورت 10 تایی در هر خط
def display_pentagonal_numbers(start, end, per_row=10):
  
#start: اولین عدد پنج ضلعی برای نمایش
#end: آخرین عدد پنج ضلعی برای نمایش
#per_row: تعداد اعداد پنج ضلعی در هر خط

# حلقه برای شمارش اعداد 5 ضلعی که در هر خط 10 تا چاپ شود  
  count = 0
  for n in range(start, end +1):
    number = get_pentagonal_number(n)
    count += 1
    print(number,end=" ")
    if count % per_row == 0:
      print()

display_pentagonal_numbers(1, 100) 
