print("Hello World")

# if else block
if 1 > 2:
    print("True")
else:
    print("False")
    print("Hello")


"""This is a multi-line
comment"""

print("hello everyone")  # printing hello everyone
print("hello everyone")
print("""hello everyone""")
print("""hello everyone""")
print(
    """hello everyone 
I hope you are well. 
Welcome to Robogarden course 
"""
)


a = 2  # a is an integer variable name which its value is 2
print(type(a))  # printing the type of variable a
print(a)


Name = "John"  # Name is a string variable name which its value is John
NAME = "Harmeet"

print(Name)
print(NAME)

del NAME

# print(NAME)  # this will give an error because we deleted the variable NAME


ls1 = ["abcd", 786, 2.23, "lj"]
ls2 = [20, "garden"]
print(ls1)
print(ls1[1])
print(ls1[1:3])
print(ls1[1:])
print(ls1 * 2)
print(ls1 + ls2)


tp = (2, "john", 5.6)
ls = [10, "abcd", 2.1]
print(tp)
print(ls)
ls[1] = 20
print(ls)
# tp[1] = 20
# print(tp)


dt = {}
dt["A"] = "all people"
dt[2] = "number two"

print(dt)  # prints the whole dictionary

print(dt["A"])  # Prints value for 'A' key
print(dt[2])  # Prints value for 2 key
print(dt.keys())  # print all keys
print(dt.values())  # print all values


a = None  # null
print(type(a))


a = 2.3
b = int(a)  # convert a to integer type
c = str(a)  # convert a to string type

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))

print("The value of a is " + str(a))


a = 19
b = 10

# Addition
print("a + b : ", a + b)

# Subtraction
print("a - b : ", a - b)

# Multiplication
print("a * b : ", a * b)

# Division
print("a / b : ", a / b)

# Modulus
print("a % b : ", a % b)

# Exponent
print("a ** b : ", a**b)

# Floor Division
print("a // b : ", a // b)


# Assignment Operator
x = 5
print("x=", x)

# Addition Assignment

y = 0
y += 2
print("y += 2:", y)

x = x + 2
print(x)


a = 10
b = 20
ls = [12, 10, "hell"]
tp = ("hi", 10, 20)

print("a in ls:", a in ls)
print("a not in tp:", a not in tp)
print("b in ls:", b in ls)
print("b not in tp:", b not in tp)


var = "Robogarden is a great place to learn"

print("var[2]=", var[2])

print("var[4:6]=", var[4:6])

print("var[4:]=", var[4:10])  # extract substring from the index 4 till the end


var = "Robogardenisagreatplacetolearn"

print("var[-3]=", var[-3])

print("var[-2:-5]=", var[-2:])


st1 = "hello everyone"

st2 = "Robogarden"

st3 = "hi"


## assign one string to another string

st3 = st2

print("st2=", st2)

print("st3=", st3)


##change string with its previous content

print("The original value of st1=", st1)

st1 = st1[0:3] + " Python"

print("After modification: st1=", st1)


## Try to change the entire content of the string

# st1[0] = "f"
#
# print("st1=", st1)


# string operators

st = "hello"  # assignment operator

print("st=", st)

st = st + " everyone"  # concatenation operator

print("st=", st)

st2 = st * 3  # repetition operator

print("st2=", st2)

print("st2[1]=", st2[1])  # slice operator

print("st2[0:4]=", st2[0:4])  # range slice operator


if "eve" in st2:  # membership operator

    print("'eve' exists in the st2:", st2)


print("hello \nworld")  ## new line character \n

print("#########")

print("hello\tworld")  ## tab character \t

print("#########")

print("hello!!\rworl")  ## Carriage return character \r


name = "Robo"

age = 10

marks = 30.8

degree = -10

string1 = "Hi %s" % (name)

print(string1)

string2 = "Hey %s, my age is %u" % (name, age)

print(string2)

string3 = "Hey %s, my subject mark is %f" % (name, marks)

print(string3)

string4 = "Hey %s, the weather degree is %d" % (name, degree)

print(string4)


string = "robo,garden,John,Ali"

print("string=", string)

print("length of the string=", len(string))  # return the length of the string

ls = string.split(
    ","
)  # divide string into multiple substrings based on the ',' delimiter

print("ls=", ls)

st = ls[1].capitalize()  # capitalize the first letter of the string

print("st=", st)

ls = [2, 19, 3, "hello", 3, 9.2]
print("ls=", ls)
del ls[1]  # delete the list item (19) at index 1
print("ls=", ls)
ls.remove(3)  # will remove the first matching number (3) from list
print("ls=", ls)

# ls.remove("Hi")
# print("ls=", ls)


# del ls[10]  # delete the list item (19) at index 1


ls = [2, 19, 3, "hello", 3, 9.2]
print("ls=", ls)
print("len(ls)=", len(ls))  # length of list
ls.append(20)  # Adds an item to the list
print("ls=", ls)
ls2 = ["hi", "welcome"]
ls.extend(ls2)  # Adds squence to the list
print("ls=", ls)

ls3 = [2, 8, 2, 11, 1, 7]
print("max(ls3)=", max(ls3))  # maximum value of the list
print("min(ls3)=", min(ls3))  # minimum value of the list
ls3.sort()  # sort list in ascending order
print("ls3.sort():", ls3)
ls3.insert(2, 15)  # insert value at a specific index
print("ls3.insert(15,2):", ls3)
print("ls3.index(15)=", ls3.index(15))  # get index


tp1 = (2, 9, 12.8)
tp2 = ("hi", 2, 9.9)
print("tp1=", tp1)
tp1 = tp2
print("tp1=", tp1)
del tp1
# print("tp1=", tp1)


tp1 = (2, 8, "hello")
tp2 = ("hi", 2, True)
print("tp1+tp2=", tp1 + tp2)
print("tp1*3=", tp1)
print("len(tp1)=", len(tp1))
tp3 = (3, 1, 21, 11)
print("max(tp3)=", max(tp3))
print("min(tp3)=", min(tp3))


dict1 = {"h": "hello", "w": "welcome", "r": "Robogarden"}
print("dict1=", dict1)

dict1["j"] = "John"  # adding a new entry to the dictionary
print("dict1=", dict1)

dict1["h"] = "hi"  # modify an existing entry
print("dict1=", dict1)

del dict1["w"]  # delete an existing entry
print("dict1=", dict1)

dict1.clear()  # remove all entries in the dictionary
print("dict1=", dict1)

# del dict1  # delete the dictionary itself
# print("dict1=", dict1)


dict1 = {"a": "Apple", "a": "first"}  # duplicate key
print('dict1["a"]=', dict1["a"])

# dict1 = {["a"]: "area"}
# print("dict1", dict1)


dict1 = {1: "Hi", 2: "welcome", 3: "RoboGarden"}
print("dict1=", dict1)
print("len(dict1):", len(dict1))
print("dict1.items():", dict1.items())
print("dict1.values():", dict1.values())
print("dict1.keys():", dict1.keys())
print("output sting=", "The dict1 is " + str(dict1))
print("dict1.get(key, default=False): ", dict1.get(7, False))


dict1.setdefault(4, "everyone")
print("After setting default: dict1=", dict1)

dict2 = dict1.copy()
print("dict2=", dict2)

dict3 = {8: "yes", 9: "No"}
dict1.update(dict3)
print("dict1=", dict1)


a = 10


print("Checking the first condition")

if a > 20:  # condition is False, the code block will not be executed

    print("a is greater than 20")


print("Checking the second condition")

if a < 20:  # condition is True, the code block will be executed

    print("a is lower than 20")


print("Bye Bye")


a = 10

if a > 20:  # condition is False, the code block inside else statement will be executed

    print("a is greater than 20")

else:

    print("a is lower than 20")


a = 4

if a > 2:  # condition is True, the code block inside if statement will be executed

    print("a is greater than 2")

else:

    print("a is lower than 2")


print("Bye bye")


grade = 67


if grade > 85:

    print("Excellent")

elif grade > 75:

    print("Very good")

elif grade > 65:

    print("Good")

elif grade > 50:

    print("Pass")

else:

    print("Failed")


print("Good luck")


x = 50


if x < 60:

    print("x is less than 60")

    if x > 55:

        print("x is greater than 55")

    elif x == 50:

        print("x equals 50")
    elif x > 45:

        print("x is greater than 45")

    else:

        print("x is less than 45")
else:

    print("x is greater than 60")


print("Bye bye")


i = 5

while i > 0:

    print("i=", i)

    i -= 1


print("Good bye")


num = 10

while num > 5:

    print("Inside the loop, num:", num)

    num -= 1

else:

    print("Outside the loop, num:", num)


ls = [7, "Hello", 2.5]

st = "Robogarden"


for item in ls:  # iterate over a list

    print("item:", item)


for letter in st:

    print("letter:", letter)


ls = [7, "Hello", 2.5]

for ind in range(len(ls)):  # iterate over a list

    print("index:", ind, "item:", ls[ind])


tp = ("hello", "hi", "Robo")


for i in range(len(tp)):

    print("tuple index:", i, "tuple item:", tp[i])

    for letter in tp[i]:

        print("letter:", letter)


st = "Robogarden"

for ind in range(len(st)):  # break example

    letter = st[ind]

    if "g" == letter:

        break

    print("current letter is:", letter)


print("The letter 'g' was found in the string at the index=", ind)


x = 0

while x < 6:  # continue example

    x += 1

    if x == 3 or x == 5:

        continue

    print("Current x value is:", x)


ls = [10, 2.6, "hello", 8, 9.1]

for item in ls:  # pass example

    if item == 8:

        pass

        print("line after pass statement")

    print("item is:", item)


print("Bye bye")


for i in range(5):
    pass


print("hello")


def greeting():
    print("Hello, welcome to our first function!")


greeting()


def seconds_in_day():
    hours_in_day = 24
    mins_in_hour = 60
    sec_in_min = 60
    return hours_in_day * mins_in_hour * sec_in_min


# Call the function and display the number of seconds in a day from the return statement
print(seconds_in_day())

# or
print(f"There are {seconds_in_day()} seconds in a day!")


def welcome(student, grade):
    print(f"Hello, {student} - Welcome to grade {grade}!")


welcome(10, "Sam")


def welcome(student, grade):
    print(f"Hello, {student} - Welcome to grade {grade}!")


welcome(grade=10, student="Sam")


def describe_pet(pet_name, species="cat"):
    print(f"I have a {species} named {pet_name}.")


describe_pet("Lucky")
describe_pet("Lucy", "rabbit")


def multiply_numbers(*args):
    total = 1
    for num in args:
        total *= num
    return total


result = multiply_numbers(1, 2, 3)
print(result)


def example_function(**kwargs):
    movies = {}  # Create an empty dictionary to store the key-value pairs

    for key, value in kwargs.items():
        movies[key] = value  # Save key-value pair in the dictionary
    return movies


# Calling the function with keyword arguments
result = example_function(movie="Toy Story", year=1995, revenue=395000000)
print(result)


double = lambda x: x * 2
print(double(5))


def calculate_square(number):
    answer = number**2
    return answer


squared_value = calculate_square(10)
print(squared_value)

# print(answer)  ### Delete the # and try running this line yourself!


def calculate_square(number):
    answer = number**2
    return answer


number = 10
squared_value = calculate_square(number)
print(squared_value)

print(number)
# print(answer)  # This line, if run, will still return an error as ‘answer’ is a local variable!


variable = "I’m a Global Variable"


def update_value():
    variable = "I’m a Local Variable"

    print("Inside function:", variable)


update_value()
print("Outside function:", variable)


import math as m

print(dir(m))


print(m.sqrt(16))


import custom_module

print(custom_module.greeting("Sam"))
print(custom_module.square(10))


import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5])

# Square the elements in the array
result = arr**2
print(result)


import pandas as pd

# Create a DataFrame from a dictionary
data = {"Name": ["Sam", "Susan", "Shen"], "Age": [25, 30, 22]}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
df


# st = input("Enter your input:")
#
# print("The input is:", st)
#
#
# st = input("Enter your input:")
#
# print("The input is:", st)


# file = open("first.txt", "w")
#
# print("file.closed:", file.closed)
#
# print("file.mode:", file.mode)
#
# print("file.name:", file.name)
#
#
# file = open("first.txt", "r")
#
# print("file.closed=", file.closed)
#
# file.close()
#
# print("file.closed=", file.closed)


file = open("first.txt", "r")

out = file.read()  ## read the 8 bytes of the file

print("The data in the file is:", out)

file.close()


file = open("first.txt", "r")

file_lines = file.readlines()  # return a list of file lines

print("length of file lines is:", len(file_lines))

for line in file_lines:

    print("The file line is:", line)


file.close()


file = open("first.txt", "w")

file.write("Hello students!!\nWelcome to the Robogarden course.")

file.close()


file = open("first.txt", "r")

chunk_out = file.read(8)  ## read the 8 bytes of the file

print("chunk_out=", chunk_out)

current_pose = file.tell()

print("current_pose=", current_pose)


chunk_out = file.read(8)  ## read the 8 bytes of the file

print("next chunk_out=", chunk_out)


## return the pointer to the first position of the file again

file.seek(
    0, 0
)  ## offset=0 (number of movements after fromwhere is 0) and fromwhere=0 (first position)

# read the first 8 bytes again

chunk_out = file.read(8)  ## read the 8 bytes of the file

print("chunk_out=", chunk_out)


file.close()


import os

# os.rename("first.txt", "third.txt")  ## rename an existing file

# os.remove("hello.txt")  # remove an existing file


print(os.getcwd())  # get current working directory

# os.mkdir("new")  # create a new directory, called new

os.chdir(
    "C:/harmeet/machine_learning_2025/home/robogarden/"
)  # change the current working directory to "/home/robogarden/"
# os.rmdir("example")  # remove the directory "example"


print(os.getcwd())  # get current working directory

# os.rmdir("new")  # remove the directory "example"


# os.chdir(
#    "C:/harmeet/machine_learning_2025/"
# )  # change the current working directory to "/home/robogarden/"
# os.rmdir("example")  # remove the directory "example"


print(os.getcwd())  # get current working directory

# os.rmdir("new")  # remove the directory "example"


def conv_degree_to_percentage(degree, total_degree):

    assert (
        degree >= 0 and total_degree >= 0
    ), "Your course degree or total degree is below than zero"

    return (degree / total_degree) * 100


#
# degree = float(input("Enter degree:"))
#
# total_degree = float(input("Enter total degree:"))
#
#
# percentage = conv_degree_to_percentage(degree, total_degree)
#
# print("Your degree by precent:", percentage)


# try:
#
#    denom = float(input("Enter the denominator value: "))
#
#    out = 50.0 / denom
#
#
# except ZeroDivisionError:
#
#    print("The denominator should not be zero")
#
# else:
#
#    print("The out is calculated successfully")

i  ## except clause with no exception

try:

    st = "hello" + 22  # concatenate string with float


except Exception as e:
    print(e)

    print("An exception occured")

else:

    print("No exception occured in the try block")


# except clause with multiple exceptions

# try:
#
#    st = "hello" + 22  # concatenate string with float
#
#
# except IOError or TypeError:
#
#    print("TypeError or IOError occured")
#
# else:
#
#    print("No exception occured in the try block")


try:

    f = open("local.txt", "r")  # file local.txt doesn't exist

    print("start reading lines")

    lines = f.readlines()

except FileNotFoundError as fnf_error:

    print("File not found error occured")


finally:

    print("In the finally section")


total_degree = 30


def conv_degree_to_percentage(degree):

    if degree < 0:

        raise ValueError("Your course degree or total degree is below zero")

    return (degree / total_degree) * 100


try:

    conv_degree_to_percentage(-1)


except ValueError as arg:

    print("The ValueError exception is raised due to:", arg)


class Car:

    def __init__(self, make, model):

        self.make = make

        self.model = model

    def description(self):

        print(f"This is a {self.make} {self.model}.")


my_car1 = Car("Toyota", "Corolla")
print(type(my_car1))

my_car1.description()

my_car2 = Car(make="Hyundai", model="Sonata")

my_car2.description()

del my_car2


# my_car2.description()


# Create the base class


class Car:

    def __init__(self, make, model):

        self.make = make

        self.model = model

    def display_info(self):

        print(f"This is a {self.make} {self.model}.")


# Create the subclass


class ElectricCar(Car):

    def __init__(self, make, model, battery_capacity):

        super().__init__(make, model)

        self.battery_capacity = battery_capacity

    def display_battery(self):

        print(f"This electric car has a {self.battery_capacity} kWh battery.")


# Create an instance of the classes

electric_car = ElectricCar("Tesla", "Model S", 50)


# Call the methods the object instance

electric_car.display_info()

electric_car.display_battery()


# Create the base class


class Car:

    def __init__(self, make, model, msrp):

        self.make = make

        self.model = model

        self._MSRP = msrp  # protected value once instance created

    def get_msrp(self):

        return self._MSRP


# Create an instance of the class

my_car = Car("Tesla", "Model S", 50000)

print(my_car.get_msrp())


# Attempt to update Restricted attribute

my_car._MSRP = 60000

print(my_car.get_msrp())


# Define the Car class, with a new Class Attribute


class Car:

    country_of_origin = "USA"

    def __init__(self, make, model):

        self.make = make

        self.model = model

    def display_info(self):

        print(f"This is a {self.make} {self.model} made in {Car.country_of_origin}.")


# Create an instance of the Car class

my_car = Car("Tesla", "Model S")


# Use the Class attribute from within a method

my_car.display_info()