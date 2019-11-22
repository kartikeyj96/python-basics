def addition(value):
    total = 0
    value = [1, 2, 4, 5, 7, 7]
    for sum in value:
        total += sum
    return total


def find_max(values):
    max = values[0]
    for digit in values:
        if digit > max:
            max = digit
    return max


print("------------------------------------------------------------------------------------------------------------")
# ADVANCE STRINGS

sentance = "This is a sentance"
print(sentance[-1])
print(sentance[-9:-2])
sentance_split = sentance.split()

sentance_join = ' '.join(sentance_split)
print(sentance_join)
print('\n'.join(sentance_split))

print('A' in 'Apple')  # BOOLEAN
letter = 'a'
word = "Apple"
print(letter.upper() in word)

word_two = "Bingo"
print((letter.lower() in word.lower()) and not (letter.lower()))
word_two.lower()

too_much_space = "         hello"
print(too_much_space.strip())  # STRIPS OFF THE SPACE

full_name = "Ishu Jain"
print(full_name.replace("Ishu", "Kartikey"))
print(full_name.find("Jain"))

movie = "John Wick"
print(f"My favorite movie is: {movie}")
print("My favorite movie is {}.".format(movie))  # PLACE HOLDERS


def favorite_book(title, author):
    fav = "My favorite book is \"{}\", which is written by {}.".format(title, author)  # PLACE HOLDERS
    return fav


print(favorite_book("Physics", "H.C Verma"))

# DICTIONARIES
drinks = {"White Russian:7",
          "Old Fashion:10",
          "Lemon Drop:8",
          "Buttery Nipple:12"
          }  # DRINKS ARE THE KEYS AND PRICE IS VALUE
print(drinks)

movies = ["Dark Knight Rises ", "Avengers End Game", "Dark Knight"]
person = ["kJ", "TJ", "GJ"]
combined = zip(movies, person)
movie_dictionary = {key: value for key, value in combined}  # MAKE A DICTIONARY USING LIST
print(movie_dictionary)

