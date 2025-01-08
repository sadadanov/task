

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    def rate_lr(self, lecturer, course, grade):
        if course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def mid_grade(self, grades):
        mid_grade_coll = []
        for grade in grades.values():
            mid_grade_coll += sum(grade) / len(grade)
        return round(sum(mid_grade_coll) / len(mid_grade_coll), 1)

    def __eq__(self, other):
        return self.mid_grade == other.mid_grade

    def __lt__(self, other):
        return self.mid_grade < other.mid_grade

    def __le__(self, other):
        return self.mid_grade <= other.mid_grade

    def __ne__(self, other):
        return self.mid_grade != other.mid_grade

    def __gt__(self, other):
        return self.mid_grade > other.mid_grade

    def __ge__(self, other):
        return self.mid_grade >= other.mid_grade

    def __str__(self):
        return (f'Имя: {self.name} /nФамилия: {self.surname} '
                f'Средняя оценка за домашние задания: {self.mid_grade}'
                f'Курсы в процессе изучения: {self.courses_in_progress}'
                f'Завершённые курсы: {self.finished_courses}')


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []



class Lecturer(Mentor):
    def __init__(self, name, surname):
        self.grades = {}
        super().__init__(name, surname)

    def mid_grade(self, grades):
        mid_grade_coll = []
        for grade in grades.values():
            mid_grade_coll += sum(grade) / len(grade)
        return round(sum(mid_grade_coll) / len(mid_grade_coll), 1)

    def __eq__(self, other):
        return self.mid_grade == other.mid_grade

    def __lt__(self, other):
        return self.mid_grade < other.mid_grade

    def __le__(self, other):
        return self.mid_grade <= other.mid_grade

    def __ne__(self, other):
        return self.mid_grade != other.mid_grade

    def __gt__(self, other):
        return self.mid_grade > other.mid_grade

    def __ge__(self, other):
        return self.mid_grade >= other.mid_grade

    def __str__(self):
        return f'Имя: {self.name} /nФамилия: {self.surname} /nСредняя оценка за лекции: {self.mid_grade}'

class Reviewer(Mentor):
    def __init__(self, name, surname):

        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student,
                Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
    def __str__(self):
        return f'Имя: {self.name} /nФамилия: {self.surname}'



best_student = Student('Ruoy', 'Eman', 'm')
some_student = Student('Gia', 'Giovanni', 'f')
best_student.courses_in_progress += ['Python']
some_student.courses_in_progress += ['Java']
best_student.add_courses('C++')

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer.courses_attached += ['Python']
cool_reviewer = Reviewer('Serg', 'Dadanov')
cool_reviewer.courses_attached += ['Java']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(some_student, 'Java', 9)
cool_reviewer.rate_hw(some_student, 'Java', 8)

best_student.rate_lr(cool_lecturer, 'Python', 9)
best_student.rate_lr(cool_lecturer, 'Python', 9)
some_student.rate_lr(cool_lecturer, 'Java', 7)
some_student.rate_lr(cool_lecturer, 'Java', 6)

print(best_student.mid_grade)
print(some_student.mid_grade)

print(best_student)
print(some_student)
print(cool_lecturer)
print(cool_reviewer)
print(best_student > some_student)


