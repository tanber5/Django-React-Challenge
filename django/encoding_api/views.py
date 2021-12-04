from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.request import HttpRequest
import re
import json

@api_view(['POST'])
def home(request: HttpRequest)-> Response:
    parseData = json.loads(request.body)
    encoded_string = parseData['data']
    if encoded_string == "": # check emptiness of the passing argument value
        json_data = { 'errors': "The passing argument can not be empty", 'value': None }
    elif len(encoded_string) <10 or len(encoded_string) > 40: # check the size of passing arguments as expected let's assume the size needs to be between 10 and 40
        json_data = { 'errors': "The passing argument's length has to be between 10 and 40", 'value': None }
    elif not re.search("^[a-zA-Z]+111[a-zA-Z]+111\d+$", encoded_string): # check valid encoded string with correct format using regex
        json_data = { 'errors': "The passing argument needs to contain valid encoded alnumeric* characters with correct format ex: 'firstname(alphabetic)<111>lastname(alphabetic)<111>id(int)'", 'value': None }
    else:
        split_input = encoded_string.split("111")    
        first_name = split_input[0] # take first value seperated by delimeter (111) as first names
        last_name = split_input[1] # take second value seperated by delimeter (111) as last name
        if len(split_input) > 3: # if split_input length is grater than 3 that means there are more than 2 delimeters so I will assumme rest of the delimeters are the parts of id
            id = split_input[2] # take first one and then add rest of the parts including delimter
            for i in range(len(split_input)):
                if(i>2):
                    id += '111'+split_input[i] # adding rest of the parts as id with delimeter
        else:
            id = split_input[2] # in case there are only two delimeters
        value = json.loads('{"firstname": "'+first_name+'", "lastname": "'+last_name+'", "id": '+str(id)+'}')
        json_data = { 'errors': None, 'value': value }
    return Response(json_data)
