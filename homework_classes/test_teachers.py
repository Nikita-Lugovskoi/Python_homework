import unittest
from hw_classes_19_10 import Teacher, DisciplineTeacher

class TestTeacherMethods(unittest.TestCase):

    def test_fire_teacher(self):
        teacher = DisciplineTeacher("Иван Петров", "БГПУ", 4, "Химия", "Директор")
        self.assertIn(teacher, Teacher.teachers_list)
        self.assertEqual(Teacher.fire_teacher(teacher), 'Учитель Иван Петров уволен.')
        self.assertNotIn(teacher, Teacher.teachers_list)
        
    def test_fire_teacher(self):
        teacher = DisciplineTeacher("Артем Петров", "БГПУ", 5, "Химия", "Директор")
        self.assertIn(teacher, Teacher.teachers_list)
        self.assertEqual(Teacher.fire_teacher(teacher), 'Учитель Артем Петров уволен.')
        self.assertNotIn(teacher, Teacher.teachers_list)

    def test_add_teacher(self):
        teacher = Teacher("Артем Иванов", "МГУ", 5)
        self.assertIn(teacher, Teacher.teachers_list)

if __name__ == '__main__':
    unittest.main()
    