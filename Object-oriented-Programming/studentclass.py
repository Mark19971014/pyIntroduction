#面向对象编程:object-oriented-programming(OOP)

class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def goLecture(self,lecture):
        return lecture
    @classmethod
    def doMathhomwork(self,a,b):
        return a + b
   

def main():
    #student = get_student()
    #print(f"{student.name} from {student.house}")
    student1 = Student("junhao","Nanjing")
    student2 = Student("xiaohuan","Tianjing")
    #print(student1.goLecture("Math"))
    print(student1.doMathhomwork(1,1))
    print(student2.doMathhomwork(1,1))

    Student.doMathhomwork()

def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)
        #Student("mark","DTU"")

if __name__ == "__main__":
    main()
    