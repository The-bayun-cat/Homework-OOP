class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_the_lecture(self, lector, course, grade):
        if isinstance(lector, Lecturer) and course in self.courses_in_progress and course in lector.courses_attached:
            if course in lector.lecturers_ratings:
                lector.lecturers_ratings[course] += [grade]
            else:
                lector.lecturers_ratings[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        sum_ = 0
        count = 0
        for val in self.grades.values():
            sum_ += sum(val)
            count += len(val)
        return (f"Имя: {self.name}\n"
                f"Фамилия: {self.surname}\n"
                f"Средняя оценка за домашнее задание: {sum_ / count:.1f}\n"
                f"Курсы в процессе изучения: Python, Git\n"
                f"Завершённые курсы: Введение в программирование")

    def get_average_grade(self):
        sum_ = 0
        count = 0
        for val in self.grades.values():
            sum_ += sum(val)
            count += len(val)
        return sum_ / count if count > 0 else 0

    def __lt__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() < other.get_average_grade()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() == other.get_average_grade()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Student):
            return self.get_average_grade() <= other.get_average_grade()
        return NotImplemented

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturers_ratings = {}

    def __str__(self):
        sum_ = 0
        count = 0
        for val in self.lecturers_ratings.values():
            sum_ += sum(val)
            count += len(val)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {sum_/count:.1f}"

    def get_average_rating(self):
        sum_ = 0
        count = 0
        for val in self.lecturers_ratings.values():
            sum_ += sum(val)
            count += len(val)
        return sum_ / count if count > 0 else 0

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_rating() < other.get_average_rating()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_rating() == other.get_average_rating()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Lecturer):
            return self.get_average_rating() <= other.get_average_rating()
        return NotImplemented


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return "Ошибка"

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

def calculate_average_hw_grade(students, course):
    total_sum = 0
    total_count = 0
    for student in students:
        if course in student.grades:
            total_sum += sum(student.grades[course])
            total_count += len(student.grades[course])
    return total_sum / total_count if total_count > 0 else 0


def calculate_average_lecture_rating(lecturers, course):
    total_sum = 0
    total_count = 0
    for lecturer in lecturers:
        if course in lecturer.lecturers_ratings:
            total_sum += sum(lecturer.lecturers_ratings[course])
            total_count += len(lecturer.lecturers_ratings[course])
    return total_sum / total_count if total_count > 0 else 0

some_student = Student("Ruoy", "Eman", "your_gender")
some_student.courses_in_progress += ["Python"]
some_student.finished_courses += ["Введение в программирование"]

some_reviewer = Reviewer("Some", "Buddy")
some_reviewer.courses_attached += ["Python"]
some_reviewer.rate_hw(some_student, "Python", 9.9)
some_reviewer.rate_hw(some_student, "Python", 9.9)
some_reviewer.rate_hw(some_student, "Python", 9.9)

some_lecturer = Lecturer("Some", "Buddy")
some_lecturer.courses_attached += ["Python"]
some_student.rate_the_lecture(some_lecturer,"Python", 9.9)

student1 = Student("Johnny", "Depp", "C")
student1.courses_in_progress += ["Python", "Git"]
student1.finished_courses += ["Введение в программирование"]
student2 = Student("Michelle", "Rodriguez", "W")
student2.courses_in_progress += ["Python", "Git"]
student2.finished_courses += ["Введение в программирование"]

lecturer1 = Lecturer("James", "Hetfield")
lecturer1.courses_attached += ["Python", "Git"]
lecturer2 = Lecturer("Dolores", "O'Riordan")
lecturer2.courses_attached += ["Python", "Git"]

reviewer1 = Reviewer("Kurt", "Cobain")
reviewer1.courses_attached += ["Python", "Git"]
reviewer2 = Reviewer("Tarja", "Turunen")
reviewer2.courses_attached += ["Python", "Git"]

# Оцениваем студентов
reviewer1.rate_hw(student1, "Python", 9)
reviewer1.rate_hw(student1, "Python", 8)
reviewer1.rate_hw(student1, "Git", 7)

reviewer2.rate_hw(student2, "Python", 10)
reviewer2.rate_hw(student2, "Python", 9)
reviewer2.rate_hw(student2, "Git", 8)

# Оцениваем лекторов
student1.rate_the_lecture(lecturer1, "Python", 9)
student1.rate_the_lecture(lecturer1, "Git", 8)
student2.rate_the_lecture(lecturer1, "Python", 10)

student1.rate_the_lecture(lecturer2, "Python", 8)
student1.rate_the_lecture(lecturer2, "Git", 9)
student2.rate_the_lecture(lecturer2, "Python", 9)

print("Оценки студента:")
print(some_student.grades)
print()

print("Информация о проверяющем:")
print(some_reviewer)
print()

print("Информация о лекторе:")
print(some_lecturer)
print()

print("Информация о студенте:")
print(some_student)
print()

print("Информация о студентах:")
print(student1)
print(student2)
print()

print("Информация о лекторах:")
print(lecturer1)
print(lecturer2)
print()

print("Информация о проверяющих:")
print(reviewer1)
print(reviewer2)
print()

# Сравниваем студентов по средним оценкам
print("Сравнение студентов:")
print(f"student1 < student2: {student1 < student2}")
print(f"student1 == student2: {student1 == student2}")
print(f"student1 <= student2: {student1 <= student2}")
print()

# Сравниваем лекторов по средним оценкам
print("Сравнение лекторов:")
print(f"lecturer1 < lecturer2: {lecturer1 < lecturer2}")
print(f"lecturer1 == lecturer2: {lecturer1 == lecturer2}")
print(f"lecturer1 <= lecturer2: {lecturer1 <= lecturer2}")
print()

# Вычисляем средние оценки по курсам
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print("Средняя оценка за домашние задания по курсу Python:",
      calculate_average_hw_grade(students_list, "Python"))
print("Средняя оценка за домашние задания по курсу Git:",
      calculate_average_hw_grade(students_list, "Git"))
print("Средняя оценка за лекции по курсу Python:",
      calculate_average_lecture_rating(lecturers_list, "Python"))
print("Средняя оценка за лекции по курсу Git:",
      calculate_average_lecture_rating(lecturers_list, "Git"))
