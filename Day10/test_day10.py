'''
Python Day10 pyTest
'''

import pytest
import requests

def test_get_students_responds_200():
     response = requests.get("http://localhost:5000/Susan")
     assert response.status_code == 200

def test_post_students_responds_201():
     response = requests.post("http://localhost:5000/Student", json={"student_name":"Susan","age":10})
     assert response.status_code == 201


def test_put_student_responds_202():
     response = requests.put("http://localhost:5000/Student/jose", json={"age":7})
     assert response.status_code == 202


def test_delete_student_responds_200():
     response = requests.delete("http://localhost:5000/Student/jose")
     assert response.status_code == 200