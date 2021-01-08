from flask import Flask, escape, request, json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def getInfo():
    out = {'status':False}
   
    ejemplo = int(request.args.get('ejemplo'))
    return {'status':True}

app.run('0.0.0.0', 5000 , True)
