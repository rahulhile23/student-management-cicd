from student_mgmt import StudentManager


def main() -> None:
    sm = StudentManager()
    sm.add_student("IT01", "Asha Patil", "IT", 82)
    sm.add_student("IT02", "Ravi Kumar", "IT", 74)
    sm.add_student("CS01", "Neha Joshi", "CS", 91)
    print("Search 'asha':", sm.search("asha"))
    sm.update_marks("IT02", 80)
    print("Average marks:", sm.average_marks())
    print("Topper:", sm.topper())
    sm.delete_student("CS01")
    print("Student Management demo complete.")


if __name__ == "__main__":
    main()
