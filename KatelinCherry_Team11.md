Katelin Cherry - Team 11

# Lab 1 - 8/25/16

**man** - is the systems' manual pager. each page argument given to man is the name of a program/utility/function. section will direct man to look only in that section of the manual - will search all the available sections following a pre-defined order unless overridden by SECTION directive (/etc/manpath.config).
section numbers:
1) executable programs or shell commands
2) system calls (functions provided by the kernel)
3) library calls (functions within program libraries)
4) special files (usually found in /dev)
5) file formats and conventions eg /etc/passwd
6) games
7) misc stuff 
8) system administration (usually only for root)
9) kernel routines

**who** - print information about users currently logged in\
-a, --all - same as -b -d --login -p -r -t -T -u  
-b, --boot - time of lat system boot  
-d, --dead - print dead processes  
-H, --heading - print line of column headings  
--ips - print ips instead of hostnames, with --lookup, canonicalizes based on stored IP, if available, rather than stored hostname  
-l, --login - print system login processes  
--lookup - attempt to canonicalize hostnames vis DNS  
-m only hostname and user associated with stdin  
-p, --process - print active processes spawned by ini  
-q, --count - all login names and number of users logged in  
-r, --runlevel - print current runlevel  
-s, --short - print only name, line, and time (default)  
-t, --time - print last system clock change  
-T, -w, --mesg - add user's message status as +, - or ?  
-u, --users - list users logged in  
--message - same as -T  
--writable - same as -T  
--help - display this help and exit  
--version - output version information and exit  

**whoami** - print effective userid

**hostname** - display the system's DNS name, display or set its hostname or NIS domain name  
hostname - print name of system as returned by gethostname function  
domainname - print NIC domainname of the system  
dnsdomainname - print domain part of FQDN (fully qualified domain name)  

**passwd** - changes passwords for user accounts and account/password validity period

**sudo** - allows a permitted user to execute a command as the superuser or another user

**su** - used to become another user during a login session, invoked w/o a username, defaults to becoming the superuser. Optional argument - may be used to provide an environment similar to what the user would expect had the user logged in directly.

**ps** - displays info about a selection of the active processes. If you want a repetitive update of the selection and the displayed info, use top(1) instead. ps accepts several kinds of options:
1) UNIX options - may be grouped and must be preceded by a dash
2) BSC options - may be grouped and must not be used with a dash
3) GNU long options - preceeded by two dashes

**top** - provides dynamic real-time view of running system. Can display system summary info as well as list of processes or threads managed by Linux kernel. Provides limited interactive interface for process manipulation and interface for personal configuration. Can be renamed (possibly an alias) - new name will be reflected on top's display.  

**uptime** - tells how long system has been running. Displays info: current time, how long the system has been running, how many users are currently logged in, system load averages for past 1, 5, 15 min. Same info contained in header line w(1).

**echo** - displays a line of text

**touch** - change file timestamps - update the access and modification times of each file to current time

**chown** (GNU version) - changes user and/or group ownership of each given file. If only an owner is given, user is made the owner of each given file, and the files' group is not changed. If the owner is followed by a colon adn a group name (or numeric group ID), with no spaces between them, the group ownership of the files is changed as well. If a colon but no group name follows the user name, that user is made the owner of the files and the group of the files is changed to that user's login group. If the colon and group are given, but the owner is omitted, only the group of the files is changed; in this case, chown performs the same function as chgrp. If only a colon is given, or if the entire operand is empty, neither the owner nor the group is changed.

**chmod** - changes the file mode bits of each given file according to mode, which can be a symbolic representation of changes to make, or an octal number representing the bit pattern for new mode bits.

**chgrp** - change the group of each file to group. With --reference, change the group of each FILE to that of RFILE.

**crontab** - program used to install, deinstall or list the tables used to drive the cron(8) daemon in Vixie Crom. Each user can have own crontab, and though these are files in /var/spool/cron/crontabs, not intended to be edited directly.

**nano** - small, free editor which aims to replace Pico (default editor in non-free Pine package), also implements some missing features

**pwd** - print full filename of current working directory

**ls** - list info about FILEs (current directory by default). Sort entires alphabetically if none of -cftuvSUX nor --sort is specified, mandatory arguments to long options are mandatory for short options too

**dir** - list info about FILEs (current directory by default). Sort entires alphabetically if none of -cftuvSUX nor --sort is specified, mandatory arguments to long options are mandatory for short options too

**mkdir** - create the DIRECTORY(ies) if they don't already exist, mandatory arguments to long options are mandatory for short options too

**cd** - change directory

**cp** - copy SOURCE to DEST, or multiple SOURCE(s) to DIRECTORY

**mv** - rename SOURCE to DEST, or move SOURCE(s) to DIRECTORY

**rm** - removes each specified file, by default doesn't remove directories. If the -I or --interactive=once option is given and there are more than 3 files on the -r, -R, or --recursive are given, then prompts the user for whether to proceed with entire operation. If response not affirmative, entire command aborted. If file is unwritable, stand input is a terminal.

**bash** - sh-compatible command language interpreter that executes commands read from the standard input or from a file. Also incorporates useful features from the Korn and C shells (ksh and csh)

**dash / sh** - standard command interpreter for system

**ssh** - (SSH client) - program for logging into remote machine and for executing commands on a remote machine. Intended to replace rlogin and rsh, and provide secure encrypted communications between two untrusted hosts over an insecure network. 

**which** - returns the pathnames of the files (or links) which would be executed in the current environment

**clear** - clears terminal screen if possible 

**cat** - concatenate FILE(s) or standard input to standard output

**sed** - stream editor - used to perform basic text transformation on an input stream (file or input from a pipeline). Similar to an editor that permits scripted edits, but makes one pass and is more efficient.

**grep** - searches named input FILEs or standard input for lines containing a match to the given PATTERN. By default, prints matching lines

**more** - filter for paging through text one screenful at a time\
**less** - similar to more but has more features - doesn't have to read entire input file so it's faster with large files

**head** - print the first 10 lines of each FILE to standard output\
**tail** - print the last 10 lines of each FILE to standard output

**tar** - stores and extracts files from a tape or disk archive

**unzip** - list, test, or extract files from ZIP archive. Default is to extract into current directory/subdirectories all files from the specified ZIP archive

**wget** - free utility for non-interactive download of files from the Web. Supports HTTP, HTTPS, and FTP protocols, as well as retrieval through HTTP proxies

**ifconfig** - configure kernel-resident network interfaces. Used at boot time to set up interfaces, after that usually only needed for debugging or system tuning

**man mount** - attaches filesystem found on some device to big file tree. unmount(8) detaches

**ping** - uses the ICMP protocol's mandatory ECHO_REQUEST datagram to elicit an ICMP ECHO_RESPONSE from a host or gateway

**apt-get** - command-line tool for handling packages

**git** - revision control system that provides high-level operations and full access to intervals

**python** - programming language

**raspistill** - for taking photos\
**rapivid** - for taking video

**uname** - print system info

**shutdown** - halt, power off, reboot machine\
**reboot** - can also use halt, poweroff, reboot

# Lab 2 - 9/1/16
**wc** - print newline, word, and byte counts for each file\
**tee** - read from std input and write to std output and files

# Notes

$ ps | grep ps\
2505 ps | grep ps\
^process ID

We can terminate a process by name or by PID\
$ kill 2506 OR $ kill ps b  will kill process\
$ killall ssh b  kill all ssh connections to other machines

/bin/bash b  bash shell is a file on your computer that gets run\
$ rm /bin/bash b  malicious user tries to delete ways for user to get a shell on their computer\
If you delete bash, computer may be nonfunctional\
The whole OS --> series of files\
$ rm -rf /\
^2nd r is for recursive through all folders, f is for forcible removal

Authorization b  every file and folder has a permission linked to it\
3 categories\
-User/owner b  owner (username) of the file (usually who created it)\
-Group b  collection of users\
-World b  any other user who has access b  typically means shell access\
For each category, 3 independent permissions\
-r b  read b  contents of a file (can read w/ cat, launch w/ nano but no edits)\
-w b  write b  edit a file\
-x b  execute\
Shown in a 10-character register ($ls -la gives you this)\
-d r w x r - x - - - pi pi somefiletxt\
 ^owner ^group\
-First character: file type\
      b  file\
      d directory/folder\
      l link\
-Next 3 sets of 3 characters each\
     1st set: user/owner\
     2nd set: group\
     3rd set: world

How to edit permissions? (ch = change)\
chown b  change ownership\
chgrp b  change group associated\
chmod b  change mode of the permissions\
$ chown student filename (student username becomes owner\
$ chmod +x filename (add execute permissions to the file)\
                 ^adds for every category\

Who can change permissions?\
-Whoever has read and write access b  typically at least the owner\
-Superuser <-> root b  one master/base user account from which all other accounts are derived\
-Typically b  if you have admin access, then you can become root
By default: pi username is an admin\

$ whoami\
Pi\
$ apt-get dist-upgrade\
Fail\
$ sudo apt-get dist-upgrade\
^checks your authorization (authentication only happens when you log in) to become root for that one command

$ sudo -s\
#_ (general user gets $, root user gets #. Warning that you have infinite power over the system)\
$ rm /bin/bash\
^wonb t run because bash file is owned by root --> fail\
$ sudo rm /bin/bash\
^will delete bash command\
$ rm -rf /\
^remove ^recursively force delete ^top level of harddrive\
If you run this while logged in as pi --> wonb t happen\
BUT\
$ sudo rm -rf /                 will delete entire harddrive

# grep
grep "boo" a_file\
-n: adds line numbers\  
-vn: prints negative result, lines that do not match search string\  
-c: suppresses printing of matching lines, only display number of lines that match the query\  
-l: only prints filenames of files in query that have lines that match the search string, useful if you're searching through multiple files for the same string\  
-i: treats upper and lower cases as equivalent while matching the search string\  
-x: looks for exact matches only\  
-A: allows you to specify additional lines of context file (grep -A2 "mach" a_file --> machine, boots, bungie)\  
-e$: prints lines that end in the letter 'e'\  
-grep "boots?" a_file --> boot, boots\  
-grep -E "boot|boots" a_file --> boot, boots\  
-special characters: grep '\$' a_file --> broken$tuff\  
-F: finds literal string and not regexps  

# awk
an awk program operates on each line of an input file\  
BEGIN {initialization awk commands}\  
{awk commands for each line of the file}\  
END {finalization awk commands}  

**Awk examples**  
`$ls -l | awk 'BEGIN {sum-0} {sum=sum+5} END {print sum}'`
Looks at the 5th coulum of data in ls-la and sums it  

`ls -la | awk '{for (i=1;i<3;i++) {getline}; print NR, $0}'` prints out every third line of ls -la

**awk control statements:**\
if (condition) statement [else statement]\
while (condition) statement\
do statement while (condition)\
for (expr1; expr2; expr3) statement\
for (var in array) statement\
break\
continue\
exit [expression]

**awk input/output statements:**\
getline: set $0 from next input record\
getline <file: set $0 from next record of file\
getline var: set var from next input record\
getline var <file: set var from next record of file\
next: stop processing current input record, next input record is read and processing starts over\
nextfile: stop processing current input file, if end of input data is reached then END block is executed\

**awk string functions:**\
**gsub(r,s[,t])**: for each substring matching the regular expression r in string t, substitute string s and return number of substitutions. If t is not supplied, use $0.\
**match(s,r[,a])**: returns the position in s where the regular expression r occurs or 0 if it is not present\
**split(s,a[,r])**: splits the string s into the array a using the regular expression r and returns the number of fields\
**sprintf(fmt,expr-list)**: prints expr-list according to format and returns resulting string\
**strtonum(str)**: examines str and returns its numeric value\
**substr(s,i[,n])**: returns the at most n-character substring of s starting at i\
**tolower(str)**: returns copy of the string with all upper-case translated to lower-case. toupper(str) does the opposite

# sed
performs basic text transformations on an input stream, single pass through stream\
sed -e 's/input/output/' my_file: echos every line from my_file to standard output and changes THE FIRST instance of 'input' to 'output'\
sed -e 's/input/output/g' my_file: changes EVERY instance\
default output is written to stdout\
sed -e 's/input/output/' my_file > new_file: redirects to new file\
sed -i -e 's/input/output/' my_file: edits existing file in place

sed -e 's/\/bin/\/\usr\/local\/bin/' my_script > new_script: need backslashes to refer to special symbols like in /usr/local/bin\
sed -e 's/[0-9]*/(&)/' my_file: takes every line that starts with a number in your file and surrounds that number by parentheses. [0-9] is a regexp range for all single digit numbers and * is a repeat count that means any number of digits\

**other sed commands**\
sed -e '/pattern/ command' my_file: general form, pattern is a regexp and command can be one or 's'=search and replace or 'p'=print or 'd'=delete or 'i'=insert or 'a'=append, default action is to print all lines that don't match anyway, so would need to suppress using -n and then use -p to control what command is being printed\
ls -l | sed -n -e '/^d/ p': listing of all sub-directories, will only print lines that start with 'd' symbol\
sed -e '/^#/ d' my_file: delete all lines that start with '#'\
sed -e '1,100 command' my_file: executes 'command' on lines 1,100, can also use '$' to indicate end of file


