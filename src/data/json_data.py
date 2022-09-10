import os
import json

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))


def get_students(filename: str = "students.json") -> dict:
    data = {}
    try:
        with open(f'{CURRENT_PATH}/{filename}', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError('ERROR: Json file not found!')
    return data


def append_student(student:dict, filename: str = "students.json") -> None:
    try:
        with open(f'{CURRENT_PATH}/{filename}') as file:
            datos = json.load(file)
            datos.append(student) # load json and append dict student
        with open(f'{CURRENT_PATH}/{filename}','w') as jsonFile:
            json.dump(datos, jsonFile, indent=4, separators=(',', ': ')) # Write as json file with w option so we dont repeat
    except FileNotFoundError:
        raise FileNotFoundError('ERROR: Json file not found!')
    except Exception as err:
        raise Exception(
            'ERROR: error presented adding json data to file, err=', err)
