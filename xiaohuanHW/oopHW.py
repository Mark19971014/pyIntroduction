class Student:
    def _init_(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age =age

def main():
    student1 = ("xiaohuan", "female","19")

def get_student():
    name = input("Name: ")
    gender = input("gender: ")
    age = input("age:")
    return Student(name, gender,age)


    