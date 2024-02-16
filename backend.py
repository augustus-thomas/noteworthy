# functions for backend calls
import os
import time
import datetime

# return whether filename exists
def search_for_file(filename):
	return filename in os.listdir("Notes")

# return files modified by date. default to after passed date
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

# name is a filename. can have .md extension passed
# if it has a period a different extension we will force it to be .md

# contents are string, filename may or may not already exist
# filename is optional. if none, first word in contents dot md
def write(contents, filename):
	pass

# if filename doesn't exist, return a string with error message
# if filename exists, return a string with its contents
def view(filename):
	pass

# list files in notes directory
def list():
	ouput = ""
	for file in os.listdir("Notes"):
		output.append(note + "\n")

	return output

