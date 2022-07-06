# csv_scanner
Simple processing of csv file row by row.
Each row is a list.
Looks at the 6th Element of that list and counts 
how often keyword1 or keyword2 appears as that element.

it works with any csv file that has rows with at least 6 elements.
put this script and the csv file "xy.csv" in the same directory and type in terminal:
"python3 scan_csv_script.py xy.csv" for it to run. Takes about 50 sec for 35 000 000 rows or 800 mb of data.

Similar to your task except that the text of that earning call
will be one element of the list and I would have to check which of those
calls contains which keyword. Could be printed to new file with the
rownumber as a unique identifier for each call
