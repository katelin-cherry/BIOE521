#! /bin/bash

# Bioe 421/521 Microcontroller Applications
# http://github.com/jmil/Bioe421_521-MicrocontrollerApplications

# Awesome help on bash shell scripting here:
# http://tldp.org/LDP/Bash-Beginners-Guide/html/

########### Purpose ############
# You should write a description here about what this script can do
# and why you wrote it. Make sure to use "#" to set each comment line as a comment!

################################
##### Your Code Goes Below #####
################################


# Adapted from: http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_02_02.html
# This script clears the terminal, displays a greeting and gives information
# about currently connected users.  The two example variables are set and displayed

cd /home/pi
mkdir -p weather
cd /home/pi/weather

today=`date +%Y-%m-%d:%H:%M:%S` 
echo $today

weather hou | grep Temperature > "$today.txt"
weather hou | grep Humidity >> "$today.txt"
weather hou | grep Wind >> "$today.txt"
weather hou | grep Weather >> "$today.txt"
weather hou | grep Sky >> "$today.txt"
weather hou | grep Precipitation >> "$today.txt"




