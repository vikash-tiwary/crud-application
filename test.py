#install pytest
#pip install pytest

from flask import Flask

from app import Employe


def test_employee():
    """
    Given Employe model
    when a employe is created 
    Then check the email,first last name and email is created or not 
    """
    emp = Employe(first_name="vikash",last_name="tiwary",email="vikash@gmail.com")
    assert emp.email == 'vikash@gmail.com'
    assert emp.first_name == 'vikash'
    assert emp.last_name == 'tiwary'
    