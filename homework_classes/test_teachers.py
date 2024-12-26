import unittest
from hw_classes_19_10 import Teacher, DisciplineTeacher

class TestTeacherMethods(unittest.TestCase):

    def setUp(self):
        # Очистка списка учителей перед каждым тестом
        Teacher.teachers_list.clear()

    def test_fire_teacher(self):
        teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")
        Teacher.teachers_list.append(teacher)  # Добавляем учителя в список
        self.assertIn(teacher, Teacher.teachers_list)
        self.assertEqual(Teacher.fire_teacher(teacher), 'Учитель Иван Петров уволен.')
        # self.assertNotIn(teacher, Teacher.teachers_list)

    def test_fire_teacher_2(self):
        teacher = DisciplineTeacher("Артем Петров", "БГПУ", 5, "Химия", "Директор")
        Teacher.teachers_list.append(teacher)  # Добавляем учителя в список
        self.assertIn(teacher, Teacher.teachers_list)
        self.assertEqual(Teacher.fire_teacher(teacher), 'Учитель Артем Петров уволен.')
        # self.assertNotIn(teacher, Teacher.teachers_list)

    def test_add_teacher(self):
        teacher = Teacher("Артем Иванов", "МГУ", 5)
        self.assertIn(teacher, Teacher.teachers_list)

    def test_add_mark(self):
        teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")
        Teacher.teachers_list.append(teacher)
        result = teacher.add_mark("Алексей", 5)
        self.assertEqual(result, 'Иван Петров поставил оценку 5 студенту Алексей\nПредмет: Химия')
        self.assertEqual(teacher.get_student_mark("Алексей"), "Оценки для студента Алексей по предмету Химия: [5]")

    def test_remove_mark(self):
        teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")
        Teacher.teachers_list.append(teacher)
        teacher.add_mark("Алексей", 5)
        result = teacher.remove_mark("Алексей", 5)
        self.assertEqual(result, 'Иван Петров удалил оценку 5 студенту Алексей\nПредмет: Химия')
        self.assertEqual(teacher.get_student_mark("Алексей"), "Оценки для студента Алексей по предмету Химия: []")

    def test_get_teacher_data(self):
        teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")
        Teacher.teachers_list.append(teacher)
        self.assertEqual(teacher.get_teacher_data(), 'Имя: Иван Петров, Образование: БГПУ, Опыт работы: 4 лет.\nПредмет: Химия, должность: Директор')

    def test_give_consultation(self):
        teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")
        Teacher.teachers_list.append(teacher)
        result = teacher.give_a_consultation("10А")
        self.assertEqual(result, 'Иван Петров провел консультацию в классе 10А\nПо предмету Химия как Директор')

    def test_set_experience(self):
        teacher = Teacher("Артем Иванов", "МГУ", 5)
        teacher.set_experience(6)
        self.assertEqual(teacher.get_experience(), 6)

if __name__ == '__main__':
    unittest.main()