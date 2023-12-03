# CYBR8470-Project Part 2

## Executive Summary
This app will be a basic website concept for the non-profit organization called Information Technology Professionals Organization of Lincoln (ITPO - LNK). This organization holds monthly educational meetings where local programmers, cybersecurity experts, graphic designers, or local businesses can share their knowledge or projects they are working on. This site will hold information about the next upcoming meeting, an about page for the public to learn more about the group, a "request to speak" page for individuals to submit their idea of a monthly meeting, along with a member's only page showing an archive of past meetings.  

## Installation
I have changed my original architecture which originally used a Django project inside of a docker container to instead use a fully cloud-based architecture. No containers or VMs are now needed, all pages are hosted via s3 buckets that are public and accessible from anywhere. If you would like to duplicate this project, I will include details under Server-Backend of how services such as API-Gateway, Lambda, Cognito, and Dynamo DB have been set up. 

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
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/815cba92-1b40-4b14-bdf6-6f436d51a29f)
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/9ca1a47f-cb44-435b-8e2e-1892fdd98e7e)
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/f5031753-7f6d-42ad-91c7-1bc239830dc9)
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/ced26375-b677-433e-99da-075d9c8040ac)
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/c8b73acb-4300-4289-8412-29e81a398be1)
![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/eb9a68d8-7a27-4e4f-a458-a4c5b45be790)

## Hardening Considerations
To prevent poor password habits and prevent password bruteforcing by attackers, a strict password policy has been created. Also, temporary passwords set by administrators expire in 7 days and last 5 previous passwords cannot be used again. 

Password must contain a lowercase letter
Password must contain an uppercase letter
Password must contain a number
Password must contain at least 8 characters
Password must contain a special character or a space
Password must not contain a leading or trailing space

To prevent invalid email addresses from being used during signup, a verification code is emailed to the user before activating the account. 
Multi-factor is required for users to login to prevent unauthorized access. 

