# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi_statement = "Your BMI is "
bmi = weight / height ** 2
if bmi <= 18.5:
  print(f"{bmi_statement}{bmi}. You are underweight")
elif bmi <= 25:
  print(f"{bmi_statement}{bmi}.You have a normal weight")
elif bmi <= 30:
  print(f"{bmi_statement}{bmi}.You are slightly overweight")
elif bmi <= 35:
  print(f"{bmi_statement}{bmi}.You are obese")
else:
  print(f"{bmi_statement}{bmi}.You are clinicaly obese")
