
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
