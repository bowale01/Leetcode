Sample Log File
Let's create a sample file named example.log with the following contents:


2024-08-08 12:34:56 INFO 192.168.1.1 200 "User logged in"
2024-08-08 12:35:00 ERROR 192.168.1.2 500 "Failed login attempt"
2024-08-08 12:35:05 INFO 192.168.1.1 200 "User logged out"
2024-08-08 12:35:10 WARNING 192.168.1.3 404 "Resource not found"
2024-08-08 12:35:15 ERROR 192.168.1.4 500 "Failed login attempt"
2024-08-08 12:35:20 INFO 192.168.1.1 200 "User logged in again"


Using GREP 

1. Search for the "ERROR" keyword:

grep "ERROR" example.log

Output
2024-08-08 12:35:00 ERROR 192.168.1.2 500 "Failed login attempt"
2024-08-08 12:35:15 ERROR 192.168.1.4 500 "Failed login attempt"



2. Case-insensitive search for the keyword "error":

   grep -i "error" example.log

2024-08-08 12:35:00 ERROR 192.168.1.2 500 "Failed login attempt"
2024-08-08 12:35:15 ERROR 192.168.1.4 500 "Failed login attempt"


Using SORT

1. Sort the log entries alphabetically:

sort example.log

2024-08-08 12:34:56 INFO 192.168.1.1 200 "User logged in"
2024-08-08 12:35:05 INFO 192.168.1.1 200 "User logged out"
2024-08-08 12:35:20 INFO 192.168.1.1 200 "User logged in again"
2024-08-08 12:35:00 ERROR 192.168.1.2 500 "Failed login attempt"
2024-08-08 12:35:15 ERROR 192.168.1.4 500 "Failed login attempt"
2024-08-08 12:35:10 WARNING 192.168.1.3 404 "Resource not found"


2. Sort by the status code (assuming column 4):

sort -k 4,4 -n example.log

2024-08-08 12:35:10 WARNING 192.168.1.3 404 "Resource not found"
2024-08-08 12:34:56 INFO 192.168.1.1 200 "User logged in"
2024-08-08 12:35:05 INFO 192.168.1.1 200 "User logged out"
2024-08-08 12:35:20 INFO 192.168.1.1 200 "User logged in again"
2024-08-08 12:35:00 ERROR 192.168.1.2 500 "Failed login attempt"
2024-08-08 12:35:15 ERROR 192.168.1.4 500 "Failed login attempt"



Sort IP Addresses:

Sort the extracted IP addresses:


grep -oE '([0-9]{1,3}\.){3}[0-9]{1,3}' log.txt | sort

192.168.1.1
192.168.1.1
192.168.1.2
192.168.1.3



Using UNIQ
1. Remove duplicate lines:

sort example.log | uniq

2024-08-08 12:34:56 INFO 192.168.1.1 200 "User logged in"
2024-08-08 12:35:00 ERROR 192.168.1.2 500 "Failed login attempt"
2024-08-08 12:35:05 INFO 192.168.1.1 200 "User logged out"
2024-08-08 12:35:10 WARNING 192.168.1.3 404 "Resource not found"
2024-08-08 12:35:15 ERROR 192.168.1.4 500 "Failed login attempt"
2024-08-08 12:35:20 INFO 192.168.1.1 200 "User logged in again"


2. Count occurrences of each unique line:

sort example.log | uniq -c

      1 2024-08-08 12:34:56 INFO 192.168.1.1 200 "User logged in"
      1 2024-08-08 12:35:00 ERROR 192.168.1.2 500 "Failed login attempt"
      1 2024-08-08 12:35:05 INFO 192.168.1.1 200 "User logged out"
      1 2024-08-08 12:35:10 WARNING 192.168.1.3 404 "Resource not found"
      1 2024-08-08 12:35:15 ERROR 192.168.1.4 500 "Failed login attempt"
      1 2024-08-08 12:35:20 INFO 192.168.1.1 200 "User logged in again"



3. Show only duplicate lines:

sort example.log | uniq -d

Output:

(In this case, there are no duplicate lines in the log file; so no output.)


Using SED

1. Substitute a string in the file:

sed 's/ERROR/ALERT/g' example.log

2024-08-08 12:34:56 INFO 192.168.1.1 200 "User logged in"
2024-08-08 12:35:00 ALERT 192.168.1.2 500 "Failed login attempt"
2024-08-08 12:35:05 INFO 192.168.1.1 200 "User logged out"
2024-08-08 12:35:10 WARNING 192.168.1.3 404 "Resource not found"
2024-08-08 12:35:15 ALERT 192.168.1.4 500 "Failed login attempt"
2024-08-08 12:35:20 INFO 192.168.1.1 200 "User logged in again"


2. Delete lines containing "WARNING":

sed '/WARNING/d' example.log

2024-08-08 12:34:56 INFO 192.168.1.1 200 "User logged in"
2024-08-08 12:35:00 ERROR 192.168.1.2 500 "Failed login attempt"
2024-08-08 12:35:05 INFO 192.168.1.1 200 "User logged out"
2024-08-08 12:35:15 ERROR 192.168.1.4 500 "Failed login attempt"
2024-08-08 12:35:20 INFO 192.168.1.1 200 "User logged in again"


3  Print only the 3rd line:

sed -n '3p' example.log

2024-08-08 12:35:05 INFO 192.168.1.1 200 "User logged out"


Summary
These commands provide powerful ways to process and analyze text data on Unix-like systems. Here’s a brief recap:

grep: Search for patterns within files.
sort: Sort lines of text files.
uniq: Filter out or count duplicate lines.
sed: Perform text transformations and deletions.
Combining these commands allows for sophisticated text processing and log analysis tasks.
















