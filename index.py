from flask import Flask, request, jsonify , Response
from flask_basicauth import BasicAuth
import routes as route
import render as ren
import constants as const
import json
import os 

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'GtG@GTM9W'
app.config['BASIC_AUTH_PASSWORD'] = 'GtG@GTM9W'
basic_auth = BasicAuth(app)

@app.route(route.ROUTE_CONTROLLER, methods=['POST'])
#@basic_auth.required
def funA001():
    jsonIn = request.json
    res = ren.renderTemplate(const.INIT_PATH_TEMPLATE,'generate-controller.jinja2',jsonIn)
    return Response(res, mimetype='text/javascript')

@app.route(route.ROUTE_SERVERLESS, methods=['POST'])
#@basic_auth.required
def funA002():
    jsonIn = request.json
    res = ren.renderTemplate(const.INIT_PATH_TEMPLATE,'generate-serverless.jinja2',jsonIn)
    return Response(res, mimetype='text/yaml')

@app.route(route.ROUTE_CLASS, methods=['POST'])
#@basic_auth.required
def funA003():
    jsonIn = request.json
    res = ren.renderTemplate(const.INIT_PATH_TEMPLATE,'generate-class.jinja2',jsonIn)
    return Response(res, mimetype='text/plain')

@app.route(route.ROUTE_REQUEST, methods=['POST'])
#@basic_auth.required
def funA004():
    jsonIn = request.json
    #Update Values
    jsonIn['traceId'] = ren.generateUuidInt()
    res = ren.renderTemplate(const.INIT_PATH_TEMPLATE,'generate-request.jinja2',jsonIn)
    return Response(res, mimetype='application/json')

@app.route(route.ROUTE_TEMPLATES, methods=['GET'])
#@basic_auth.required
def funA005():
    #jsonIn = request.json
    os.chdir(".")
    os.chdir('./templates')
    path = os.getcwd()
    dir_list = os.listdir(path) 
    print(dir_list)
    #Update Values
    #jsonIn['traceId'] = ren.generateUuidInt()
    response = {
        "files": dir_list
    }
    res = json.dumps(response)
    #res = ren.renderTemplate(const.INIT_PATH_TEMPLATE,'generate-request.jinja2',jsonIn)
    return Response(res, mimetype='application/json')

@app.route("/documents", methods=['POST'])
#@basic_auth.required
def funA006():
    jsonIn = request.json
    print(jsonIn)
    fields = jsonIn['fields']
    res = ren.generateCodeFields(fields)
    ren.fnReplaceFields(jsonIn['templatePath'],res)
    print(res)
    return jsonIn

if __name__ == '__main__':
    app.run(debug=True)