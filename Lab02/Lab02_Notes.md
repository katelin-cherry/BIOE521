# Lab2A. Redirecting Streams of Data
**STDIN:** command prompt serves as a source of standard input  
**STDOUT** computer monitor serves as a stream of std output  

Can send a streamed output directly to a new file, instead of computer screen, usting the ```>``` operator. Ex:  
```$echo 'Hello World! > hi.txt```  
```$cat hi.txt```  

**wc** - prints newline, word, and byte counts for each file  
The hi.txt file created earlier contains 12 bytes. Each character including a space is a byte. You can also tell how man bytes are in a file using the `wc`command:  ``$ wc -c hi.txt``

## Looking at Long streams
Using `ls -la`: The `.` entrie refers to current directory and the `..` refers to parent directory. You can use them to navigate up one directory. Also see last date file was modified and column of integers show how many bytes are in the file

`$head web2` looks at the first ten lines of file  
`$tail web2` looks at last ten line of file  
`$more web2` or `$cat web2 | more` inspects the file file live, one screen at a time  
**pipe** - processes the datastream as its going by. A simple way of connecting two commands together, and sending a datastream through this connection.  
`$cat web2 | more` searchs through web2 file with cat as its input stream then outputs via STDOUT to your screen.  
`$cat web2 | grep dog | cat -n > some_dog_words.txt` numbers the file that contains only words that have dog in it  
`$wget -q0- http://google.com/robots.txt` only reads the file so you can find what you want on it  
`tee` one input stream but two output streams (one of which can be written directly to a file wihtout interrupting the other output). Good way to save some of the data streams along the way.  

## Practice
1. single-line program to output a line of text which tells you the line number where `palm` is Disallowed in Google's robot.txt file: `$wget -q0` http://google.com/robots.txt | cat -n | grep palm
2. A single-line program to output a line of text containing your "inet addr" and save output: `$ifconfig | grep "inet addr" | head -1 | tee inet.txt`

# Lab2b. Customizing your command prompt  
**The Command Prompt** 
`cat ~/.bashrc` is the configuration file for your login. Can customize command prompt by editing this file  
When editing the file, it's good to make a backup which can be done by: `$ cp ~/.bashrc ~/.bashrc-BACKUP`  
To add other commands into your prompt, consider the backtick character. It escapes you from its own temporary shell mid-stream and takes the STDOUT from that command to insert. It's a simple way to have nested commands simply by encasing in backticks. 
