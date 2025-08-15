# a = "ball"
# b = "ping"

# print(a + b) 

# c = 3
# d = 5
# print(c + d)

# print(a + c)

# name = "Jude" #global variable

# def greet():
#     age = 22
#     print(f"hello my name is {name}") # global variable is being accessed
#     print(f"i am {age} years old")

# print(name)
# # greet()

# name = "a" #global variable

# def greet():
#     name = "b"
#     print("this is for local " + name) # local variable is being accessed
# greet()
# print("this is for global " + name) # global variable is being accessed 

name = "a" #global variable

def greet():
    global phone_no
    phone_no = 345

greet()

print(phone_no)

print('hello')

print("hello") # use this one instead

name = "jude"

print("this is my name", name)

print(f"this is my name, {name}") # this is called place holder

txt = "we are the so_called \"vikings\" from the north"

print(txt)
# the boys are "swagging"
