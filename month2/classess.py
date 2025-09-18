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

    """
    a constructor to get user data
    """
    def __init__(self,firstname, lastname, age, sex, nationality, email, phone):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.sex = sex
        self.nationality = nationality
        self.email = email
        self.phone = phone


    """
    method to return first name
    """
    def print_firstname(self):
        print(self.firstname)

    def print_lastname(self):
        print(self.lastname)

    def print_age(self):
        print(self.age)

    def print_sex(self):
        print(self.sex)

    def print_nationality(self):
        print(self.nationality)

    def print_email(self):
        print(self.email)

    def print_phone(self):
        print(self.phone)
#object of the class User
user1 = User("majesty", "chibuikem", 30, "gay", "ibiza", "chichi@gmail.com", 7777)
userDaniel = User("Daniel", "Onyenta", 12, "child", "israel", "danielOs@gmail.com", 8888)

userMajesty = user1
userMajesty.print_firstname()
userDaniel.print_firstname()
userMajesty.print_lastname()
userMajesty.print_age()
userMajesty.print_sex()
userMajesty.print_nationality()
userMajesty.print_email()
userMajesty.print_phone()


# print(user1.firstname)
# print(user1.lastname)
# print(user1.age)
# print(user1.sex)
# print(user1.nationality)
# print(user1.email)
# print(user1.phone)
print(userMajesty.phone)