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
			pos = find_pat(r'\d+',find_pat(r'>\d+',s))
			name_m = find_pat(r'<tr align="right"><td>\d+</td><td>[A-Za-z]+',l) #returns <tr align="right"><td>1</td><td>Michael
			name_m = find_pat(r'>[A-Za-z]+',name_m) #returns >Michael
			name_m = find_pat(r'[A-Za-z]+',name_m)
			
			#name_m = find_pat(r'>\w+',find_pat(r'<td>\d+</td><td>\w+',l)) #returns '>name'
			#name_m = find_pat(r'\w+',name_m) #returns 'name'
			
			#name_m = "saul%s" % lines
			
			#name_f = find_pat(r'<td>\w+</td><td>\w+',l) #returns <td>Michael</td><td>Jessica
			#name_f = find_pat(r'</td><td>\w+',name_f) #returns </td><td>Jessica
			#name_f = find_pat(r'>\w+',name_f) #returns >Jessica
			#name_f = find_pat(r'\w',name_f) #returns Jessica
			names_d[name_m] = pos
			#names_d[name_f] = pos
	
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