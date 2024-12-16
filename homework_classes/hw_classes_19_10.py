# Задание 1,2
class Teacher:
    teachers_list = []  
    
    def __init__(self, name, education, experience):
        self.__name = name
        self.__education = education
        self.__experience = experience
        self._marks = {}
        Teacher.teachers_list.append(self)  
        
    # Геттеры  
    def get_name(self):
        return self.__name
    
    def get_education(self):
        return self.__education

    def get_experience(self):
        return self.__experience

    # Сеттер для опыта работы
    def set_experience(self, value):
        self.__experience = value
    
    # Метод для получения информации об учителе    
    def get_teacher_data(self):
        return f'Имя: {self.__name}, Образование: {self.__education}, Опыт работы: {self.__experience} лет.'    
    
    # Метод для добавления оценки 
    def add_mark(self, student_name, student_mark):
        if student_name in self._marks:
            self._marks[student_name].append(student_mark)
        else:
            self._marks[student_name] = [student_mark]
        return f'{self.__name} поставил оценку {student_mark} студенту {student_name}'
    
    # Метод для удаления оценки
    def remove_mark(self, student_name, student_mark):
        if student_name in self._marks and student_mark in self._marks[student_name]:
            self._marks[student_name].remove(student_mark)
            return f'{self.__name} удалил оценку {student_mark} студенту {student_name}'
        else:
            return f"Оценка {student_mark} не найдена для студента {student_name}."
        
    # Метод для получения оценок всех учеников
    def get_marks(self):
        return f'Оценки: {self._marks}'
    
    # Метод для получение оценок конкретного ученика
    def get_student_mark(self, student_name):
        if student_name in self._marks:
            return f"Оценки для студента {student_name}: {self._marks[student_name]}"
        else:
            return f"Студент {student_name} не найден."

    # Метод для консультации
    def give_a_consultation(self, student_class):
        return f'{self.__name} провел консультацию в классе {student_class}'
    
    @classmethod
    def fire_teacher(cls, teacher):
        if teacher in cls.teachers_list:
            cls.teachers_list.remove(teacher)
            return f'Учитель {teacher.get_name()} уволен.'
        else:
            return 'Учитель не найден в списке.'
    

class DisciplineTeacher(Teacher):
    
    def __init__(self, name, education, experience, discipline, job_title):
        super().__init__(name, education, experience)
        self._discipline = discipline
        self._job_title = job_title
        
    # Геттеры
    @property
    def discipline(self):
        return self._discipline

    @property
    def job_title(self):
        return self._job_title

    # Сеттер для должности
    @job_title.setter
    def job_title(self, value):
        self._job_title = value
        
    # Переопределение метода для получения информации об учителе
    def get_teacher_data(self):
        base_data = super().get_teacher_data()
        return f'{base_data}\nПредмет: {self._discipline}, должность: {self._job_title}'
    
    # Переопределение метода для добавления оценки
    def add_mark(self, student_name, student_mark):
        return super().add_mark(student_name, student_mark) + f'\nПредмет: {self._discipline}'
    
    # Переопределение метода для удаления оценки
    def remove_mark(self, student_name, student_mark):
        return super().remove_mark(student_name, student_mark) + f'\nПредмет: {self._discipline}'
    
    # Переопределение метода для консультации
    def give_a_consultation(self, student_class):
        return super().give_a_consultation(student_class) + f'\nПо предмету {self._discipline} как {self._job_title}'
    
    # Метод для получение оценок конкретного ученика
    def get_student_mark(self, student_name):
        if student_name in self._marks:
            return f"Оценки для студента {student_name} по предмету {self._discipline}: {self._marks[student_name]}"
        else:
            return f"Студент {student_name} не найден."

if __name__ == "__main__":
    discipline_teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")
    teacher_2 = Teacher("Иван Петров", "БГПУ", 4)
    discipline_teacher_2 = DisciplineTeacher("Артем Иванов", "МГУ", 5, "Английский", "Старший преподаватель")

    print(discipline_teacher.get_teacher_data())
    print(discipline_teacher.add_mark("Алексей", 5))
    print(discipline_teacher.add_mark("Алексей", 4))
    print(discipline_teacher.add_mark("Андрей", 4))
    print(discipline_teacher.add_mark("Иван", 4))
    print(discipline_teacher.get_marks())
    print(discipline_teacher.remove_mark("Алексей", 5))
    print(discipline_teacher.remove_mark("Андрей", 5))
    print(discipline_teacher.get_marks())
    print(discipline_teacher.get_student_mark("Иван"))
    print(discipline_teacher.get_student_mark("Алла"))
    print(discipline_teacher.give_a_consultation("10А"))
    print()
    print(teacher_2.add_mark("Иван", 4))
    print(teacher_2.get_student_mark("Иван"))
    print()
    print(discipline_teacher_2.add_mark("Андрей", 4))
    print(discipline_teacher_2.get_student_mark("Андрей"))
    print(discipline_teacher_2.give_a_consultation("10Б"))
    print()
    # print(teacher_2.__name)
    print(teacher_2.get_name())
    print()
    print(Teacher.teachers_list)  
    print(Teacher.fire_teacher(discipline_teacher))  
    print(Teacher.teachers_list)  
