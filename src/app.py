import os
from shared.utils import generate_uuid, indent_print
import data.json_data as json
from models.student import Student

if __name__ == '__main__':
    print('Starting application...')
    #d = json.get_students()
    #indent_print('students')
    usr = {
        "id": "a9be485a-30ad-11ed-a939-c869cdb2b987",
        "first_name": "Alberto",
        "last_name": "Chaves",
        "username": "achaves",
        "age": 16,
        "email": "achaves@test.com",
        "carreers": [
            "ELE-ENG"
        ]
    }
    # Pydantic model
    user = Student(**usr)
    print(user.__fields__, user.carreers)
    
    
    