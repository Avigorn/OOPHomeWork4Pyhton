from abc import ABC
from small_data.Student import Student
from typing import Iterable


class StudentGroup(Iterable, ABC, Student):

    def __init__(self, students):
        self.students = students

    """
    Метод получения студента
    """
    def getStudents(self):
        return self.students

    """
    Строчный метод вывода информации о студенте
    """
    def __str__(self):
        return "StudentGroup" + "students=" + str(self.students)

    """
    Итерация
    """
    def __iter__(self):
        return self
