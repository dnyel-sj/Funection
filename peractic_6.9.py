# Function to convert meters to feet
def convert_meters_to_feet(meters):
    feet = meters * 3.28084
    return feet

# Function to convert feet to meters
def convert_feet_to_meters(feet):
    meters = feet / 3.28084
    return meters

Metr_temp = [100.0, 90.0, 80.0, 70.0, 60.0, 50.0, 40.0, 30.0]

# تبدیل فارانهایت به سانتی
foot_temp = []
for temp in Metr_temp:
    foot_temp.append(convert_meters_to_feet(temp))

# چاپ جدول از فارانهایت به سانتی
print("METR\tFOOT")
for i in range(len(Metr_temp)):
    print(f"{Metr_temp[i]}\t{foot_temp[i]}")

foot_temp = [40.0, 39.0, 38.0, 37.0, 36.0, 35.0, 34.0, 33.0, 32.0, 31.0]

# تبدیل سانتی به فارانهایت
Metr_temp = []
for temp in foot_temp:
    Metr_temp.append(convert_feet_to_meters(temp))

# چاپ جدول
print("\nFOOT\tMETR")
for i in range(len(foot_temp)):
    print(f"{foot_temp[i]}\t{Metr_temp[i]}")
