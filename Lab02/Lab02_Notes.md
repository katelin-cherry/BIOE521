# Lab2A. Redirecting Streams of Data
**STDIN:** command prompt serves as a source of standard input  
**STDOUT** computer monitor serves as a stream of std output  

Can send a streamed output directly to a new file, instead of computer screen, usting the ```>``` operator. Ex:  
```$echo 'Hello World! > hi.txt```  
```$cat hi.txt```  

**wc** - prints newline, word, and byte counts for each file  
The hi.txt file created earlier contains 12 bytes. Each character including a space is a byte. You can also tell how man bytes are in a file using the `wc`command:  
``$ wc -c hi.txt``

## Looking at Long streams
Using `ls -la`
