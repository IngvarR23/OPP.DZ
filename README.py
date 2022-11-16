class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades1:
                lecturer.grades1[course] += [grade]
            else:
                lecturer.grades1[course] = [grade]
        else:
            return 'Ошибка'  

    def average_grade(self):
        self.average = round(sum(sum(self.grades.values(), []))/len(sum(self.grades.values(), [])), 1)
        return self.average

    
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Not a Student!')
            return
        return self.average_grade() < other.average_grade()    

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за Домашние задания: {self.average_grade()}\nКурсы в процессе изучения: {self.courses_in_progress}\nЗавершенные курсы: {self.finished_courses}'
        return res    

      
        
class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
        
          
class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades1 = {}

    def average_rate(self):
        self.average = round(sum(sum(self.grades1.values(), []))/len(sum(self.grades1.values(), [])), 1)
        return self.average  
     

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Not a Lecturer!')
            return
        return self.average_rate() < other.average_rate()  

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nCредняя оценка за лекции: {self.average_rate()} '
        return res  



class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'
          
    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


Masha_student = Student('Masha', 'Medvedeva', 'female')
Dima_student = Student('Dima', 'Stepanov', 'Male')
Masha_student.finished_courses += ['Введение в программирование']
Masha_student.courses_in_progress += ['Python', 'Git']
Dima_student.finished_courses += ['Введение в программирование', 'GIT']
Dima_student.courses_in_progress += ['Python']


Oleg_mentor = Mentor('Oleg', 'Olegovich')
Olya_mentor = Mentor('Olya', 'Oleneva')


Ivan_lecturer = Lecturer('Ivan', 'Ivanov')
Sasha_lecturer = Lecturer('Sasha', 'Smirnova')
Ivan_lecturer.courses_attached += ['Python', 'Git']
Sasha_lecturer.courses_attached += ['Python', 'Git']

Egor_reviewer = Reviewer('Egor', 'Posohin')
Rita_reviewer = Reviewer('Rita', 'Ora')
Egor_reviewer.courses_attached += ['Python', 'Git']
Rita_reviewer.courses_attached += ['Python', 'Git']


Masha_student.rate_lecturer(Ivan_lecturer, 'Python', 9)
Masha_student.rate_lecturer(Sasha_lecturer, 'Phython', 8)
Dima_student.rate_lecturer(Ivan_lecturer, 'Python', 9)
Masha_student.rate_lecturer(Sasha_lecturer, 'Python', 9)
Dima_student.rate_lecturer(Ivan_lecturer, 'Python', 8)

Egor_reviewer.rate_hw(Masha_student, 'Python', 9)
Egor_reviewer.rate_hw(Dima_student, 'Python', 9)
Rita_reviewer.rate_hw(Masha_student, 'Python',9)
Rita_reviewer.rate_hw(Masha_student, 'Python', 8)
Rita_reviewer.rate_hw(Dima_student, 'Python', 8)
Egor_reviewer.rate_hw(Masha_student, 'Git', 8)


Masha_student.average_grade()
Dima_student.average_grade()
print(Masha_student < Dima_student)
print(Masha_student)
print(Dima_student)

Ivan_lecturer.average_rate()
Sasha_lecturer.average_rate()
print(Ivan_lecturer < Sasha_lecturer)
print(Ivan_lecturer)
print(Sasha_lecturer)

print(Egor_reviewer)
print(Rita_reviewer)


student_list =[Masha_student, Dima_student]
def grade_av_student(student_list, course):
  sum = 0
  count = 0
  for person in student_list:
    for i in person.grades[course]:
        sum += i
        count += 1
  return round(sum/count, 1)
  

lecturer_list =[Ivan_lecturer, Sasha_lecturer]
def grade_av_lecturer(lecturer_list, course):
  sum = 0
  count = 0
  for person in lecturer_list:
    for i in person.grades1[course]:
        sum += i
        count += 1
  return round(sum/count, 1)  

print(grade_av_student(student_list, 'Python'))
print(grade_av_lecturer(lecturer_list, 'Python'))