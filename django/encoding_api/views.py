from typing import List
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http.request import HttpRequest
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .serializers import DataSerializer
from .data import Data, User
import re
import json

@api_view(['POST'])
def home(request: HttpRequest)-> Response:
    encoded_string = JSONParser().parse(request)['data']
    if encoded_string == "": # check emptiness of the passing argument value
        serializer = DataSerializer(Data("The passing argument can not be empty", None))
    elif len(encoded_string) <10 or len(encoded_string) > 40: # check the size of passing arguments as expected let's assume the size needs to be between 10 and 40
        serializer = DataSerializer(Data("The passing argument's length has to be between 10 and 40", None))
    elif not re.search("^[a-zA-Z]+111[a-zA-Z]+111\d+$", encoded_string): # check valid encoded string with correct format using regex
        serializer = DataSerializer(Data("The passing argument needs to contain valid encoded alnumeric* characters with correct format ex: 'firstname(alphabetic)<111>lastname(alphabetic)<111>id(int)'", None))
    else:
        split_input:List[str] = encoded_string.split("111")    
        first_name = split_input[0] # take first value seperated by delimeter (111) as first names
        last_name = split_input[1] # take second value seperated by delimeter (111) as last name
        id = ""
        if len(split_input) > 3: # if split_input length is grater than 3 that means there are more than 2 delimeters so I will assumme rest of the delimeters are the parts of id
            id = split_input[2] # take first one and then add rest of the parts including delimter
            for i in range(len(split_input)):
                if(i>2):
                    id += '111'+split_input[i] # adding rest of the parts as id with delimeter
        else:
            id = split_input[2] # in case there are only two delimeters
        serializer = DataSerializer(Data(None, User(first_name, last_name, id)))
    final_serializer= JSONRenderer().render(serializer.data)
    return Response(final_serializer)
