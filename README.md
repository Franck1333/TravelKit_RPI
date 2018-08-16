# TravelKit_RPI  
  
This Project give you useful details about the environement where you are by Using an USB GPS and some API with an Internet Connection. 
  
## Getting Started  
  
To get a copy of the project , you can go on the GitHub's webpage of the project and click on the green button to download as a .ZIP file. However , if you're using a prompt on a unix machine use this line :

```
git clone https://github.com/Franck1333/TravelKit_RPI.git
```
  
### Prerequisites  
  
To use the project , you will need some Hardware :
  
```  
A Raspberry Pi (Version 3 is better)
A USB G.P.S (Ublox-7) -->  http://amzn.eu/aG9vR3t
A Micro S.D card (8 Gb Minimum)
A screen (Diplayotron 3000 or other Displays) 
```  
  And you will also need some libraries and softwares :

```
- Python version 2 and 3
	- Python Libraries:
		-serial
		-time
		-os
		-sys
		-from urllib2 import urlopen
		-json
		-googlemaps (API GOOGLEMAPS pip install -U googlemaps)
		-datetime
		-unicodedata
		-requests
		-pyowm (API METEO // pip install pyowm)
    { FOR THE DOT3K in python files :
      import dot3k.lcd as lcd
      import dot3k.backlight as backlight
    }
	- Raspian Wheezy/STRETCH or later

```

Now especially for the Display'O'Tron 3000 in our case :

```
	- The Github page : https://github.com/pimoroni/displayotron
	- The command line Setup (need to be install) : curl -sS get.pimoroni.com/displayotron | bash
	- Directory 'plugins'
	- Directory 'utils'
	- File 'dot3k.cfg'
	- Directory 'library'
```
  
### Downloading/Installing - EASY WAY !!!  
To get and downloaded the files , use this line : 
```
git clone https://github.com/Franck1333/TravelKit_RPI.git
```

- When the project is Downloaded , check your "pi" folder , and you will see the folder "TravelKit_RPI"
When you did it , you will have to launch the file called "setup.py" to install the dependencies neccessary for the project with this command line : 

```
  sudo python setup.py install
```

### Or you can do it by yourself with those command lines :

#### The Weather API :
```
  sudo pip install pyowm
```

#### The Google Maps API :

```
  sudo pip install -U googlemaps
```

### This commmand line must be executed anyway to install the DOT3K DISPLAY: 
#### The Display'O'Tron Softwares and libs :

```
  curl -sS get.pimoroni.com/displayotron | bash
```
## Run
#### First Way to run the project :
To run the project , you can run the small script file called "Start_DOT3K_TravelKit.sh" in the folder "START" ; it's will launch the project in the background

#### Second Way to run the project :
To run the project ; if you want to see the console activities , you can launch the file called "Start_DOT3K_TravelKit.sh"  into the Command Line Prompt with "./Start_DOT3K_TravelKit.sh"

#### Third Way to run the project :
To run the project ; if you want to see the console activities , you can launch the file called "Start_DOT3K_TravelKit.py" into the Command Line Prompt with "sudo python Start_DOT3K_TravelKit.py" in the folder "START"

#### The Fourth Way to run the project :
To run the project ; if you want the project run automatically when system start-up ; Go to launch a Prompt and type:

```
>>sudo nano /etc/rc.local

AND WRITE before "exit 0":
>> sleep 35  #Give time to the system to boot and get all the data necessary
>> bash /home/pi/TravelKit_RPI/START/Start_DOT3K_TravelKit.sh &

```

## Running the tests  
  
That's how to test features:

    sudo python file.py

## The Folders and Files

In this project we've got six Directories

#### Directories
```
Affichage 	: 	This folders contains files useful for Interfaces / Displays
Example 	: 	Any help or example that I used for the project
EXTRA 		: 	Some (ideas) features that maybe will be developped in the future
General 	: 	Usual features
GPS 		:	Features use the GPS USB STICK or in realtion with GPS data
START 		:	File usefull to start the Project
```

#### Files in "/TravelKit_RPI/Affichage/DOT3K"
- In this project I used the Display'O'tron 3000 by Pimoroni
```
dot3k_affichage_boussole.py 		: Launch the feature "Boussole" in the folder "GPS" and display the data to Display Compass informations

dot3k_affichage_determination.py 	: Launch the feature "Recuperation_Determination" in the folder "GPS" and display the Location

dot3k_affichage_emergency_number.py 	: Launch the feature "emergency_number" in the folder "General" and display the continent's Emergencies Numbers

dot3k_affichage_meteo.py 		: Launch the feature "Meteo" in the folder "GPS" and display the Weather data

dot3k_affichage_meteo_3h.py 		: Launch the feature "Meteo_3h" in the folder "GPS" and display the Weather data with a forecast of 3 Hours

dot3k_affichage_temps_système.py 	: Launch the feature "temps" in the folder "General" and display the system time

light_blue_cyan.py 			: Put a Swagg Cyan color for the light of the Screen to be more readable

nettoyage_du_cache.py 			: Delete the Python Cache files (*.pyc)

dot3k.cfg 				: Configuration file for the DOT3K display

```
#### Files in "/TravelKit_RPI/EXTRA/"
 - Future features
```
assistant_audio.py 		: I would like to develop an Audio Assistant that tell the User important informations
sifflet_numerique.py 		: I would like to develop a numeric whistle that can be usefull in case of avalanche or flood to locate the user the fast as possible in this kind of cases
```
#### Files in "/TravelKit_RPI/General/"
- Usefull and common informations
```
Date_Heure_Annee.py 	: Get the time with more details
emergency_number.py 	: Get the Emergencies Phones Numbers of your continents by locate using the GPSoI.py file in the "GPS" folder
temps.py 		: Get the system time basically
```

#### Files in "/TravelKit_RPI/GPS/"
- GPS data
```
Boussole.py 					: Get Compass data by using the "Recuperation_Determination.py" file's data
GPSoI.py 					: Get the location of the user's IP Adress by using the *IPSTACK.COM API*
Meteo.py 					: Get the Weather's data by using *pyown API* and the "Recuperation_Determination.py" file's data
Meteo_3h.py 					: Get the Weather's data by using *pyown API* and the "Recuperation_Determination.py" file's data with a forecast of 3 Hours
Recuperation_Determination.py 			: Get information come from the GPS USB stick and determinate the location with the *Google Maps API*
Recuperation_FR_GPS.py 				: Allow to display the information come from the GPS USB stick in French
```
#### Files in "/TravelKit_RPI/START/"
- Start FILES
```
Start_DOT3K_TravelKit.py : Start the whole project by using the DOT3K display
Start_DOT3K_TravelKit.sh : File use to start the "Start_DOT3K_TravelKit.py" file when the Raspberry is ON.
```



## Authors

-   **Franck ROCHAT**  -  _Initial work_  -  [Franck ROCHAT](https://github.com/Franck1333)  Thank You !  :heart:
