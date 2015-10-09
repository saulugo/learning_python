#print the year and then the names follow by the position of the name on that year
#in the case the same name appears as male and female, just give it the smaller number of both.
#f = open(myfile, "w")
#f.write(mytext)

#option -summaryfile 

import re
import os
from sys import argv

def find_pat(pat, text):
	match = re.search(pat,text)
	if match:
		return match.group()
	else:
		return 'not_found'

def look_for_names(file_n):
	f = open(file_n)
	f_text = f.read()
	f_lines = f_text.split('\n')
	names_d = {}
	
	#<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
	lines = 0
	for l in f_lines:
		lines += 1
		s = find_pat(r'<tr align="right"><td>\d+',l)
		if s!="not_found":
			m = re.search(r'<tr align="right"><td>(\d+)</td><td>([A-Za-z]+)</td><td>([A-Za-z]+)</td>',l)
			pos = m.group(1)
			name_m = m.group(2)
			name_f = m.group(3)
			
			names_d[name_m] = pos
			names_d[name_f] = pos
		
	
	return names_d

def main():
	file_n = argv[1] #the first argumen of the script must be the name of the html file to look for the baby names
	names_d = look_for_names(file_n) #look_for_names() returns a dictionary with the list of names and their position
	for k,v in names_d.items():
		print "%s : %s" % (k,v)
	
	print "Bye, Bye!"

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()