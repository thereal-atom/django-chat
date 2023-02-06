import random
import string
from django.forms.models import model_to_dict

def generate_id(prefix: str, length = 16):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))

    return prefix + '_' + result_str

# convert list of database models to list of dictionaries

def model_to_list_dicts(query_set) -> list:
    dicts = []

    for i in range(0, len(list(query_set))):
        dicts.append(model_to_dict(query_set[i]))

    return dicts
