# functions for backend calls
import os
import time
from datetime import date

#import easygui

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
#		f.write('\u2001' + str(date) + '\u2001' + '\n')
#		I am having issues with this line, keep getting the error:
#		UnicodeEncodeError: 'charmap' codec can't encode character '\u2001' in position 0: character maps to <undefined>
#		So for now I am commenting it out, with the plan to look further into it
		f.write(contents)

# if filename doesn't exist, return a string with error message
# if filename exists, return a string with its contents
def view(filename):
	if search_for_filename(filename):
		with open("./Notes/" + filename, "r+") as f:
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


# This function operates by generating a text box (easyGUI) that is platform agnostic and allows for simple editing
# while being less signifigant and easier to use than a full on text editor (VIM, NANO, platform specific editor, etc.)
def input_pre_filled(prompt, prefill):
	input = easygui.enterbox(prompt, title="Input", default = prefill)
	if input is None:
		input = prefill
	return input

# Concept for an edit function
def enter_edit(file):
	contents = view(file)
	print(contents)
	contents = input_pre_filled("Edit in the text box", contents)
	del_file_contents(file)
	write(contents, filename = file)
 