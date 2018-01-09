# Quick Python function to read lines from a file and format it
# Used to make my life easier when needing to format a bunch of SQL queries for JavaScript 
# To run: cat <input_file> | python main.py
import sys
data = sys.stdin.readlines()
with open("output.txt", "w") as text_file:
	for index, i in enumerate(data):
		str = "'" + i.strip() + "'"
		if index < (len(data) - 1):
			str += " +\n"
		else:
			str += ";"
		text_file.write(str)
