#install pytest
#pip install pytest

from re import template
from flask import Flask
import json
import requests

from app import Employe
from app import index
from app import app

def test_employee():
    """
    Given Employe model
    when a employe is created 
    Then check the email,first last name and email is created or not 
    """
    emp = Employe(first_name="vikash",last_name="tiwary",email="vikash@gmail.com")
    print(emp.id)
    assert emp.email == 'vikash@gmail.com'
    assert emp.first_name == 'vikash'
    assert emp.last_name == 'tiwary'
    

#Post the data
def test_index():
    """
    Test case for uploading the data into database
    """
    data = {
        "id": "1", 
        "first_name": "vikash", 
        "last_name":"tiwary",
        "email":"vikash@gmail.com"
    }

    response = requests.post("http://127.0.0.1:5000/", json=json.dumps(data))
    
    assert 200== response.status_code


#update data    
def test_update():
    """
    Test cases for update the data
    """
    data = {
        "first_name": "vickey"
    }
    response = requests.post("http://127.0.0.1:5000/edit/1", json=json.dumps(data))
    
    assert 200== response.status_code

#delete data
def test_delete():
    """
    Test cases to delete employee from table
    """
    response = requests.post("http://127.0.0.1:5000/delete/1")

    assert 200== response.status_code
