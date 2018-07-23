# TravelKit_RPI  
  
This Project give you useful details about the environement where you are by Using an USB GPS and some API with an Internet Connection. 
  
## Getting Started  
  
To get a copy of the project , you can go on the GitHub's webpage of the project and click on the green button to download as a .ZIP file. However , if you're using a prompt on a unix machine use this line :

```
git clone https://github.com/Franck1333/TravelKit_RPI.git
```
  
### Prerequisites  
  
To use the project , you will need some Hardware:
  
```  
A Raspberry Pi
A USB G.P.S (Ublox-7) -->  http://amzn.eu/aG9vR3t
A Micro S.D card (8 Gb Minimum)
A screen (Diplayotron 3000 or other lcd) 
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

Now especially for the Display'O'Tron 3000 in our case

```
	- The Github page : https://github.com/pimoroni/displayotron
	- The command line Setup (need to be install) : curl -sS get.pimoroni.com/displayotron | bash
	- Directory 'plugins'
	- Directory 'utils'
	- File 'dot3k.cfg'
	- Directory 'library'
```
  
### Installing  
To get and install the files , use this line : git clone  [https://github.com/Franck1333/TravelKit_RPI.git](https://github.com/Franck1333/TravelKit_RPI.git)

### NEED TO BE INSTALL BEFORE RUNNING

#### The Weather API :
```
  sudo pip install pyowm
```

#### The Google Maps API :

```
  sudo pip install -U googlemaps
```

#### The Display'O'Tron Softwares and libs :

```
  curl -sS get.pimoroni.com/displayotron | bash
```
  
## Running the tests  
  
For now , you have to run the project by using this command to each files:

    sudo python file.py

  

## Authors

-   **Franck ROCHAT**  -  _Initial work_  -  [Franck ROCHAT](https://github.com/Franck1333)  Thank You ! :heart:


