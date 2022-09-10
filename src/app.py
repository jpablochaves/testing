import os
from shared.utils import generate_uuid, indent_print
import data.json_data as json


if __name__ == '__main__':
    print('Starting application...')
    d = json.get_students()
    indent_print('students')
    