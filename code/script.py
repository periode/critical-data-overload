# variables - states
name = "pierre" # type string
height = 185 # type number
activities = ["walk", "breathe", "eat", "talk", "write", "joke", "hike", "webscrape", "read"] # type list
print("hello, " + name)

# for loop
# for each activity in the list activities do...
for activity in activities:
    print("i really like to "+activity)
    
# conditional statements
# if kind_of_rain is drizzle:
#   do stuff
# else if kind_of_rain is pouring:
#   do this instead
# else:
#   do other stuff

have_to_go_out = True
kind_of_rain = "pouring"

if (have_to_go_out is True) and (kind_of_rain == "drizzle"):
    print("we take a rain jacket")
elif have_to_go_out is True and kind_of_rain == "pouring":
    print("take umbrella")
elif have_to_go_out is True:
    print("walk out")

# functions - actions
# title
# ingredients
# instructions
def greet_person(name):
    print("hello, "+name)
