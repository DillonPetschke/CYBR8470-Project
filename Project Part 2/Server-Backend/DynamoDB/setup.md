## Dynamo DB Setup 

In this project, 2 dynamo DB tables are used for data collection RequestToSpeak and RSVP Form.
![dynamosetup](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/582a653a-4a53-41ea-af1e-826ca8e83eca)

## Request To Speak

Database contains several fields to be filled by the lambda functions, email, month, name, and topic. This allows an unauthenticated person to submit their name and email, and volunteer to speak about a topic of their choice at a monthly meeting of their choice. The email field is used as the primary sorting key. 

![requesttospeakdynamo](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/0abc0763-1c27-4434-9894-4a2dc2cd0fef)

## RSVP Form

Database contains 2 fields to be filled by the lambda functions, email and name. This allows an unauthenticated person to submit their name and email and let ITPO staff know they are planning to attend the next monthly meeting.
![RSVPFormdynamo](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/7b7fed15-e63a-4024-a01d-508036f307a0)
