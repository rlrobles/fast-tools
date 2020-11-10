import yaml
from jinja2 import Environment, FileSystemLoader
from json import JSONEncoder
import uuid
import datetime
import docx
import re

def generateUuidDefault():
    id = uuid.uuid1()
    return id

def generateUuidHex():
    id = uuid.uuid1()
    return id.hex

def generateUuidInt():
    id = uuid.uuid1()
    return id.int

def getDateNow():
    dateTime = datetime.datetime.now()
    formatDateTime = dateTime.isoformat()
    return formatDateTime

def renderTemplate(templatePath,templateName,json):
    env = Environment(loader = FileSystemLoader(templatePath))
    template = env.get_template(templateName)
    if json['save'] == "Y":
        ruta = r"C:\Users\Royer Leandro\Documents\proyectos\fast-dev-api\output"
        fileNameTemplate = """{ruta}\salida.json""".format(ruta=ruta)
        file = open(fileNameTemplate, "w") 
        file.write(template.render(json)) 
        file.close()
        print("Generate Sucess")
        #read
        f = open(fileNameTemplate,'r')
        filedata = f.read()
        f.close()
        newdata = filedata.replace("'",'"')
        #write
        f = open(fileNameTemplate,'w')
        f.write(newdata)
        f.close()
        print("Generate Sucess 2")
        f = open(fileNameTemplate,'r')
        filedataout = f.read()
        f.close()
        return filedataout
    else:
        print(template.render(json))
        print("No save")
        return template.render(json)
    #print(template.render(json))
    #return template.render(json)

def generatePath(basePath,renderPath,templateRenderName):
    templatePath = "/{0}/{1}/{2}".format(basePath,renderPath,templateRenderName)
    print(templatePath)
    return templatePath

def generateCodeFields(items):
    code = ""
    for item in items:
        strCode = """if "{0}" in paragraph.text:\n    paragraph.text = re.sub("{0}", "{value}" , paragraph.text)\n""".format(item['key'],value=item['replaceWith'])
        code += strCode
    return code

def fnReplaceFields(documentPath,code):
    document = docx.Document(docx = documentPath)
    for paragraph in document.paragraphs:
        exec(code)
    document.save(documentPath)

#print(generateUuidDefault())
#print(generateUuidHex())
#print(generateUuidInt())
#print(getDateNow())
#renderTemplate()
