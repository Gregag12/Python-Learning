print("The Love Calculator is calculating your score...")
name1 = input() # What is your name?
name2 = input() # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇
combined_names = name1.lower() + name2.lower()
number_of_t = combined_names.count("t",0) 
number_of_r = combined_names.count("r",0)
number_of_u = combined_names.count("u",0)
number_of_e = combined_names.count("e",0)
number_of_l = combined_names.count("l",0)
number_of_o = combined_names.count("o",0)
number_of_v = combined_names.count("v",0)
number_of_e = combined_names.count("e",0)
true = str(number_of_t + number_of_r + number_of_u + number_of_e)
love = str(number_of_l + number_of_o + number_of_v + number_of_e)
love_score = int(true + love)
if (love_score < 10) or (love_score > 90):
    print (f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}")
