# #function


# # def greetings():
# #     print("welcome to the application")
# # greetings()


# # num1 = int(input("Enter first number: "))
# # num2 = int(input("Enter second number: "))
# # def add(a,b):
# #     print(a + b)
# # add (1, 2)


# myName = "majesty"
# myName1 = "debby"
# myName2 = "nenye"
# myName3 = "justina"
# myName4 = "despina"
# myName5 = "somto"

# def greet(*yourName):
#   print(f"hello user {yourName[3]}")
# greet(myName, myName1, myName2, myName3, myName4, myName5)


# def my_function(child1, child2, child3):
#   print("the oldest child is" + child1)
#   print("the middle child is" + child2)
#   print("the youngest child is" + child3)

#   my_function(child2= "great", child1= "jude", child3="paschal")


# # time space complexity

# # parameters and arguments
# def add2(num1 = 5, num2 = 5):
#      sum = num1 + num2
#      print(num1)
#      print(num2)
#      print(f"this is the sum: {sum}")

# add2(6)

# choice = 1
# while(choice == 1):
#    pass

# for X in range(5):
#    pass

# bakerylist = ["bread", "cake", "donuts", "cookies", "muffins", "strawberry cake"]
# # function check through my list for strawberry cake
# def checkStock(pastry):
#    counter = 0
#    for item in pastry:
#       if item != "strawberry cake":
#          counter += 1
#          print(counter, "loop")
#          continue
#       else:
#          print("yes we are in stock")
# checkStock(bakerylist)


classList = ["nenye", "actress", "despina", "kamsy", "somto", "sanctus", " chisom", "irene", "pascal", "jude", "daniel", "chiemerie", "kosi"]

def school(list):
   for student in list:
      if student == "jude":
         print("Found Jude!")
      else:
         print("Not Jude")
school(classList)

# def add2():
#     num1 = 10
#     num2 = 20
#     sum = num1 + num2
#     return sum

# thesum = add2()
# print(thesum)
