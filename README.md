Below is the original readme from part 1 of the semester project. Part 2 readme can be found under project2 folder or click here: https://github.com/DillonPetschke/CYBR8470-Project/blob/90b144b2dcbf9a3c59f9e664d0bdf273a611bc26/Project2/README.md

# CYBR8470-Project

## Executive Summary
This app will be a basic website concept for the non-profit organization called Information Technology Professionals Organization of Lincoln (ITPO - LNK) This site will announce upcoming events, allow RSVPing to events, and tell visitors more about the non-profit. 

## Installation
- Open PowerShell 
- Cd to the folder of your choice (that contains required files)
- Docker build -t project .
- Docker run -it -p 8000:8000 project

## Getting Started 
- Install via Installation above
- Check out the following pages
  - 127.0.0.1:8000/homepage
  - 127.0.0.1:8000/joinnow
  - 127.0.0.1:8000/about
  - 127.0.0.1:8000/requesttospeak



## User Stories

As a **public viewer**, I want to **view the About page**, so I can **learn more about the organization**
- Acceptance Criteria:
  - Contain the non-profit’s general description and mission statement
  - Contain contact information for reaching out
  - Contain non-profits logo
  - Link to social media 

As a **public viewer**, I want to **view the signup page**, so I can **be emailed future updates**
- Acceptance Criteria:
  - Contain a form to collect information
    - Name
    - Email Address
    - Member Type (student\professional)
      
As a **public viewer**, I want to **view the speaker signup page**, so I can **apply to speak at a future event**
- Acceptance Criteria:
  - Contain a form to collect information
    - Name
    - Email Address
    - Topic of potential presentation

As a **public viewer**, I want to **view upcoming events**, so I can **RSVP if interested**
- Acceptance Criteria:
  - Contain information about the next event
    - Event location
    - Event time
    - Speaker \ presenter 
    - Presentation description
    - Photo
  - Contain a form to RSVP yourself
    - Name
    - Email Address
      

## MisUser Stories

As a **misuser**, I want to **spam the RSVP** by **entering fake information**
- Mitigation criteria:
  - Only allow 1 RSVP per email address, or limit 1 RSVP by IP address per day
  
As a **misuser**, I want to **signup unwanting individuals** by **entering their contact info to receive notifications**
- Mitigation criteria:
  - Require the user to click accept on a one-time confirmation email
  - Only allow 1 signup per IP address per day
		
As a **misuser**, I want to **post fake future events**, by **entering false information to event creation features**
- Mitigation criteria:
  - Require administrators to log in to modify events, don’t allow the public to modify events.


## Site Mock Up \ Examples

**About Page:**

![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/3cf3ddd8-47d8-42e5-8bfe-19abe437bdb5)




**Event Page:**

![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/514e59f1-1510-47ba-a9a3-86a42b35de84)




**Join Today Page:**

![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/762ca8af-fe48-4998-a8c7-e2c037013478)



**Request to speak page:**

![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/a10be259-2357-43ac-b8c5-2a5cd0c7a408)


## C4 Diagrams 

**Level 1**

![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/d41b0589-c4f1-418b-aa25-4529d90fa8ad)


**Level 2**

![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/9900aa54-c700-42df-9d83-6e0b76c16c75)

**Level 3**

![image](https://github.com/DillonPetschke/CYBR8470-Project/assets/51690971/dcd57b7b-9ee1-4d1d-9b34-716f3a14c42a)


## License
The MIT License (MIT)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
