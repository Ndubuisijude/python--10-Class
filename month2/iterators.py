mytuple = ("apple", "banana", "cherry")

myiter = iter(mytuple)
print(myiter)
print(next(myiter))
print(myiter)
print(next(myiter))
print(myiter)
print(next(myiter))
print(myiter)


def myfunc():
  global x
  x = 300
  print(x)

  print(x)
myfunc()