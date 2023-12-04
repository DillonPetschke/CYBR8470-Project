## Lambda Setup 

In this project, 2 python 3.11 lambda functions are used for database updates.
![lambdasetup1](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/b2fc984f-a9db-4b86-b400-3c451881d7cd)


## Request To Speak
Triggered by API Gateway "RequestToSpeak", this lambda function takes json formatted data and performs a put_item towards Dynamo DB table requesttospeak. 

![requesttospeaklambda](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/3c6fecb4-67a1-4ea4-a001-cb1656e84024)



**code is copied below:**

import json

import boto3

import time

import re 


dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
        email = event['email']
        month = event['month']
        name = event['name']
        topic = event['topic']

        dynamodb.put_item(TableName='RequestToSpeak', Item={'email':{'S':email}, 'month':{'S':month}, 'name':{'S':name}, 'topic':{'S':topic}})

    

## RSVPForm
Triggered by API Gateway "RSVPForm", this lambda function takes json formatted data verifies the email input is a valid email address, and performs a put_item towards Dynamo DB table RSVPForm. 
![rsvpformlambda](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/5737033a-cc05-493f-850e-c0145118a518)


**code is copied below:**

import json

import boto3

import time

import re 



dynamodb = boto3.client('dynamodb')

def lambda_handler(event, context):
        email = event['email']
        name = event['name']



        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
        
        if re.match(pattern,email):
                dynamodb.put_item(TableName='RSVPForm', Item={'email':{'S':email}, 'Name':{'S':name}})

        else:
                print("Invalid Email")
