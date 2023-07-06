class Student:
    def __init__(self, name: str, age: int, grades: list):
        self.name = name
        self.age = age
        self.grades = grades

    def count_scholarship(self):
        ss = 0
        for i in range(len(self.grades)):
            ss = ss + self.grades[i]
        ship = ss * 1000
        return ship

    def add_grade(self, mark: int):
        self.grades.append(mark)
        print(*self.grades )

    def clear_grades(self):
        self.grades.clear()


student = Student("Игорь", 20, [3, 4, 3, 2, 5, 5])


print(student.grades)
print(student.count_scholarship())
print(student.add_grade(1))
