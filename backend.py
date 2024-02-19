# functions for backend calls
import os
import time
from datetime import date

# return whether filename exists
def search_for_filename(filename):
	return filename in os.listdir("Notes")

# returns the content in file from the date requested
def search_content(filename, date):
	pass
	
# returns a list of name date pairs [['name.md', '2022/04/11'], ['science.md', '2024/03/01']]
def search_title(filename, date):
	# date info needs to be formated YYYY/MM/DD
	year_date_month = date.split('/')
	# make date into EPOCH
	epoch = datetime.datetime(*year_date_month, 0, 0, 0).strftime('%s')
	output = ""
	for filename in os.listdir("Notes"):
		# get the time file was last modified
		modified = os.path.getmtime(filename)
		if modified >= epoch:
			output.append(filename + '\n')
	return output

# name is a filename. can have .md extension passed
# if it has a period a different extension we will force it to be .md

# contents are string, filename may or may not already exist
# filename is optional. if none, first word in contents dot md
def write(contents, date=date.today(), filename=None):
	# contents should be a string
	assert type(contents) == type("string")

	# find the filename if none was passed
	if filename == None:
		potential_filename = contents.split(" ", 1)[0]
		filename = potential_filename.split(",", 1)[0]

	edit_char = "w"
	if search_for_filename(filename):
		# append if filename already exists
		edit_char = "a"

	with open(filename, edit_char) as f:
		f.write('\u2001' + str(date) + '\u2001' + '\n')
		f.write(contents)

# if filename doesn't exist, return a string with error message
# if filename exists, return a string with its contents
def view(filename):
	if search_for_filename(filename):
		with open(filename) as f:
			s = f.read()
	else:
		s = "File does not exist"
	return s

# list files in notes directory
def list():
	output = ""
	for file in os.listdir("Notes"):
		output += file + "\n"

	return output

