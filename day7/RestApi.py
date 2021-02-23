from flask import Flask, request
from flask_restful import Api, Resource, abort

app = Flask(__name__)
api = Api(app)

vegetables = [
    {
        'name' : 'carrot',
        'price': 50
    },
    {
        'name' : 'onion',
        'price': 70
    }
    ,
    {
        'name' : 'Brinjal',
        'price': 45
    }
]

class Vegetable(Resource):

    def get(self):
        return vegetables
    
    def post(self):
        newDict = {}
        newDict['name'] = request.json['name']
        newDict['price'] = request.json['price']
        vegetables.append(newDict)
        return request.json

class RequestClass(Resource):
    
    def get(self, item):
        
        for index in vegetables:
            if item == index['name']:
                return index
        else:
            abort(404, message=f"{item} Not Found")
    
    def delete(self, item):

        for index,listItem in enumerate(vegetables):
            if item == listItem["name"]:
                vegetables.pop(index)
                return item + " Deleted"
        else:
            abort(404, message=f"{item} Not Found")
    
    def put(self, item):

        for index, listItem in enumerate(vegetables):
            if item == listItem['name']:
                listItem['price'] = request.json['price']
                return item + ' Updated'
        else:
            abort(404, message=f"{item} Not Found")   

api.add_resource(Vegetable,'/vegetables')
api.add_resource(RequestClass,'/vegetables/<item>')

if __name__=="__main__":
    app.run()