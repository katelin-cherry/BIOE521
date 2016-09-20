# Lab 4A. Parsing with Grep, Awk, and Sed

A script that downloads the article information to substitute the unique PMID for the line going through
```
#! /bin/bash

chmod +x parsePMIDs.sh 

while read line; do
echo "$line"
site="http://www.ncbi.nlm.nih.gov/pubmed/$line?report=MEDLINE&format=text"
wget -O - >> Tsien_result.txt "$site"

done <tsien_PMIDs.txt 
```
The syntax for the URL fields defined for NIH e-utilities:
* term 
* reldate - when reldate is set to an integer n, the search returns only those items that have a date specified by datetype within the last n days
* mindate,maxdate - will look between these date ranges. General date format is YYYY/MM/DD
* retmax - how many IDs retrieved

script that takes the first user input and processes it line by line to generate a PMID query, and append a formmatted bibliography for that PMID to a new cancer_bibliography.txt file:
```
#! /bin/bash

echo "PMID Queries" > prettybib.txt #creates a temporary file

while read line; do
echo "$line" #takes the line from the first user input
site="http://www.ncbi.nlm.nih.gov/pubmed/$line?report=MEDLINE&format=text"
wget -O - >> "bibliography$line.txt" "$site" #creates a temp file for that ID

grep "PMID" "bibliography$line.txt" >> prettybib.txt #adds the  PMID number to the pretty text file
sed -n 's/^[^-]*FAU[^-]*-[[:blank:]]*//p' "bibliography$line.txt" >> prettybib.txt #adds author info
grep "SO  -" "bibliography$line.txt" >> prettybib.txt
sed -n '/AB  -/,/FAU -/p' "bibliography$line.txt" >> prettybib.txt

rm "bibliography$line.txt"

done < "$1"

grep -v "FAU -" prettybib.txt > "$2"

chmod +x PMID_query.sh
```