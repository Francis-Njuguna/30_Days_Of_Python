#Working with strings
mystring = "Hello, World!"
print(mystring)  # Output the string

#String indexing
mystring[0:3]  # Output: 'Hel'
print(mystring[0:3])  # Output the substring

#String methods
print(mystring.upper())  # Output: 'HELLO, WORLD!'
print(mystring.lower())  # Output: 'hello, world!'
print(mystring.split(","))  # Output: ['Hello', ' World!']
#String concatenation
greeting = "Hello"
name = "Alice"

name_greeting = greeting + ", " + name + "!"
print(name_greeting)  # Output: 'Hello, Alice!'

#String formatting
age = 30
formatted_string = f"{name} is {age} years old."

#the purpose of the f before the string is to indicate that it is a formatted string literal, allowing for the inclusion of expressions inside curly braces {} that will be evaluated at runtime.
print(formatted_string)  # Output: 'Alice is 30 years old.'
#Another way of formatting strings
formatted_string2 = "{} is {} years old.".format(name, age)
print(formatted_string2)  # Output: 'Alice is 30 years old.'
