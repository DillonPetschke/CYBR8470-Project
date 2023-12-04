# CYBR8470-Project Part 2

## Executive Summary
This app will be a basic website concept for the non-profit organization called Information Technology Professionals Organization of Lincoln (ITPO - LNK). This organization holds monthly educational meetings where local programmers, cybersecurity experts, graphic designers, or local businesses can share their knowledge or projects they are working on. This site will hold information about the next upcoming meeting, an about page for the public to learn more about the group, a "request to speak" page for individuals to submit their idea of a monthly meeting, along with a member's only page showing an archive of past meetings.  

## Installation
I have changed my original architecture which originally used a Django project inside of a docker container to instead use a fully cloud-based architecture. No containers or VMs are now needed, all pages are hosted via AWS s3 buckets that are public and accessible from anywhere. All server backend processes are handled by scaleable AWS services. If you would like to duplicate this project, I will include details under Server-Backend of how services such as API-Gateway, Lambda, Cognito, and Dynamo DB have been set up. 

## Direct S3 webpage links:

Home page:
- https://itpolnk-homepage.s3.us-east-2.amazonaws.com/HomePage.html
  
About page:
- https://itpolnk-about.s3.us-east-2.amazonaws.com/About.html

Request To Speak page:
- https://itpolnk-requesttospeak.s3.us-east-2.amazonaws.com/RequestToSpeak.html

AWS Cognito Login page **(Join Now and Member's only archive pages are served via this login page)**
- https://itpolnk.auth.us-east-2.amazoncognito.com/login?client_id=1lirdggul7glfd5toje0qpml8a&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2Fitpolnk-archive.s3.us-east-2.amazonaws.com%2Fmembersonly.html

## Architecture Diagrams
The below image demonstrates the general concept of the architecture behind this web app. All javascript built into the HTML pages communicates to an AWS API Gateway, which routes the data provided by the script to the corresponding lambda function, which modifies the corresponding dynamo Database as needed. 
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/815cba92-1b40-4b14-bdf6-6f436d51a29f)


The below image demonstrates the remaining pages (Join Now, Archive) utilizing AWS Cognito's login portal rather than a custom-built s3 website. The Cognito portal will then redirect authenticated users to the restricted S3 bucket for viewing. 

![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/9ca1a47f-cb44-435b-8e2e-1892fdd98e7e)



The below images focuses on RequestToSpeak.html webpage, this webpage contains javascript that POSTs data towards an API Gateway "RequestToSpeak". This specific API Gateway communicates with Lambda function "RequestToSpeak". Which interacts with Dynamo DB named RequestToSpeak. 
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/f5031753-7f6d-42ad-91c7-1bc239830dc9)



The below images focuses on Homepage.html webpage, this webpage contains javascript that POSTs data towards an API Gateway "RSVPForm". This specific API Gateway communicates with Lambda function "RSVPForm". Which interacts with Dynamo DB named RSVPForm. 
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/ced26375-b677-433e-99da-075d9c8040ac)



The below images focuses on archive.html webpage, this webpage will redirect unauthenticated users to the AWS Cognito to verify credentials and generate a token. The user is then re-directed toward archive.html that will read the token, verify the user linked to it is inside of the "members" user pool, and then display the webpage if so. 
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/c8b73acb-4300-4289-8412-29e81a398be1)



The below images focuses on joinnow.html webpage, this webpage redirects users to the AWS Cognito Sign up experience page. This page requires an Email, full name, and a complex password to create an account. AWS Cognito then utilizes AWS SNS to send a verification code to the inputted address. Once the verification code is entered, the email received will redirect users to Cognito again to set up multi-factor authentication.  
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/eb9a68d8-7a27-4e4f-a458-a4c5b45be790)



## Hardening Considerations
To prevent poor password habits and prevent password brute-forcing by attackers, a strict password policy has been created. 
- Password must contain a lowercase letter
- Password must contain an uppercase letter
- Password must contain a number
- Password must contain at least 8 characters
- Password must contain a special character or a space
- Password must not contain a leading or trailing space

Temporary passwords set by administrators expire in 7 days and the last 5 previous passwords cannot be used again per account. 

To prevent invalid email addresses from being used during signup, a verification code is emailed to the user before activating the account. 

Multi-factor is required for users to login to prevent unauthorized access. 

