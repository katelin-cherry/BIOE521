**BIOE 521 - Microcontrollers Notes**

Raspberry Pi is a complete computer system under $40. It uses an ARM processor similar to what is found in many smartphones. It can run many operating systems (OSes) and is perfect for lightweight input/output tasks. Raspberry Pi's low cost and extremely low power usage make it a perfect choice for always-on internet-connected computing. It also has a rudimentary graphics card allowing us to run a full graphical user interface, which we will do later in the semester.

**Logging in**   
Upon logging in, you see last login time, program info, and that it comes will no warranty.

**Setting up**  
`$sudo raspi-config`   This is the command to launch the raspi-config tool  
    
**Internet access**  
`$if config eth0`  This command will tell you if you have internet access. If you do have access, you will see an entry for inet6 addr

**Upgrading system and all software**  
Grabs the complete list of all the latest software programs and packages 
`$sudo apt-get upgrade`  
 
We use dist-upgrade instead of upgrade to make sure that we have an intelligently loaded set of software that is known to work together. To upgrade system:
`$sudo apt-get dist-upgrade`  

Installing games and other programs:    `sudo apt-get install arduino`  

**Shutting down and rebooting**  
Rebooting:
`sudo shutdown -r now` or  `reboot`   
Safe shutdown: `sudo shutdown -h now`

## Lab1C: Understanding the Shell

**shell**: A shell manages the user-system interaction by prompting users for input, interpreting their input, and then handling an output from the underlying operating system.  
**text-only command-line interface (CLI):** - or the "command line" is the simplest shell we use in the class
**command prompt** - string of characters next to your blinking cursur. You typically type the **command** then the **argument**  
* defalut command prompt - $  
* superuser: #  

# Learning more about your Pi
1. What is your username? `$whoami` Answer: pi  
2. Short hostname? `hostname` raspberry pi  
3. IP Address? `$ifconfig` inet addres: 10.64.30.216 
4. full path of current working directory? `pwd` /home/pi/Documents
5. How long Pi has been turned on? `uptime --pretty1` up 1 hr, 23 min
6. version of Python installed on Pi? `Python --version` Python 2.7.9
7. How long to get a ping from google.com? How many bytes? `$ping google.com` time=1.56 ms 64 bytes
8. Where is the man command located on hard drive? `$manpath` /usr/local/man:/usr/local/share/man:/usr/share/man:usr/man
9. Serial number on your Pi? `tail /proc/cpuinfo` 0000000a161b3b6
10. version of Raspbian Linux are you running on your Pi(hint: it's the pretty name show in the /etc/os-release file) `$head /etc/os-release` "Raspbian GNU/Linux 8 (jessie)"
11. If you want your pi to take a photograph every hour, what program and what program to schedule the command? `$raspistill --timelapse` and `$crontab -e`
12. Command to reboot immediately? `$reboot`
13. What percentage of CPU does the top command utilize? `$top` 1.6





