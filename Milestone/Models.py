from flask import Flask, request, g
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields
from marshmallow.validate import Range, Length
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
# import BankApi





# #created a class object
# db = SQLAlchemy(BankApi.app)
# ma = Marshmallow(BankApi.app)
db = SQLAlchemy()
ma = Marshmallow()

class Registration(db.Model):

    UserName = db.Column(db.String(20), primary_key=True)
    Name = db.Column(db.String(40), nullable=False)
    Password = db.Column(db.String(9), unique=True, nullable=False)
    EmailAddress = db.Column(db.String(20), nullable=False)
    Pan = db.Column(db.String(20), nullable=False)
    ContactNo = db.Column(db.Integer, nullable=False)
    DOB = db.Column(db.String(20), nullable=False)
    Account_Type=db.Column(db.String(20), nullable=False) # savings /current
    password_hash = db.Column(db.String(128))
    def hash_password(self, password):
        self.password_hash = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password_hash)
        
        # try:
        #     db.create_all() # created the table
        # except:
        #     print("Error in Table creation")   

    def __repr__(self):
        return '<Registration %r>' % self.UserName

class RegSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Registration
        load_instance = True

    UserName = fields.String(required = True, validate = Length(min=6))
    Name = fields.String()
    EmailAddress = fields.String()
    Pan = fields.String()
    ContactNo = fields.Integer()
    DOB = fields.String()
    Account_Type = fields.String()
    Password = fields.String(required = True, validate = Length(min=8))

class LoanDetails(db.Model):

    __tablename__ = 'LoanDetails'
    Id= db.Column(db.Integer, primary_key=True)
    Loan_User = db.Column(db.String(20), db.ForeignKey('registration.UserName'), nullable=False)
    Loan_Type = db.Column(db.String(20), nullable=False)
    Loan_Amount = db.Column(db.Float,nullable=False)
    Date = db.Column(db.String(20), nullable=False)
    Rate_Of_Interest = db.Column(db.Float,nullable=False)
    Duration = db.Column(db.Integer,nullable=False)
    
    # try:
    #     db.create_all() # created the table
    # except:
    #     print("Error in Table creation")

    def __repr__(self):
        return '<LoanDetails %r>' % self.Loan_User

class LoanSchema(ma.SQLAlchemySchema):
    class Meta:
        model = LoanDetails
        load_instance = True

    Id= ma.auto_field()
    Loan_User = ma.auto_field()
    Loan_Type = ma.auto_field()
    Loan_Amount = ma.auto_field()
    Date = ma.auto_field()
    Rate_Of_Interest = ma.auto_field()
    Duration = ma.auto_field()

