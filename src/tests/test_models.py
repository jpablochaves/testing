import pytest
from shared.utils import generate_uuid
from models.student import Student


def test_valid_student_model():
    student_test = {
        "id": generate_uuid(),
        "first_name": "Paco",
        "last_name": "Piedra",
        "username": "ppiedra",
        "age": 18,
        "email": "ppiedra@test.com",
        "carreers": [
            "SW-ENG"
        ]
    }
    student = Student(**student_test) ## dict map to Student model
    assert student 
    
