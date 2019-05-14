class Student:
    """
        Represents information of 
        students and their details
    """

    def __init__(self, rollNo, name):
        self.rollNo = rollNo
        self.name = name
        self.age = None
        self.marks = None

    def display(self):
        print(self.rollNo, self.name, self.age, self.marks)

    def setAge(self, age):
        self.age = age

    def setMarks(self, marks):
        self.marks = marks

stud1 = Student(1, 'Abhijeet Singh')
stud1.setAge(22)
stud1.setMarks(100)
stud1.display()
