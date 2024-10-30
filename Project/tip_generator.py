# This is a welcome statement
welcome_statement = "Welcome to the tip calculator."
# this function asks the user what they bill is and saves it as a string
original_total_bill = input("What was the total bill?\n")
# this function converts the original_total_bill string into a float number and removes any $ sign that might be present
total_bill_float = float(original_total_bill.replace('$',''))
# this function asks the user what they tipped and saves it as a string
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15?\n")
# this function converts the tip number into a percentage 
converted_tip = int(percentage_tip) / 100
# this function multiplies the tip percentage with the total and saves the values
tip_amount = round(total_bill_float * float(converted_tip), 2)
# this function asks the user how many people are splitting the bill and saves it as a string
number_people = input("How many people are there to split the bill?\n")
# this function calculated the amount each person has to pay and rounds it to the nearest cent
amount_per_person = round((float(total_bill_float) + tip_amount) / int(number_people), 2)
#formats the final amount to use 2 decimal places when the calcuated response returns an answer that only goes to one decimal place
final_amount = "{:.2f}".format(amount_per_person)
print(f"Each person should pay: ${final_amount}")
