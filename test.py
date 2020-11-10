


req = {
    "templatePath": "templates/template.docx",
    "fields":[
        {
            "key": "@PRODUCT_NAME",
            "replaceWith": "enterprise"
        },
        {
            "key": "@PRODUCT_VERSION",
            "replaceWith": "2.0"
        }
    ],
    "tables":{
        "0":[
            {
                "key": "@PRODUCT_NAME",
                "replaceWith": "enterprise"
            }
        ]
    }
}


array = req['fields']
print(array)

for x in array:
    print(x['key'])
    #strCode = """if "{0}" in paragraph.text:\n    paragraph.text = re.sub("{0}", "{value}" , paragraph.text)\n""".format(x,value="PRODUCT_VALUE")
    #code += strCode 
#print(req)


# @PRODUCT_NAME
# @PRODUCT_VERSION
# @MENSAJE
# @PROYECTO