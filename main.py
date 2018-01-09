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
