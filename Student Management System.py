class Student:
    def __init__(self,name,roll_number):
        self.name = name
        self.Roll_number = roll_number
        self.grade = []
    def add(self,score):
        self.grade.append(score)
    def calculate_average(self):
        if len(self.grade) == 0:
            return 0
        else:
            return  sum(self.grade) / len(self.grade)
    def get_status(self):
        average = self.calculate_average()
        if average >= 60:
            return 'PASS'
        else:
            return 'FAIL'
class School:
    def __init__(self):
        self.students = {}
    def admit_student(self,name,roll_number):
        student =Student(name,roll_number)
        self.students[roll_number] = student
        self.save_data()
        print(f'{student.name} Admitted')
    def assign_grade(self,roll_number, score):
        if roll_number in self.students:
            target_student = self.students[roll_number]
            target_student.add(score)
            self.save_data()
            print(f'Grade added for {target_student.name}')
        else:
            print("Student not found!")
    def show_report(self):
        for stu in self.students.values():
            print(f'{stu.name}: Average {stu.calculate_average()}')
    def save_data(self):
        with open('students.txt','w') as f:
            for s in self.students.values():
                avg = s.calculate_average()
                stat = s.get_status()
                f.write(f'{s.name},{s.Roll_number},{avg},{stat}\n')
# 1. Create School
my_school = School()

# 2. Admit Students
my_school.admit_student("Mustansir", "A001")
my_school.admit_student("Alice", "A002")

# 3. Assign Grades
my_school.assign_grade("A001", 90)
my_school.assign_grade("A001", 80) # Mustansir Average = 85 (Pass)

my_school.assign_grade("A002", 40)
my_school.assign_grade("A002", 50) # Alice Average = 45 (Fail)

# 4. Show Report
my_school.show_report()

# 5. CHECK YOUR FILE 'students.txt'