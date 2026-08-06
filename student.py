class Student:

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def result(self):

        if self.score >= 50:
            print(self.name, "Passed")

        else:
            print(self.name, "Failed")

student1 = Student("John", 85)
student2 = Student("Mary", 40)

student1.result()
student2.result()