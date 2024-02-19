# functions for backend calls
import os
import time
from datetime import date

# return whether filename exists
def search_for_filename(filename):
	return filename in os.listdir("Notes")

# return files modified by date. default to after passed date
# return contents directly the date before the next day
def search_by_date(filename, date, after=True):
	year_date_month = date.split('\\')
	# make date into EPOCH
	epoch = datetime.datetime(*year_date_month, 0, 0, 0).strftime('%s')
	output = ""
	for filename in os.listdir("Notes"):
		# get the time file was last modified
		modified = os.path.getmtime(filename)
		if modified >= epoch:
			output.append(filename + '\n')
	return output

# date is in format zero width space "YYYY-MM-DD" zero width space on its own line
def search_for_modfication_on_date(filename, date):
	pass

#^^ Change to search by date?

# Fully deletes a file
def remove_file(file):
	os.remove(file)

# Fully clears the file where info is stored
def del_file_contents(file):
	with open(file,'r+') as file:
		file.truncate(0)

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

