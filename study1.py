# %%
a = 1
b=2
a+b

# %% Hello World
print("Hello, World!")

# %% Indentation
if 2 > 1:
    print("Two is greater than one.")


# %%
def say_hello(name):
    return f"Hello {name}"


say_hello("John")

# %% Variables
a = 1
b = "Hello World"

print(a)
print(b)

# %%
π = 3.14159
jalapeño = "a hot pepper"
好吃 = "delicious"

print(π)
print(jalapeño)
print(好吃)

# %% Data Types
a = "123"

b = 123
c = 123.4
d = 123 + 4j
e = complex(123, 4)

f = [1, 2, 3]
g = (1, 2, 3)
h = range(10)

i = {1: "a", 2: "b"}

j = {1, 2, 3}
k = frozenset(j)

l = True

# %% List
cars = ["honda", "tesla", "ford"]
length = len(cars)
length

# %%
values = [1, 2, 3, 4, 5.6, 7.8, 9.01]
print(max(values))
print(min(values))
print(sum(values))

# %%
cars = ["honda", "tesla", "ford"]
first = cars[0]
last = cars[-1]
print(first, last)

# %% List Comprehension
letters = []
for letter in "data analytics":
    letters.append(letter)
print(letters)

letters = [letter for letter in "data analytics"]
print(letters)

# %%
term = "data analytics"
letters = [letter for letter in term if letter not in "aeiou"]
print(letters)

# %%
print([i for i in range(1, 101) if i % 2])

# %%
print([i * 3 for i in range(100)])

# %%
x, y = 2, 10

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x**y)
print(x // y)

# %%
x -= 1
x


# %%
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# %%
print(x > 1 and x < 10)
print(x > 1 or x < 10)
print(not (x < 5))


# %%
x, y = 10, 10

print(x is y)
print(x is not y)

# %%
x, y = object(), object()

print(x is y)
print(x is not y)

# %%
x, y = 1, [1, 2, 3]
print(x in y)
print(x not in y)

# %%
x, y = 4, 5
print(x & y)
print(x | y)
print(x ^ y)
print(~x)
print(x << y)
print(x >> y)

# %%
# This is a comment.
print("Hello, World!")

print("Hello, World!")  # This is a comment.

# %%
a = 1
b = 2
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# %%
i = 0
while i < 10:
    print(i)
    i += 1

# %%
for i in range(10):
    print(i)


# %%
fruits = ["apple", "banana", "coconut"]
for fruit in fruits:
    print(fruit)


# %%
def echo(word):
    print(word)


echo("hello")


# %%
def add(a, b):
    return a + b


add(1, 2)

# %%
import math

print(math.pow(2, 5))

from datetime import datetime

print(datetime.now())

import math as m

m.pow(2, 5)

# %%
try:
    print(a + 1 + "abc")
except NameError:
    print("Variable a is not defined")
except Exception as e:
    print("Something else went wrong")
    print(e)
else:
    print("Nothing happened")
finally:
    print("done")

# %%
email = input("Enter email: ")
print(f"Your email is: {email}")

# %%
