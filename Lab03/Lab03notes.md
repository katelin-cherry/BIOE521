
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
