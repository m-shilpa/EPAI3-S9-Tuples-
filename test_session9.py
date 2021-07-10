from session9 import *
from datetime import datetime
import pytest
from io import StringIO 
import sys
import time
import inspect
import os

README_CONTENT_CHECK_FOR = [
    "and",
    "or",
    "repr",
    "str",
    "add",
    "eq",
    "float",
    "ge",
    "gt",
    "invert",
    "le",
    "lt",
    "mul",
    "sqrt",
    "bool",
    "init"
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r", encoding="utf-8")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session9)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"

def test_getlargest_blood_group():
    profiles = ()
    output = largest_blood_group(profiles,dtype='namedtuple')
    print(output)
    assert any(["No profiles available" in output])

def test_get_oldest_person_age():
    profiles = ()
    output = get_oldest_person_age(profiles,dtype='namedtuple')
    print(output)
    assert any(["No profiles available" in output])

def test_get_mean_current_location():
    profiles = ()
    output = get_mean_current_location(profiles,dtype='namedtuple')
    print(output)
    assert any(["No profiles available" in output])

def test_get_averge_age():
    profiles = ()
    output = get_averge_age(profiles,dtype='namedtuple')
    print(output)
    assert any(["No profiles available" in output])
