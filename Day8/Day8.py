'''
Try SQLAlchemy to persist data into a SQLite data base
use any data, demo the read, write capabilities using python
Try the same, but add marshmallow to dump the data as JSON
'''

#Programs 1 and 2
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'

db = SQLAlchemy(app)
ma = Marshmallow(app)

class Grocery(db.Model):
    Grocery_id = db.Column(db.Integer, primary_key=True)
    vegetable_name = db.Column(db.String(80), unique=True, nullable=False)
    veggie_qty = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Grocery %r>' % self.vegetable_name

class GrocerySchema(ma.SQLAlchemySchema):
    class Meta:
        model = Grocery
        load_instance = True

    Grocery_id = ma.auto_field()
    vegetable_name = ma.auto_field()
    veggie_qty = ma.auto_field()


db.create_all()
grocery_schema = GrocerySchema()
obj1 = Grocery(vegetable_name = "Carrot", veggie_qty = 5)
obj2 = Grocery(vegetable_name = "Capsicum", veggie_qty = 3)
result=Grocery.query.filter_by(vegetable_name=obj1.vegetable_name).first()

if result:
   print("item already present")  
   
else:
   db.session.add(obj1)
   db.session.add(obj2)
   db.session.commit()
     


print(result)
print(grocery_schema.dump(obj1))
print(grocery_schema.dump(obj2))
print(Grocery.query.all())

