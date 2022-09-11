import os
import json
import re
from models.student import Student


CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))


def get_students(filename: str = "students.json") -> list:
    data = []
    try:
        with open(f'{CURRENT_PATH}/{filename}', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError('ERROR: Json file not found!')
    return data


def get_students_by_name(student_name: str, filename: str = "students.json") -> list:
    results = []
    try:
        with open(f'{CURRENT_PATH}/{filename}', 'r') as file:
            data = json.load(file)
            for reg in data:
                if re.search(student_name, reg['first_name'], re.IGNORECASE):
                    results.append(reg)
    except FileNotFoundError:
        raise FileNotFoundError('ERROR: Json file not found!')
    return results


def append_student(student: dict, filename: str = "students.json") -> None:
    try:
        with open(f'{CURRENT_PATH}/{filename}') as file:
            datos = json.load(file)
            datos.append(student)  # load json and append dict student
        with open(f'{CURRENT_PATH}/{filename}', 'w') as jsonFile:
            # Write as json file with w option so we dont repeat
            json.dump(datos, jsonFile, indent=4, separators=(',', ': '))
    except FileNotFoundError:
        raise FileNotFoundError('ERROR: Json file not found!')
    except json.decoder.JSONDecodeError as jerr:
        raise Exception('Error: JSON decoder error ', jerr)
    except Exception as err:
        raise Exception(
            'ERROR: error presented adding json data to file, err=', err)
