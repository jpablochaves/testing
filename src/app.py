import os
from shared.utils import generate_uuid, indent_print
import data.json_data as json
from models.student import Student
import services.services as service

if __name__ == '__main__':
    print('Starting application...')
    #d = json.get_students()
    #indent_print('students')
    usr = {
        "id": "a9be485a-30ad-11ed-a939-c869cdb2b987",
        "first_name": "prueba",
        "last_name": "prueba",
        "username": "pruchaves",
        "age": 16,
        "email": "pruchaves@test.com",
        "carreers": [
            "ENG"
        ]
    }
    # Pydantic model
    user = Student(**usr)
    #print(user.__fields__, user.carreers)
    res = service.add_user(user)
    print(res)
    