class person:
    def __init__(self, fnmae, lname):
        self.fname = fnmae
        self.lname = lname
    def printFullname(self):
        print(self.fname + " "+self.lname)


class student(person):
    def printlname(self):
        print(self.lname)

me = person("majesty", "chibuikem")
me.printFullname()
sanctus = student("sanctus", "cisco")
sanctus.printFullname()
sanctus.printlname