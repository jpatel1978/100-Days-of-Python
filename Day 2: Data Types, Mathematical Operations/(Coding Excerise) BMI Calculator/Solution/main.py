# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_int = float(height)
weight_int = int(weight)

BMI = weight_int / (height_int * height_int)

BMI_INT = int(BMI)

print(BMI_INT)
