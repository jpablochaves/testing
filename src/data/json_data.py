import os
import json

CURRENT_PATH = os.path.dirname(os.path.realpath(__file__))

def get_students(filename:str="students.json") -> dict:
    data = {}
    try:
        with open(f'{CURRENT_PATH}/{filename}', 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError('ERROR: Json file not found!')
    return data


def append_student(filename:str="students.json") -> None:
    data = {}
    try:
        with open(f'{CURRENT_PATH}/{filename}', 'r+') as file:
            data = json.load(file)
    except FileNotFoundError:
        raise FileNotFoundError('ERROR: Json file not found!')
    return data
