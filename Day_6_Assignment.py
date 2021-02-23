from flask import Flask,render_template, request,jsonify
from flask.wrappers import Response

app = Flask(__name__)



groceriesData = [
    {
        'name':'Fruits',
        'amount':5,
    },
    {
        'name':'Snacks',
        'amount':2,
    }
]

@app.route('/groceries', methods=['GET'])
def groceries():
    return jsonify(groceriesData)

@app.route('/groceries', methods=['POST'])
def newFunc():
    newDict = {}
    newDict['name'] = request.json['name']
    newDict['amount'] = request.json['amount']
    groceriesData.append(newDict)
    return request.json

@app.route('/groceries/<string:name>', methods=['GET','DELETE'])
def identify(name):
    if request.method == 'GET':
        for item in groceriesData:
            if name == item['name']:
                return item
        else:
            return "No Such item",404
    else:
        counter = 0
        for item in groceriesData:
            if name == item["name"]:
                groceriesData.pop(counter)
                return name + " Deleted"
            else:
                counter += 1
        else:
            return "No Such item to delete",404

if __name__=="__main__":
    app.run()
