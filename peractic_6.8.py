# برنامه نوشتن تبدیلات سانتی به فارانهایت و بالعکس

# تابع مربوط به تبدیل فارانهایت به سانتی
def fahrenheit_to_centigrade(fahrenheit):
    
# فرمول تبدیل فارانهایت به سانتی    
    return (fahrenheit - 32) * 5/9

# تابع مربوط به تبدیل سانتی به فارانهایت
def centigrade_to_fahrenheit(centigrade):

# فرمول تبدیل سانتی به فارانهایت    
    return (centigrade * 9/5) + 32

# لیست اعداد به فارانهایت
fahrenheit_temps = [100.0, 90.0, 80.0, 70.0, 60.0, 50.0, 40.0, 30.0]

# تبدیل فارانهایت به سانتی
centigrade_temps = []
for temp in fahrenheit_temps:
    centigrade_temps.append(fahrenheit_to_centigrade(temp))

# چاپ جدول از فارانهایت به سانتی
print("Fahrenheit\tCentigrade")
for i in range(len(fahrenheit_temps)):
    print(f"{fahrenheit_temps[i]}       \t{centigrade_temps[i]}")

# لیست درجه های سانتی گراد
centigrade_temps = [40.0, 39.0, 38.0, 37.0, 36.0, 35.0, 34.0, 33.0, 32.0, 31.0]

# تبدیل سانتی به فارانهایت
fahrenheit_temps = []
for temp in centigrade_temps:
    fahrenheit_temps.append(centigrade_to_fahrenheit(temp))

# چاپ جدول
print("\nCentigrade\tFahrenheit")
for i in range(len(centigrade_temps)):
    print(f"{centigrade_temps[i]}       \t{fahrenheit_temps[i]}")