from flask import Flask, jsonify, request, render_template
import sys 
from termcolor import colored, cprint 
app = Flask(__name__)

@app.route('/developers/')
@app.route('/developers/<colorname>')
def developer(colorname = None):
      return render_template('myhtml.html', colorname=colorname)

if __name__=="__main__":
    app.run()

