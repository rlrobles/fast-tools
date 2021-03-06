from flask import Flask, request, jsonify , Response
#from flask_basicauth import BasicAuth
import routes as route
import render as ren
import constants as const
import json
import os
from rethinkdb import r 
import platform

UPLOAD_DIRECTORY = ""

if platform.system() == "Linux":
    UPLOAD_DIRECTORY = "/templates"
else:
    UPLOAD_DIRECTORY = "./templates"
    print("windows")

#sUPLOAD_DIRECTORY = "./templates"
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'GtG@GTM9W'
app.config['BASIC_AUTH_PASSWORD'] = 'GtG@GTM9W'
#basic_auth = BasicAuth(app)

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

@app.route("/registros", methods=['GET'])
#@basic_auth.required
def funA007():
    r.connect('localhost', 28015).repl()
    cursor = r.table("tv_shows").run()
    for document in cursor:
        print(document)
    #return cursor
    #return cursor
    return Response(jsonify(cursor), mimetype='application/json')


#@app.route("/upload/document/<filename>", methods=['POST'])
@app.route("/upload/document", methods=['POST'])
#@basic_auth.required
def funA008():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            print(image)
            image.save(os.path.join(UPLOAD_DIRECTORY, image.filename))
    #jsonIn = request.json
    #photos = UploadSet('photos', IMAGES)
    # with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
    #     fp.write(request.data)
    # if request.method == 'POST' and 'photo' in request.files:
    #     filename = photos.save(request.files['photo'])
    #     rec = Photo(filename=filename, user=g.user.id)
    #     rec.store()
    #     flash("Photo saved.")
        #return redirect(url_for('show', id=rec.id))
    #return render_template('upload.html')
    #res = ren.renderTemplate(const.INIT_PATH_TEMPLATE,'generate-controller.jinja2',jsonIn)
    #return Response(res, mimetype='text/javascript')
    return "subido"

@app.route("/files", methods=['GET'])
#@basic_auth.required
def funA009():
    files = []
    for filename in os.listdir(UPLOAD_DIRECTORY):
        path = os.path.join(UPLOAD_DIRECTORY, filename)
        if os.path.isfile(path):
            files.append(filename)
    return jsonify(files)

# if __name__ == '__main__':
#     app.run(debug=True)