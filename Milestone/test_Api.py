import pytest
import sys
import BankApi
import time
from flask import jsonify


# applying loan for a  user
def test_Loan_post_201():
    tester = BankApi.app.test_client()
    # time.sleep(10)
    response = tester.post('/Loan', json={
    "Loan_User": "NewUser4",
    "Loan_Type": "Personal",
    "Loan_Amount": 100000.0,
    "Date": "28-03-2021",
    "Rate_Of_Interest": 9.5,
    "Duration": 5    
},headers={"Authorization": "Basic TmV3VXNlcjQ6bmV3NEAzMjQ0"}
)
    assert response.status_code == 201

# user created successfully
def test_RegisterDetails_post_201():
     tester = BankApi.app.test_client()
     response = tester.post('/Registration', json={"UserName":"NewUser5","Name":"Helan2 paul","Password":"new5@3244","EmailAddress":"Helan1@test.com","Pan":"HHERTGFT1","ContactNo":"955123453","DOB":"28-03-1997","Account_Type":"Saving"})
     assert response.status_code == 201

#get account user details
def test_AccountUser_Get_200():
    tester = BankApi.app.test_client()
    response = tester.get('/UpdateUserDetails/JITHIN',headers={"Authorization": "Basic SklUSElOOmppdGh1N0Ax"})
    status = response.status_code
    assert status == 200

#get loan details    
def test_LoanDetails_Get_200():
    tester = BankApi.app.test_client()
    response = tester.get('/LoanDetails/NewUser4',headers={"Authorization": "Basic TmV3VXNlcjQ6bmV3NEAzMjQ0"})
    status = response.status_code
    assert status == 200


#update an exixting user details
def test_AccountUser_put_204():
    tester = BankApi.app.test_client()
    response = tester.put('/UpdateUserDetails/JITHIN', json={"UserName":"JITHIN","Name":"Update Paul","Password":"jithu7@123","EmailAddress":"david@test123.com","Pan":"New1234P","ContactNo":"9551514256","DOB":"28-03-1990","Account_Type":"Current"},headers={"Authorization": "Basic SklUSElOOmppdGh1N0Ax"})
    assert response.status_code == 204

# request to edit details of invalid userid
def test_AccountUser_put_404():
    tester = BankApi.app.test_client()
    response = tester.put('/UpdateUserDetails/JITHIN01', json={"UserName":"JITHIN","Name":"Jithinj Paul","Password":"jithu7@123","EmailAddress":"david@test123.com","Pan":"New1234P","ContactNo":"9551514256","DOB":"28-03-1990","Account_Type":"Current"},headers={"Authorization": "Basic SklUSElOOmppdGh1N0Ax"})
    assert response.status_code == 404

#user alreday exist
def test_RegisterDetails_post_400_Existinguser():
    tester = BankApi.app.test_client()
    response = tester.post('/Registration', json={"UserName":"JITHIN","Name":"anu paul","Password":"Arath@3244","EmailAddress":"Arath1@test.com","Pan":"CCERTGFT1","ContactNo":"955123453","DOB":"28-03-1993","Account_Type":"Saving"})
    assert response.status_code == 400

# user name with number of characters less than 6 bad request
def test_RegisterDetails_post_400():
    tester = BankApi.app.test_client()
    response = tester.post('/Registration', json={"UserName":"Helan","Name":"Helan paul","Password":"Helan@3244","EmailAddress":"Helan1@test.com","Pan":"HHERTGFT1","ContactNo":"955123453","DOB":"28-03-1997","Account_Type":"Saving"})
    assert response.status_code == 400


# applying loan for already applied user
def test_Loan_post_400():
    tester = BankApi.app.test_client()
    response = tester.post('/Loan', json={
    "Loan_User": "Merin01",
    "Loan_Type": "Personal",
    "Loan_Amount": 100000.0,
    "Date": "28-03-2021",
    "Rate_Of_Interest": 9.5,
    "Duration": 5    
},headers={"Authorization": "Basic TWVyaW4wMTpQYXNzd29yZEAx"}
)
    assert response.status_code == 400


