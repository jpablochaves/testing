import uuid
import json
from data.json_data import get_students


def generate_uuid() -> uuid.UUID:
    """Generate an UUID (Universally Unique identifier)"""
    return uuid.uuid4()


def print_students(entity:str) -> None:
    result = get_students()
    print(json.dumps(result, indent=4, sort_keys=True))

# To map dict to functions and avoid multiple conditions 
JSON_ENTITIES = {
    "students": print_students,
}
def indent_print(entity:str,sort_keys:bool=True) -> None:
    """
    Print in prettier format the JSON entity 
    Args:
        entity (str): Name of the entity as in the file
        sort_keys (bool, optional): Print sorting by keys or not. Defaults to True.
    Returns:
        None: Just prints the JSON Entity values
    """
    return JSON_ENTITIES[entity](sort_keys)


    

    
