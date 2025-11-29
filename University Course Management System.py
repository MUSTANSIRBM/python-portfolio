import datetime
import json
def log_action(func):
    def wrapper(*args,**kwargs):
        timestamp = datetime.datetime.now()
        with open ('../audit.txt', 'a') as f:
            f.write(f'{timestamp} Executing Function: {func.__name__}\n')
        return func(*args,**kwargs)
    return wrapper
class Student:
    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {}
    def add_grade(self,subject, score):
        self.grades[subject] = score

    def get_gpa(self):
        if not self.grades:
            return 0.0

        return sum(self.grades.values()) / len(self.grades)
class Course:
    def __init__(self):
        self.students = []
        self.load_data()
    @log_action
    def enroll(self,name, student_id):
        for s in self.students:
            if s.student_id == student_id:
                print(f"Student {name} is already enrolled.")
                return
        a = Student(name,student_id)
        self.students.append(a)
        self.save_data()
    def assign_grade(self,student_id, subject, score):
            for student in self.students:
                if student.student_id == student_id:
                    student.add_grade(subject, score)
                    self.save_data()
                    print(f'grade added for {student.name}')
                    return
            print('Error: Student ID not found.')
    def get_top_student(self):
        best_student = self.students[0]
        for stu in self.students:
            if stu.get_gpa() >best_student.get_gpa():
                best_student =stu
        print(f"Top student is {best_student.name} with GPA: {best_student.get_gpa()}")
    def save_data(self):
        data = []
        for stu in self.students:
            st_dict = {
                "name": stu.name,
                "student_id": stu.student_id,
                "grades": stu.grades
            }
            data.append(st_dict)
        with open('../course_db.json', 'w') as f:
            json.dump(data, f)
    def load_data(self):
        try:
            with open('../course_db.json', 'r') as f:
                raw = json.load(f)
            self.students = []
            for item in raw:
                new_student = Student(item["name"], item["student_id"])
                new_student.grades = item.get("grades", {})
                self.students.append(new_student)
        except FileNotFoundError:
            self.students = []
        except json.JSONDecodeError:
            self.students = []
if __name__ == "__main__":
    print("--- Initializing Course Management System ---")

    # Initialize the Course (this triggers load_data)
    my_course = Course()

    # 1. Enroll Students (Triggers @log_action)
    # Using the name from your snippet
    my_course.enroll("Mustansir", 25030124086)
    my_course.enroll("sourabh", 25030124114)
    my_course.enroll("aman", 25030124078)

    print("\n--- Assigning Grades ---")
    # 2. Assign Grades (Triggers save_data inside)
    my_course.assign_grade(25030124086, "FWT", 97)
    my_course.assign_grade(25030124086, "Python", 95)

    my_course.assign_grade(25030124114, "FWT", 80)
    my_course.assign_grade(25030124114, "Python", 66)

    my_course.assign_grade(25030124078, "FWT", 89)  # Alice is smart
    my_course.assign_grade(25030124078, "Python", 72)  # Alice is smart

    print("\n--- Analytics ---")
    # 3. Calculate Results
    my_course.get_top_student()

    print("\n--- Verification ---")
    print("Check 'audit.txt' for enrollment timestamps.")
    print("Check 'course_db.json' for persisted student data.")