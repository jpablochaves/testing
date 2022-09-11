from models.student import Student
import data.json_data as bd_json


def get_students() -> list[Student]:
    res: list[Student] = []
    try:
        res = bd_json.get_student()
    except Exception as err:
        raise Exception(f'Error, no students fetched from JSON. {err}')
    finally:
        return res


def get_students_by_name(student_name: str) -> list[Student]:
    res: list[Student] = []
    if student_name is None or len(student_name) < 1:
        raise Exception('Error, parameter student_name cannot be empty or None!') 
    
    res = bd_json.get_students_by_name(student_name)
    return res


def add_user(student:Student) -> bool:
    try:
        user_to_add = student.dict()
        bd_json.append_student(user_to_add)
        return True    
    except:
        raise Exception(f"Error, user {student.first_name} can't be added to JSON")
    