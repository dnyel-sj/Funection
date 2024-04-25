# برنامه گرفتن عدد صحیح از کاربر و جمع اعداد ان

# تابع جمع اعداد
def sum_digit(a):
    s = 0
    while a > 0:
        s += a % 10
        a //= 10 
    return s
# تابع جدید برای ورودی گرفتن از کاربر
def main():
    num = eval(input( "Enter the int number : "))
    if num < 0 :
        print(f"entered number {num} is negative ")
    else :
        sum_of_gidits = sum_digit(num)
        print(f"sum of number {num} = {sum_of_gidits}")
        
main()