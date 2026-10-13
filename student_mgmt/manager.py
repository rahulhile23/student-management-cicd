"""Simple Student Management System."""
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class Student:
    roll_no: str
    name: str
    department: str
    marks: float = 0.0


def _check_marks(marks: float) -> None:
    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")


class StudentManager:
    def __init__(self) -> None:
        self._students: Dict[str, Student] = {}

    def add_student(self, roll_no: str, name: str, department: str,
                    marks: float = 0.0) -> Student:
        if not roll_no or not name or not department:
            raise ValueError("roll_no, name and department are required")
        if roll_no in self._students:
            raise ValueError("Student with this roll number already exists")
        _check_marks(marks)
        student = Student(roll_no, name, department, marks)
        self._students[roll_no] = student
        return student

    def get_student(self, roll_no: str) -> Student:
        if roll_no not in self._students:
            raise KeyError("Student not found")
        return self._students[roll_no]

    def update_marks(self, roll_no: str, marks: float) -> Student:
        _check_marks(marks)
        student = self.get_student(roll_no)
        student.marks = marks
        return student

    def delete_student(self, roll_no: str) -> None:
        self.get_student(roll_no)
        del self._students[roll_no]

    def search(self, keyword: str) -> List[Student]:
        keyword = keyword.lower().strip()
        return [
            s for s in self._students.values()
            if keyword in s.name.lower() or keyword in s.department.lower()
        ]

    def list_by_department(self, department: str) -> List[Student]:
        return [
            s for s in self._students.values()
            if s.department.lower() == department.lower()
        ]

    def average_marks(self) -> float:
        if not self._students:
            return 0.0
        total = sum(s.marks for s in self._students.values())
        return round(total / len(self._students), 2)

    def topper(self) -> Optional[Student]:
        if not self._students:
            return None
        return max(self._students.values(), key=lambda s: s.marks)
