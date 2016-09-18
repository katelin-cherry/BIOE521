
# Lab3a. The Raspberry Pi Camera  
**Using the camera**  
Can see a list of commands by running `$raspistill 2>&1 | more`. Have to have 2 and 1 bc STDERR is simply integer 2 and want to redirect it to STDOUT which is integer 1. This has to be done before you can pipe it to do more.  
Option `-v`: outputs debugging/information messages during the program run  
Option `-o`: Specifies the output filename. If not specified, no file is saved. If the filename is '-', then all output is sent to stdout.  

**To view images**  
Install `fbi` aka Linux FrameBufferImageviewer by: `$sudo apt-get update` then `$sudo apt-get install fbi`  
Can view slideshow of images with 5 sec delay: `$ fbi -a -t 5 *.jpg`  
**Recording a video**   
Learn about `raspivid` with `$ raspivid 2>&1 | more`  
To play video have to use omxplayer  

# Lab3b. Introduction to Shell Scripting  
**shebang** - the character sequence consisting of the characters number sign and exclamation mark at the the beginning of the script. To denote a shell script use `#! /bin/bash` at the beginning of a text file.  
**bang (!)** - indicates to the shell interpreter that the file should be processed as a series of commands. Together the `#` indicating comment and the `!` make the shebang.  
**Setting variables** - some are already set into the shell such as `$USER` and `$PATH`.  
You can also set variables with a simple assignment or the backtick character to call it when the script is running. Like in the exerpt from the bash-script.sh:

```
echo "I'm setting two variables now."  
COLOUR="purple"					# set a local shell variable  
VALUE="96"					# set a local shell variable  
echo "This is a string: $COLOUR"		# display content of variable  
echo "And this is a number: $VALUE"		# display content of variable  
echo  

echo "Let's figure out who you are:"  
echo "Oh, hi, $USER!"		# dollar sign is used to get content of variable  
echo  

echo "We can also do this by nesting commands with the backtick:"  
myName=`whoami`  
echo "I've just run 'whoami' to determine that you are the user '$myName'"  
echo  

echo "Let's figure out what date and time it is:"  
DATE=`date +"%Y-%m-%d @ %I:%M%p"`  
echo "Oh, it's currently $DATE"  
echo
```  
**More Input**  
User input options are assigned to integer variables in numerical order.  

## Assignments  
1. **get-script.sh** Creates a new file based on an online template and user input:  
```
#! /bin/bash
wget https://github.com/jmil/Bioe421_521-MicrocontrollerApplications/raw/master/Attachments/bash-script.sh 
mv bash-script.sh "$1"
chmod +x "$1" #changes the user permissions to executable
```  
2. **weather.sh** A script that grabs the current local weather data and saves to a file with the current time and located at /home/pi/weather.
First, you need to install the weather-util command using `$ sudo apt-get install weather-util`.  
Handy tool: `tail -n <number_of_lines> /path/to/file` gets the number of last lines you want to get  
```
#! /bin/bash

cd /home/pi
mkdir -p weather #makes a new directory if there isn't one already there
cd /home/pi/weather

today=`date +%Y-%m-%d:%H:%M:%S` #tickmarks call an in script action to retrieve date
echo $today #sets this as a variable

weather hou | grep Temperature > "$today.txt" #creates the file with today's date
weather hou | grep Humidity >> "$today.txt" #appends to the file
weather hou | grep Wind >> "$today.txt"
weather hou | grep Weather >> "$today.txt"
weather hou | grep Sky >> "$today.txt"
weather hou | grep Precipitation >> "$today.txt"
```

3. **robots.sh** A script that grabs the google.com/robots.txt file and sends the output to STDOUT. Modify script to take input from the user, and use this user input to constrain the output. This will search for a certain word that the user inputs:
```
#! /bin/bash

wget http://www.google.com/robots.txt  
cat robots.txt | cat -n | grep -w "$1" 
```

4. **word.sh** Write a script to grep the web2 dictionary for the string wow. Modify script to take input from the user.
```
#! /bin/bash

cd ~/Lab02
cd dict 
cat web2 | grep "$1"
```
Note: We tried downloading the dictionary and unzipping that file but were unsuccessful. It would download the zip file but then couldn't read the documents within the script file. It worked when we did it in the command window though.  
5. **selfie.sh** Write a script to take a selfie and save the image with the current time.
```
#! /bin/bash

cd /home/pi
mkdir -p raspicam
cd /home/pi/raspicam

today=`date +%Y-%m-%d:%H:%M:%S` 
echo $today

raspistill -v -o "HouseOfPies-$today.jpg"
```
