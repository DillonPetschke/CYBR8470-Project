## Cognito Setup:

All users are added to a user pool named ITPOLNK

  ![cognitouserpool](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/5f99dd8a-fe25-4ac3-b2a2-2fe846b79c4e)

All users in the user pool are members of ITPOMembers

![userpoolmembers](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/da7fccf4-85d5-47d7-a814-19da716de92d)

Users are added to the list after self-enrollment

![users](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/e2b64cc5-f21d-419b-a759-fda1651f4e9d)

Cognito Settings that control password policy, MFA enablement, User account recovery, and device tracking. 

![settings](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/0f10bd46-ce17-41f1-8a44-17b64fcb3828)

Signup settings that required additional fields to be added, such as if the user is a student or professional member. Also allowing users to self-service signup. 

![signupsettings](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/1d96e858-d996-444e-aada-c21b041c9b5f)

The above settings and configuration generates the below login page, first-time users can click "Sign up" to create an account. 

![login page](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/2f1520b6-59ba-49ab-9adc-765eb6374d0a)

The following is the new user signup page, showing the password requirements. 

![new user signup page](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/3720d2e2-fda2-4654-962d-04d219542de4)

Clicking sign up generates the following screen and sends an email via AWS SNS with a verification code. 

![verification code](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/09eca7c4-e383-4f4c-8715-89207c04c9c0)

MFA Email example:

![MFA](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/32d8eb13-bf08-4b75-99d6-b59255dd45a5)
