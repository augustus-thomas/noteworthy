# functions for backend calls
import os
import time
from datetime import date
from datetime import datetime
import easygui
import pandoc

# CORE FUNCTIONALITY FUNCTIONS
def string_to_epoch(string):
	year_date_month = [int(date_number) for date_number in str(string).split('/')]
	epoch = datetime(*year_date_month).timestamp()
	return epoch

def epoch_to_string(epoch):
	return datetime.fromtimestamp(modified).strftime('%Y/%m/%d')

def format_date(d):
	return d.strftime('%Y/%M/%d')

def does_exist(filename):
	return filename in os.listdir("Notes")

# This function saves a newline to the lastmodified csv that marks some change and the date
def save_modified(file, date):
	assert type(date) == type("string")
	with open('lastmodified.csv','a') as f:
		try:
			f.write(str(date) + chr(0x1F) + "," + file + '\n')
		except:
			print(type(str(date)), type(chr(0x1F)), type(","), type(file), type('\n'))

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


# SEARCH FUNCTIONS
# return a filename, date pair for particular file
def search_for_filename(filename):
	result = []
	with open('lastmodified.csv','r') as lm:
		records = lm.readlines()
	for line in records[1:]:
		this_date, this_filename = line.split(",")
		print(this_filename)
		print(filename)
		this_filename = this_filename.strip()
		if this_filename == filename:
			result.append([this_filename, this_date])
	return result
	
# returns a list of name date pairs [['name.md', '2022/04/11'], ['science.md', '2024/03/01']]
def search_date(date, before_or_after):
	# make date a comparable epoch
	search_epoch = string_to_epoch(date)
	# throw "Error" and return false if you didnt supply correct string
	if before_or_after != "before" and before_or_after != "after":
		print("Error: please supply 'before' or 'after' strings in search")
		return False
	# to store all results
	result = []
	with open('lastmodified.csv','r') as lm:
		records = lm.readlines()
	for line in records[1:]:
		this_date, this_filename = line.split(",")
		this_date = this_date[:-1]
		this_epoch = string_to_epoch(this_date)
		if before_or_after == "before" and this_epoch < search_epoch:
			result.append([this_filename.strip(), this_date])
		if before_or_after == "after" and this_epoch >= search_epoch:
			result.append([this_filename.strip(), this_date])
	if not result:
		return False
	else:
		return result

# returns the content in file from the date requested
def search_content(filename, date):
	pass


# FILE MANAGMENT FUNCTIONS
# list files in notes directory
def list():
	output = ""
	for file in os.listdir("Notes"):
		output += file + "\n"

	return output

# returns True is remove actually happened
# Fully deletes a file
def remove_file(file):
	s = does_exist(file)
	if s:
		os.remove("./Notes/" + file)
		save_modified(file, date = format_date(date.today()))
	else: 
		s = False
	return s

# Fully clears the file where info is stored
def del_file_contents(file):
	if does_exist(file):
		with open("./Notes/" + file,'r+') as file:
			file.truncate(0)
		save_modified(file, date = format_date(date.today()))
		return True
	else:
		return False

# name is a filename. can have .md extension passed
# if it has a period a different extension we will force it to be .md


# FILE MODIFICATION FUNCITONS
# contents are string, filename may or may not already exist
# filename is optional. if none, first word in contents dot md
def write(contents, date=format_date(date.today()), filename=None):
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
	if does_exist(filename):
		with open("./Notes/" + filename, "r+") as f:
			s = f.read()
	else:
		s = False
	return s

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

# MKDownToPDF

# def MKDownToPDF(filename):
#     if search_for_filename(filename):
#     	if filename.find(".") == -1:
#     		pdf_filename = filename + ".pdf"
#     	else:
#     		pdf_filename = filename[:filename.find(".")] + ".pdf"
#     	md2pdf(pdf = "./Notes/" + pdf_filename, md="./Notes/" + filename)