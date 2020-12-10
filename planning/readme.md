### Your project idea 

My application is an aquarium controller built from a Raspberry Pi and a variety of sensors. It will  provide data to the backend and then be compile into updates and historical information on your aquarium such as current and past water temperatures. This info will be accessible through a clean fronted application.  

### Your tech stack (frontend, backend, database)

-  Frontend : React
- Backend : Django
- PostgreSQL
- Hardware
  - Raspberry Pi, Temperature probe and adapter 
  - Stretch Automatic Feeder: Stepper motor and motor controller board

### List of backend models and their properties

So I haven’t fully decided. But I think I am going to have users with different permissions and the Raspi Pi will be a “user” with sudo permission and then I will have an account with sudo permission as well but then restrict being able to make more accounts. I want others to have read only access and myself and the pi to have read, write, and execute privileges.

- Users
  - Email
  - Username

- Temperature
  - Temperature
  - Date
  - Time

Stretch 

- Water Flow
  - Water flow l/min || gph
  - Date
  - Time

- Lighting
  - On/off Status

- Automatic Feeder
  - On/off Status
  - Date
  - Time 



### React component hierarchy 
- app
  - nav
  - aquarium status homepage
     - historical temperature list/page
     - historical temperature graph page (stretch)


### User stories

- As a hobbyist aquarium owner, I would like to be able to remotely check the status of my aquarium.
- As a user, I would like to be able to see this info on a web page or cellular application so I can be confident my aquarium is okay even when I’m not home.
- As a user, I would like to  know what the current or recent water temperature is so I can monitor if their might be an issue or failure.
- As a user, I would like to be able to see historical temperature data so I can see if my heater is wearing out or how stable my tank temperature is.

Stretch

- As a user I would like to see historical temperature for different time intervals: day, week, month
- As a user I would like to see historical temperature displayed in a graph so I can quickly visualize the info and recognize trend and outliers
- As a user, I would like to have an automatic aquarium feeder so my fish can be feed when I am not home
- As a user I would like to know if my automatic feeding feature is activated and turn it on and off so it only feeds the fish when I’m not home .
- As a user, I would like to be able to monitor water flow so I can make sure the pumps are running and could use this as indicator for leaks or pumps needing to be cleaned.


### Wireframes
![image](https://media.git.generalassemb.ly/user/31218/files/7b34f000-3ac4-11eb-82e1-1e3fcd1b2289)


### Anything else your squad lead should know
- I have successfully created a python script that is deployed on a Raspberry Pi and can read current temperatures  from an external probe
- I have made timed authenticated http get and post request to heroku via python scripts with help of the python request and time libraries 
- I have not yet tested this across a entire day with cronjobs running scripts at an hourly interval
