# Functions
# def my_function():
#   Do this
#   Then do this
#   Finally do this

# Functions with Inputs 
# def my_function(something):
#   Do this with something
#   Then do this
#   Finally do this

# Functions with Outputs
# def my_function():
#   result = 3 *3
#   return result

def format_name(f_name, l_name):
    """Take a first and last name and format it to return
        the title case version of the name."""
    if f_name == "" or l_name == "":
        return "You did not provide valid inputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"Result: {formated_f_name} {formated_l_name}"

# formated_string = format_name(f_name="GreG", l_name="GARRett")
print(format_name(input("What is your first name?"), input("What is your last name?")))

def function_1(text):
    return text + text

def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)

