# functions for backend calls
import os
import time
from datetime import date

#import easygui

# This function saves a newline to the lastmodified csv that marks some change and the date
def save_modified(file, date):
	with open('lastmodified.csv','a') as f:
		f.write(str(date) + "," + file + '\n')
# MKDownToPDF
def MKDownToPDF(filename):
    pass 


# return whether filename exists
def search_for_filename(filename):
	return filename in os.listdir("Notes")

# returns the content in file from the date requested
def search_content(filename, date):
	pass
	
# returns a list of name date pairs [['name.md', '2022/04/11'], ['science.md', '2024/03/01']]
def search_title(date):
	# date info needs to be formated YYYY/MM/DD
	year_date_month = date.split('/')
	# make date into EPOCH
	epoch = datetime.datetime(*year_date_month, 0, 0, 0).strftime('%s')
	output = []
	for filename in os.listdir("Notes"):
		# get the time file was last modified
		modified = os.path.getmtime(filename)
		if modified >= epoch:
			output.append([filename, modified])
	return output

# date is in format zero width space "YYYY-MM-DD" zero width space on its own line
def search_for_modfication_on_date(date):
	records = open('lastmodified.csv','r')
	for l in records:
		i = 0
		filename = line.split(",")[1]
		for c in l:
			if date[i] != c:
				break
			if i > 2 && date[i] == chr(0x1F):
				return filename
	return FALSE
# Prototype, tests still need to be written


# Fully deletes a file
def remove_file(file):
	os.remove(file)
	save_modified(file, date = date.today())

# Fully clears the file where info is stored
def del_file_contents(file):
	with open(file,'r+') as file:
		file.truncate(0)
	save_modified(file, date = date.today())

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
		f.write(chr(0x1F) + str(date) + chr(0x1F) + '\n' )
		# Using chr(0x1F) as it returns a standard ascii or unicode character of the unit seperator, a reserved character
		f.write(contents)
	save_modified(filename, date)
# if filename doesn't exist, return a string with error message
# if filename exists, return a string with its contents
def view(filename):
	if search_for_filename(filename):
		with open("./Notes/" + filename, "r+") as f:
			s = f.read()
	else:
		s = "false"
	return s

# list files in notes directory
def list():
	output = ""
	for file in os.listdir("Notes"):
		output += file + "\n"

	return output


# This function operates by generating a text box (easyGUI) that is platform agnostic and allows for simple editing
# while being less signifigant and easier to use than a full on text editor (VIM, NANO, platform specific editor, etc.)
def input_pre_filled(prompt, prefill):
	#Pass a prompt as if operating a normal input() statement and then a prefill which will fill the text box.
	assert input == type("String")
	input = easygui.enterbox(prompt, title="Input", default = prefill)
	if input is None:
		input = prefill
	#returns the input from the user in the form of a string
	return input

# This function allows for editing using the easyGUI functionality outlined in input_pre_filled in order to faclite very
# basic editing. 
# NOTE: line breaks are preseverd but in the editing functionality are saved as zerospaces for some reason.
# Possible solutions: replace the character for spaces with LaTeX formatting (i.e. \newline ) and therefore allow the user
# easy addition of characters not well represented by the easyGUI.
def enter_edit(file, date=date.today()):
	#Pass a file in order to edit, optionally add a date to save as the date of modification
	contents = open(file,'r')
	contents = input_pre_filled("Edit in the text box", contents)
	del_file_contents(file)
	write(contents, filename = file)
	with open(file, "a") as f:
		f.write(chr(0x1F) + str(date) + chr(0x1F) + '\n')
	save_modified(file, date)
		# Using chr(0x1F) as it returns a standard ascii or unicode character of the unit seperator, a reserved character
	#This function does not return anything
 