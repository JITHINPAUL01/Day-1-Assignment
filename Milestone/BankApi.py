from flask import Flask, request, g ,jsonify,make_response,abort
from flask_restful import reqparse, Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_httpauth import HTTPBasicAuth
from passlib.apps import custom_app_context as pwd_context
import Models
import os
import mylogs

auth=HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
db = SQLAlchemy(app)
ma = Marshmallow(app)

class RegisterDetails(Resource):
    
    def post(self):
        mylogs.log_data_process("Inside the User registration Method:Post")
       
        errors = Models.RegSchema().validate(request.json,many=None,partial=None)
        #validate(data: Mapping, *, many: Optional[bool] = None, partial: Optional[Union[bool, Sequence[str], Set[str]]] = None) 
        if errors:
            abort(400, str(errors))

        newDict={}
        newDict['UserName'] = request.json['UserName']
        password = request.json.get('Password')
        db.create_all()
        user_list=Models.Registration.query.filter_by(UserName = newDict['UserName']).first()
            
        if user_list:  
            db.session.commit()              
            return make_response(jsonify(message= f"{user_list.UserName} user Already Regestried",status=400),400,)

        else:
            Obj_schema = Models.RegSchema()
            user_new = Models.Registration(**request.json)
            user_new.hash_password(password)
            
            try: 
              db.session.add(user_new)
              db.session.commit()
              mylogs.log_data_process("Craeted a new User in Database")
              return make_response(jsonify(message= f"{user_new.UserName} user Regestried Successfully",status=201),201,)
            except:
              db.session.rollback()
              return make_response(jsonify(message= f"{user_new.UserName} Schema validation failed",status=400),400,)
           

class AccountUser(Resource):
    decorators = [auth.login_required]
    def put(self,username):
        mylogs.log_data_process("Inside update user details")
        User_list=Models.Registration.query.filter_by(UserName =  username).first()
        
        if User_list:          
            Obj_schema = Models.RegSchema() 

            if "Name" in request.json:
                User_list.Name = request.json['Name']
            if "EmailAddress" in request.json:
                User_list.EmailAddress = request.json['EmailAddress']
            if "Pan" in request.json:
                User_list.Pan = request.json['Pan']
            if "ContactNo" in request.json:
                User_list.ContactNo = request.json['ContactNo']
            if "DOB" in request.json:
                User_list.DOB = request.json['DOB']
            if "Account_Type" in request.json:
                User_list.Account_Type = request.json['Account_Type']

            db.session.merge(User_list)  
            db.session.commit()
            return make_response(jsonify(message= f"{User_list.Name} details updated Successfully.",status=204),204,)

        else:
            db.session.commit()
            return make_response(jsonify(message= "User doesn't exist.Please check username and password entered",status=404),404,)
    
    
    def get(Usself,username):

        mylogs.log_data_process("Get method to get the detail of the user")
        try:
          user_list = Models.Registration.query.filter_by(UserName = username).first()
          if user_list:
              mylogs.log_data_process("Get method found the requested user detail")
              Obj_schema = Models.RegSchema() 
              db.session.commit()
              return Obj_schema.dump(user_list)

          else:
              db.session.commit()
              return make_response(jsonify(message= f"{username} Not found.Please check username",status=404),404,)    
        except:
          return make_response(jsonify(message= "Unexpected error",status=500),500,)    

class Loan(Resource):
    decorators = [auth.login_required]
    def post(self):
        mylogs.log_data_process("Post method to add loan details")
        db.create_all()
        loan_list = Models.LoanDetails.query.filter_by(Loan_User =  g.user.UserName).first()
            
        if loan_list:        
            return make_response(jsonify(message= f"{loan_list.Loan_User} user Already applied laon",status=400),400,)

        else:
            Obj_schema = Models.LoanSchema()
            user_loan = Models.LoanDetails(**request.json)
            db.session.add(user_loan)
            db.session.commit()
            mylogs.log_data_process("Loan Data created for User")    
            return make_response(jsonify(message= f"Loan for {g.user.UserName} user created successfully",status=201),201,)


class LoanDetails(Resource):
    decorators = [auth.login_required]
    def get(self,LoanID):
        mylogs.log_data_process("Get method to get the Loan detail of the user")
        Loan_list=Models.LoanDetails.query.filter_by(Loan_User = LoanID).first()
        if Loan_list:
            mylogs.log_data_process("Found Loan detail of the user")
            Obj_schema = Models.LoanSchema() 
            return Obj_schema.dump(Loan_list)

        else:
            mylogs.log_data_process("No Loan details exist of the user")

            return make_response(jsonify(message= f"{LoanID}  No Loan Deatils Available.Please check username entered.",status=404),404,)


@auth.verify_password
def verify_password(username, password):
    Obj_schema = Models.LoanSchema()
    user = Models.Registration.query.filter_by(UserName = username).first()
    
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


api.add_resource(RegisterDetails,'/Registration')
api.add_resource(Loan,'/Loan')
api.add_resource(LoanDetails,'/LoanDetails/<LoanID>')
api.add_resource(AccountUser,'/UpdateUserDetails/<username>')


if __name__=="__main__":
    app.run()