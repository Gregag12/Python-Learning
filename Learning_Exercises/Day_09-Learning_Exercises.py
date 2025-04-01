programing_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected.",
    "Function" : "A piece of code that yo ucan easily call over and over again.",
    "Loop" : "The action of doing something over and over again.",
}

# Calls ths Bug key and returns it's value
# print(programing_dictionary["Bug"])

# Adds a new thing to the dictionary
# programing_dictionary["Test"] = "A set of actions to validate something"

# Wipe an existing dictionary -- useful to reset progress, like in a game
# programing_dictionary = {}

# Edit an item in a dictionary
# programing_dictionary["Bug"] = "A moth in your computer"

# Loop through a dictionary
#for key in programing_dictionary:
#    print(key)
#    print(programing_dictionary[key])

# Nested Dictionary

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#travel_log = {
#    "France": ["Paris", "Lille", "Dijon"],
#    "Germany": ["Stuttgart", "Berlin"],
# }

# print Lille
# print(travel_log["France"][1])

# 2D List
nested_list = ["A", "B", ["C", "D"]]
# print(nested_list[2][1])

# Nested dictionary
travel_log = {
    "France": {
        "num_times_visited": 12,
        "cities_visited": ["Paris", "Lille", "Dijon"]
        },
    "Germany": {
        "cities_visited": [ "Berlin", "Hamburg", "Stuttgart"],
        "num_times_visited": 5
        }
}
# Print Stuttgart
print(travel_log["Germany"]["cities_visited"][2])

