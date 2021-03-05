'''
Python Day 10 Assignment
'''

#Rest API
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError, validate
from flask_restful import Api, Resource

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite3"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
api = Api(app)

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(80), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)

    def __init__(self, student_name, age):
        self.student_name = student_name
        self.age = age 

    def __repr__(self):
        return '<School %r>' % self.student_name       


class StudentSchema(ma.SQLAlchemySchema):

    #Validators using Schema
    student_name = fields.Str(validate=validate.Length(min=1))
    age = fields.Int(validate=validate.Range(min=4, max=100))
    class Meta:
        fields = ("student_name","age")

db.create_all()
student_schema = StudentSchema()
student_schema = StudentSchema(many=True) 

class CreateAndRead(Resource):
    def post(self):
        new_student = Student(student_name = request.json['student_name'], age = request.json['age'])
        student_name = request.json.get('student_name')
        if Student.query.filter_by(student_name = student_name).first() is not None:
            abort(400, message = f"Student {student_name} already exists.") 
        try:         
            db.session.add(new_student) 
            db.session.commit()    
            return f"Student {request.json['student_name']} has been added and the age is {request.json['age']}. ", 201 
        #Handling Validation Error
        except ValidationError as err:
            print(err.messages)


    def get(self):
        students = Grocery.query.all()
        return student_schema.dump(students), 200


class UpdateAndDelete(Resource):
    def put(self, student):
        Student_in_db = Student.query.filter_by(student_name = student).first()
        if Student_in_db == None:
            abort(404, message="Student not found")
        Student_in_db.age =  request.json['age']
        db.session.commit()

        return f"{Student_in_db.student_name} updated successfully", 202 


    def delete(self, name):
        Student_in_db = Grocery.query.filter_by(student_name = name).first()
        if Student_in_db == None:
            abort(404, message="Student not found")
        db.session.delete(Student_in_db)
        db.session.commit()
        return "Successfully Deleted", 200


api.add_resource(CreateAndRead, '/Student')
api.add_resource(UpdateAndDelete, '/Student/<student_name>')


if __name__=="__main__":
     app.run()
