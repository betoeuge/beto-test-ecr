from flask import Flask, escape, request, json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def getInfo():
    try:
        name = request.args.get('name')
    except:
        name = 'Not name'
    out = {'name':name}
    return {'name':out}

app.run('0.0.0.0', 5000 , True)
