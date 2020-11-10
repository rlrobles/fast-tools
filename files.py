import os
from shutil import copyfile
import docx
import re
import openpyxl


def fnReplaceFields(documentPath,data):
    document = docx.Document(docx = documentPath)
    for paragraph in document.paragraphs:
        if "NRO_REQUEST" in paragraph.text:
            paragraph.text = re.sub("NRO_REQUEST", requestFolder , paragraph.text)
        
        
        if "PRODUCT_NAME" in paragraph.text:
            paragraph.text = re.sub("PRODUCT_NAME", productName , paragraph.text)
        if "PRODUCT_VERSION" in paragraph.text:
            paragraph.text = re.sub("PRODUCT_VERSION", productVersion , paragraph.text)
        if "API_NAME" in paragraph.text:
            paragraph.text = re.sub("API_NAME", apiName , paragraph.text)
        if "API_VERSION" in paragraph.text:
            paragraph.text = re.sub("API_VERSION", "v2" , paragraph.text)
        if "API_METHOD" in paragraph.text:
            paragraph.text = re.sub("API_METHOD", apiMethod , paragraph.text)
        if "API_OPERATION" in paragraph.text:
            paragraph.text = re.sub("API_OPERATION", apiOperation , paragraph.text)
    
    document.save(documentPath)