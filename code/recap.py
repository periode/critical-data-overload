name = "sam" # this is a type string
age = 23 # this is a type number (integers, 34, 2, -4) or (floating points 2.4, 4.56)
is_enrolled = True # this is a type boolean (true or false)


favorite_books = [
    {"title": "dune", "lang": "en"},
    {"title": "西遊記", "lang": "zh"},
    {"title": "MINIMA MORALIA", "lang": "de"}
]

# for every book in the list of favorite_books, do the following...
for book in favorite_books:
    if book["lang"] == "zh": # check if the language is equal to 'zh'
        print(f"i like to read {book["title"]}")
    else:
        print("nope")

# this way of representing data is called JSON
# python also calls this a "dictionary"
book = {
    "title": "dune", # a key-value pair
    "lang": "en",
    "characters": { # an object inside an object
        "main": {
            "birth_name": "paul atreides",
            "war_name": "muad'dib"
        },
        "secondary": [ # a list inside an object
            "duke leto",
            "worm",
            "alia"
        ]
    }
}
print(book['characters']['main']['war_name'])

# "return" is the result of a function
# this function checks if a given password is the correct one
def check_password(password):
    if password == "1234":
        return "yep you're in!"
    else:
        return "heute leider nicht"


result_of_password_check = check_password("0000")

print(f"the password is correct? {result_of_password_check}")


