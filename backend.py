# functions for backend calls
import os
import time

# return whether filename exists
def search_for_file(filename):
	pass

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

