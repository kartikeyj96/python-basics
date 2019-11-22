# !/bin/python3

# PRINT STRINGS

print("strings and things")
print('SYNTAX: STRINGS/.')
print("---------MISSION ABORT-----------")
print("---------MALFUNCTION-------------")
print("this is" + "NOTHING")

print('\n')  # NEW LINE

# MATHS
print("MATHS TIME:")
print(40 + 90)
print(90 - 40)
print(50 * 50)
print(50 ** 2)  # EXPONENT
print(50 / 40)
print(50 % 2)  # MODULO
print(50 // 6)  # NUMBER WITHOUT LEFOVERS

print('\n')  # NEW LINE

# VARIABLES

print("FUN WITH VARIABLES")
quote = "MY NAME IS KARTIKEY JAIN"
print(len(quote))  # LENGTH
print(quote.lower())  # LOWERCASE
print(quote.upper())  # UPPERCASE
print(quote.title())  # TITLE (FIRST LETTER WILL BE IN UPPERCASE)

print('\n')  # NEW LINE

name = "kartikey"
age = 18  # int int(18)
cgpa = 9.2  # float float(9.2)

print(int(age))
print(float(cgpa))
print(int(cgpa))
print(" My name is " + name + " and im " + str(age) + " years old ")

# str is use because age cannot be printed in string

print('\n')
age += 1
print(age)
birthday = 1
age += birthday
print(age)

# FUNCTIONS

print("ITS TIME FOR FUNCTIONS:")


def func():
    name = "KARTIKEY"
    age = 19
    print(" My name is " + name + " and im " + str(age) + " years old ")


func()


# ADDING IN PARAMETER

def add_one_parameter(num):
    print(num + 100)


add_one_parameter(100)


# ADDING MULTIPLE PARAMETER

def add(x, y):
    print(x + y)
    print(x - y)
    print(x * y)


add(7, 7)
add(500, 500)


# USING RETURN
def multiply(x, y):
    return x * y


print(multiply(7, 7))


def expo(x, y):
    return x ** y


print(expo(4, 4))


def square_root(x):
    return x ** 0.5


print(square_root(25))
print('\n')

# BOOLEAN EXPRESSIONS(TRUE AND FALSE)

print("BOOLEANS EXPRESSIONS:")
bool1 = True
bool2 = 3 * 3 == 9
bool3 = False
bool4 = 3 * 3 != 9

print(bool1, bool2, bool3, bool4)
print(type(bool1))

bool5 = "True"
print(type(bool5))

# RELATIONAL AND BOOLEAN OPERATIONS
print("RELATIONAL AND BOOLEAN OPERATIONS:")

greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >= 7
less_than_equal_to = 7 <= 7

print(greater_than, less_than, greater_than_equal_to, less_than_equal_to)

test_and = (7 > 5) and (6 < 7)
test_or = (7 > 5) or (5 < 7)
test_not = not True

print(test_and)
print(test_or)
print(test_not)
print('\n')

# CONDITIONAL STATEMENTS

print("CONDITIONAL STATEMENTS:")


def soda(money):
    if money >= 2:
        return "Take your Soda"
    else:
        return "Go and get some money!"


print(soda(3))
print(soda(1))


def alcohol(age, money):
    if (age >= 18) and (money >= 5):
        return "KAM DAARU PIYA KER"
    elif (age >= 18) and (money < 5):
        return " TERI AUKAAT NHI HAI "
    elif (age < 18) and (money >= 5):
        return "BADA HOJA AMIR KE LADKE"
    else:
        return "KAHA RAAJA BHOJ KAHA GANGUTELI"


print(alcohol(18, 5))
print(alcohol(18, 4))
print(alcohol(17, 5))
print(alcohol(17, 4))
print('\n')

# LIST
print("LIST HAS [BRACKETS] AND CAN BE MODIFIED")
movies = ["Dark Knight Rises ", "Avengers End Game", "Dark Knight"]
print(movies[0])
print(movies[1])
print(movies[0:2])  # movies calls from 0 to 1 (2 is not included)
print(movies[1:])  # all the movies printed from 1 to last (1 is the second one)
print(movies[:1])  # agar kuch nhi likha hua hai startimg mai toh vo 0 by default hota hai
print(movies[-1])  # -1 ka mtlb last item print hoga list ka
print(len(movies))  # LEN total items count kerta hai list ka

movies.append("Joker")  # use to add the item in the list
print(movies)

movies.pop()  # by default last item will be removed
print(movies)

movies.pop(1)  # avengers will be deleted
print(movies)

movies = ["Dark Knight Rises ", "Avengers End Game", "Dark Knight"]
person = ["kJ", "TJ", "GJ"]

combined = zip(movies, person)  # use to merge the list to the corresponding items (pairs)
print(list(combined))

# TUPLES
print("TUPLES HAVE PARENTHESIS AND CANNOT CHANGE")
grades = ("A", "B", "C", "D")
print(grades[1])

# LOOPING

print("FOR LOOPS - START TO FINISH Of ITERATE:")
vegetables = ["cucumber", "SPINACH", "OKRA"]

for x in vegetables:
    print(x)
print('\n')

print("WHILE LOOPS-EXECUTE AS LONG AS TRUE")
i = 1
while i < 10:
    print(i)
    i += 1

first = 'John'
last = 'Smith'
message = f'{first} [{last}] is a coder'
print(message)

course = 'PYTHON FOR BEGINNERS'
print(len(course))
print(course.lower())
print(course.find('P'))  # GIVES THE INDEX OF THE CHARACTER
print(course.find('BEGINNERS'))
print(course.replace('BEGINNERS', 'ABSOLUTE BEGINNERS'))  # USE TO REPLACE THE STRINGS
print("PYTHON" in course)  # USE TO CHECK THE STRINGS EXISTENCE BASED ON BOOLEAN(T/F)

# weight_in_lbs=input('weight_in_lbs: ')
# weight_in_kgs=int(weight_in_lbs)*0.45
# print(weight_in_kgs)


x = 2.34
print(round(x))  # USE FOR ESTIMATION

is_hot = True
is_cold = False

if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear Warm clothes")
else:
    print("It's a lovely day")

print("----------------------------------------------------------------------")

has_good_credit = True

price = 1000000

if has_good_credit:
    down_payment = (0.1) * price
    print(f"DOWN PAYMENT: ${down_payment}")

else:
    down_payment = (0.2) * price
    print(f"DOWN PAYMENT: ${down_payment}")

print("------------------------------------------------------------------------")

# temp = int(input("ENTER THE TEMP VALUE: "))

# if temp >= 30:
# print("IT's A HOT DAY")
# elif temp <= 10:
# print("IT'S A COLD DAY")
# else:
# print("IT'S NEITHER HOT NOR COLD")

print("--------------------------------------------------------------------")

char = "KARTIKEY"

if len(char) < 3:
    print("Name must be at least 3 characters")
elif len(name) > 50:
    print("Name must be of maximum 50 characters")
else:
    print("Name looks good")

print("-------------------------------------------------------------------")

# weight = int(input('Weight: '))
# unit = input('(L)bs or (K)g: ')
# if unit.upper() == "L":
# converted=weight * 0.45
# print(f"You are {converted} kilos")
# else:
# converted = weight / 0.45
# print(f"You are {converted} pounds")

print("-----------------------------------------------------------------------")

i = 1
while i <= 5:
    print('$' * i)
    i += 1
print("Done")

for item in range(10):  # 0 to 9
    print(item)
print('\n')
print("-----------------------------------------------------------------------")
for item in range(5, 10):  # PRINT THE NUMBERS FROM 5 TO 10(NOT INCLUDE 10)
    print(item)
print('\n')
print("-----------------------------------------------------------------------")
for item in range(5, 10, 2):  # PRINT THE NUMBERS FROM 5 TO 10 IN THE GAP OF 2
    print(item)

prices = [10, 20, 30]
sum = 0
for price in prices:
    sum += price
print(f"Sum: {sum}")

# PRINT COMBINATIONS OF COORDINATES

for x in range(4):
    for y in range(3):
        print(f"({x}, {y})")

print("-----------------------------------------------------------------------")

numbers = [1, 1, 1, 1, 5]
for x in numbers:
    output = ""
    for count in range(x):
        output += 'x'
    print(output)

num = [2, 3, 4, 5]
max = num[0]
for number in num:
    if number > max:
        max = number
print(f"The largest number in the list: {max}")

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])
print(matrix[0][1])

num = [1, 1, 2, 3, 4, 5, 6]
num.append(20)  # USE TO ADD AN ITEM IN THE LIST
print(num)

num.insert(0, 10)  # USE TO ADD AN ITEM IN B/W THE LIST BY GIVING THE INDEX NUMBER
print(num)

num.remove(10)  # USE TO REMOVE THE ITEM BY PASSING IT IN FUNCTION
print(num)

num.pop()  # USE TO REMOVE THE LAST ITEM FROM THE LIST
print(num)

print(num.index(1))  # USE TO TELL THE INDEX VALUE OF AN ITEM
print(50 in num)  # USE TO TELL THE PRESENCE OF AN ITEM IN THE LIST
print(num.count(1))  # USE THE COUNT THE NO.OF 1 IN THE LIST

num.sort()  # USE THE SORT THE LIST IN ASENDING ORDER
print(num)
numbers.reverse()  # USE THE SORT THE LIST IN DESENDING ORDER
print(num)

num2 = num.copy()  # USE TO COPY TH ITEM OF THE LIST IN THE NEW LIST
print(num2)

print('-------------------------------------------------------------------------')

list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
for x in list:
    if list.count(x) > 1:
        list.remove(x)
print(list)

# OR

list = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
unique = []
for number in list:
    if number not in unique:
        unique.append(number)
print(unique)

coordinates = (1, 2, 3)
x, y, z = coordinates  # x=coordinates[0],y=coordinates[1],z=coordinates[2]
print(x)
print(y)
print(z)
print("-----------------------------------------------------------------------")
# DICTIONARIES(CASE SENSITIVE)

customer = {
    "name": "Kartikey",
    "age": 18,
    "is verified": True
}
print(customer["name"])  # PRINT THE NAME
print(customer.get("name"))  # USING GET FUNCTION(BETTER PRACTICE)
print(customer.get("birthdate", "March 2001"))
customer["name"] = "ISHU"  # CHANGE THE NAME
print(customer["name"])

print("-------------------------------------------------------------------------------")

# USING SPLIT() FUNCTION
# ILLUSTRATION
# message = input(">")
# words = message.split(' ') # SPLIT THR LINE FROM SPACES AND MAKE A LIST OF IT
# print(words)
print("-------------------------------------------------------------------------")


# FUNCTIONS (BY DEFAULT THE FUNCTION RETURN NONE VALUE)

def greet_user(first_name, last_name):  # PASSING PARAMETERS
    print(f"Hi {first_name} {last_name}")
    print("Welcome")


print("Start")
greet_user("Gauri", "Jain")  # POSITION OF ARGUMENTS
# greet_user("Jain", first_name= "Kartikey") # KEYWORDS OF ARGUMENTS
# POSTION ARGUMENTS HAS MORE PRIORITY THEN KEYWORD ARGUMENTS
print("Finish")

print("------------------------------------------------------------------------------")

# TRY AND EXCEPT FUNCTIONS (USE TO HANDLE THE ERRORS AND PREVENT FROM CRASHING OF PROGRAM

# try:
#   age= int(input("Age: "))
#  income = 20000
# risk = income/age # IF WE INPUT AGE AS 0 AUR PROGRAM SHOULD GIVE A ZERO DIVISON ERROR
# print(f"Your age is: {age} years")
# print(f"Your risk is: {risk}")
# except ZeroDivisionError: # NAME OF THE ERROR,THIS WILL PREVENT THE PROGRAM FROM CRASHING AND PRINT THE MSG INSTEAD
#   print("Age cannot be 0")
# except ValueError:
#   print("age can be in numerics only")

print("-----------------------------------------------------------------------------")


# CLASSES ( UNDERSCORE IN NOT USE TO SEPERATE TWO WORDS )
#         ( FIRST LETTER IS CAPATALIZED TO SEPERATE WORDS )

class Point:
    def __init__(self, x):  # CONSTRUCTOR INTIALIZATION
        self.x = x

    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point(20)  # CREATE AN OBJECT POINT1 IN CLASS POINT
# WE PASSES THE VALUE 20 IN CONSTRUCTOR
point1.x = 10  # X AND Y ARE ATTRIBUTES  X UPDATED TO 10
point1.y = 20
print(point1.x)
point1.draw()
point1.move()


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


ishu = Person("Kartikey Jain")
ishu.talk()
ishu2 = Person("Gauri Jain")
ishu2.talk()


# INHERITANCE

class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):  # DOG WILL INHERIT ALL THE FEATURES OF MAMMAL
    pass  # PASS IS USE BECAUSE A CLASS CAN NEVER BE EMPTY


class Cat(Mammal):
    def meow(self):
        print("Meow")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.meow()

print("--------------------------------------------------------------------------------------------------------")

# HOW TO IMPORT MODULES

import app2  # IT IMPORTS ENTIRE MODULE (SAME DIRECTORY)

value = [1, 2, 4, 5, 7, 7]
print(app2.addition(value))

# OR

from app2 import addition  # CHOOSE SPECIFIC FUNCTION FROM MODULE (SAME DIRECTORY)

value = [1, 2, 4, 5, 7, 7]
total = addition(value)
print(total)

from app2 import find_max

values = [1, 7, 9, 6, 8, 3, 4]
max = find_max(values)
print(max)

print("------------------------------------------------------------------------------------------------------")

# HOW TO IMPORT MODULES FROM DIFFIRENT DIRECTORY

import ecommerce.shipping
ecommerce.shipping.calc_shipping()

# OR

from ecommerce.shipping import calc_shipping
calc_shipping()

# IMPORT WHOLE MODULE

from ecommerce import shipping
shipping.calc_shipping()

print("----------------------------------------------------------------------------------------------------")

# BUILT-IN MODULES

import random  # RANDOM IS AN IN BUILT LIBRARY
for i in range(3):
    print(random.random())
    print(random.randint(10, 20))  # RANGE FROM 10 TO 20

members = ["A", "B", "C"]
leader = random.choice(members)
print(leader)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice = Dice()  # CREATING AN OBJECT
print(dice.roll())  # CALLING THE FUNCTION USING OBJECT


from pathlib import Path

path = Path("ecommerce")  # CHECK THE EXISTENCE OF THE DIRECTORY
print(path.exists())

path = Path()
print(path.glob('*.py'))  # USE TO FIND THE FILES IN THE CURRENT DIRECTORY

for files in path.glob('*.py'):
    print(files)





from pyexcel_ods import get_data
data = get_data("transactions.ods")
import json

print(json.dumps(data))