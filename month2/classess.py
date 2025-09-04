# class User:
#     first_name = "jude"
#     last_name = "Ndubuisi"
#     age = 23
#     nationality = "Nigeria"
#     sex = "male"
#     email = "ndubuisijude46@gmail.com"
#     phone_number = "09066471342"

#     def addition():
#         return 2 + 2
    

# # object of the class user
# user1 = User()
# user2 = User()

# user1.last_name = "Ndubuisi"
# print(user1.first_name)
# print(user1.last_name)
# print(user1.age)
# print(user1.nationality)
# print(user1.sex)
# print(user1.email)
# print(user1.phone_number)



class User:
    # firstname = "majesty"
    # lastname = "chibuikem"
    # age = 30
    # sex = "gay"
    # nationality = "ibiza"
    # email = "chichi@gmail.com"
    # phone = "77"
    def __init__(self,firstname, lastname, age, sex, nationality, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.nationality = nationality
        self.email = email
        self.phone = phone
#object of the class User
user1 = User("majesty", "chibuikem", 30, "gay", "ibiza", "chichi@gmail.com", 7777)
print(user1.firstname)



# print(user1.firstname)
# print(user1.lastname)
# print(user1.age)
# print(user1.sex)
# print(user1.nationality)
# print(user1.email)
# print(user1.phone)
