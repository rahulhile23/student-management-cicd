import pytest

from student_mgmt import StudentManager


@pytest.fixture
def sm():
    manager = StudentManager()
    manager.add_student("IT01", "Asha Patil", "IT", 80)
    manager.add_student("CS01", "Ravi Kumar", "CS", 60)
    return manager


def test_add_student(sm):
    assert sm.add_student("IT02", "Neha Joshi", "IT").name == "Neha Joshi"


def test_add_duplicate_roll_fails(sm):
    with pytest.raises(ValueError):
        sm.add_student("IT01", "Other", "IT")


def test_add_missing_fields_fails(sm):
    with pytest.raises(ValueError):
        sm.add_student("", "Name", "IT")


def test_invalid_marks_fails(sm):
    with pytest.raises(ValueError):
        sm.add_student("IT05", "Name", "IT", 150)


def test_get_student(sm):
    assert sm.get_student("IT01").name == "Asha Patil"


def test_get_unknown_student_raises(sm):
    with pytest.raises(KeyError):
        sm.get_student("XX99")


def test_update_marks(sm):
    assert sm.update_marks("CS01", 75).marks == 75


def test_update_marks_invalid_fails(sm):
    with pytest.raises(ValueError):
        sm.update_marks("CS01", -5)


def test_delete_student(sm):
    sm.delete_student("CS01")
    with pytest.raises(KeyError):
        sm.get_student("CS01")


def test_search_and_department(sm):
    assert len(sm.search("asha")) == 1
    assert len(sm.search("cs")) == 1
    assert len(sm.list_by_department("IT")) == 1


def test_average_and_topper(sm):
    assert sm.average_marks() == 70.0
    assert sm.topper().roll_no == "IT01"


def test_empty_manager():
    empty = StudentManager()
    assert empty.average_marks() == 0.0
    assert empty.topper() is None
