import os
import backend
import time
import re

#1 

bold_text = '\033[1m'
end_color = '\033[0m'
purple_text = '\033[95m'
underline_text = '\033[4m'
blue_text = '\033[96m'
underline_text = '\033[4m'
red_text = '\033[0;31m'
#Idea - Text editor in the command line 
#Does anyone have any other ideas 
#C - add, view, main, stylstic choices (color, bold), help, introduction, Noteworthy User Manual, Markdown to PDF 
#T - search
#J - clear notes, delete files, list notes, edit notes (This one might be difficult to do)

def Help(): 
    print(f"\n{bold_text}{purple_text}Noteworthy Help Manuel{end_color}\n")
    print(f"{blue_text}")
    
    print(f"{underline_text}Help Functions{end_color}{blue_text}")
    print("     syntax: information relating to Markdown Syntax")
    print("     date: information about date formatting for this app")
    print("     end_of_file: information about how to stop taking notes")
    print("     user_manual: information for code examples, documentation and use.\n")
    
    help_variable = input(f"{underline_text}What do you need help with?{end_color}{blue_text} ")

    if help_variable == "syntax":
        print ("Markdown Syntax Guide: https://www.markdownguide.org/")
        time.sleep(1.5)
    elif help_variable == "date": 
        print ("Date Format: yyyy-mm-dd")
        time.sleep(1.5)
    elif help_variable == "end_of_file":
        print (f"Stop Writing to File: (Mac:) 'ctrl + D'")
        print(f"Windows: 'ctrl + z'")
        time.sleep(1.5)
    elif help_variable == "user_manual":
        incoming_input = 'NoteworthyUserManual.md'
        with open(incoming_input, "r+") as f:
            s = f.read()
        print(s)
        time.sleep(1.5)
    else: 
        print (f"{red_text}Function not Available{end_color}")
        time.sleep(1.5)
    
    print (f"{end_color}") 
    main()
    
def AddNotes(): 
    print (f"{bold_text}{purple_text}\nAdd Notes{end_color}")
    print (f"{blue_text}")
    name_of_file = input(f"{underline_text}Name of Markdown File to add to:{end_color}{blue_text} ")
    name_of_file = f"{name_of_file}"
    date_of_file = input(f"{underline_text}Input today's Date:{end_color}{blue_text} ")
    date_of_file = f"{date_of_file}"
    if not ".md" in name_of_file:
        name_of_file = f"{name_of_file}.md"
    
    print(f"{underline_text}Type notes below: {end_color}{blue_text}\n")
    print("     return key: Start a new line")
    print("     ctrl + d for mac: Stop typing to file")
    print("     ctrl + z for windows: Stop typing to file\n")
    
    content = []
    while True: 
        try: 
            line = input("")
        except EOFError:
            break 
        content.append(f"\n{line}")

    content_string = ' '.join([str(item) for item in content])
    backend.write(content_string, date_of_file, name_of_file)
        
    print("Notes added to file successfully")
    time.sleep(1.5)
    print(f"{end_color}")
    main()
    
def SearchNotes():
    print(f"{bold_text}{purple_text}\nSearch Notes{end_color}")
    print(f"{blue_text}Would you like to search for file by modified date or by filename?")

    #Takes user input for date or filename for preference.
    read_input = input(f"{blue_text}Input 'date' or 'filename' for preferred search parameters: ")

    if read_input == "date":
        read_input = input(f"{blue_text}Input the date you wish to search for and specify before or after (Format: 2000/01/01 before): ")
        
        
        #This part is temporary as I'm not sure whether functions are going to include before or after input, it just references it in specs.
        split_input = read_input.split(" ")
        #If format doesn't have two terms
        if len(split_input) != 2:
            return
        date = split_input[0]
        searchDirection = split_input[1]

        check = 0
        regex_list = ['\d{4}/\d{2}/\d{2}']
        for pattern in regex_list:
            if re.match(pattern,date):
                check = 0
            else:
                check = 1
        
        if check == 1:
            print(f"Improper Format. The format is YYYY/MM/DD.")
            print(f"Ensure you have '0's in single digit dates.")
            time.sleep(1.5)
            main()
        
        #Passes to backend to have search_for_file ran
        #Takes the output and sets it to a variable, finding the length of the array to find how many terms there are, then going through while statement to print results.
        #Might recommend a name change for "search_title" as it was searching by date instead of title.
        searchOutput = backend.search_date(date, searchDirection)
        if searchOutput == 0:
            print("Error in search. Files could not exist or format was not properly used.")
            main()
        n = len(searchOutput)
        print(f"{blue_text}There are " + str(n) + f"{blue_text} matches. They are: ")
        x = 0
        while x < n:
            print(searchOutput[x][0] + f"{blue_text}: Modified on " + searchOutput[x][1])
            x += 1
            
        time.sleep(1.5)

    if read_input == "filename":
        read_input = input(f"{blue_text}Input the filename that you wish to search for (Format: filename.md): ")

        #Makes it an .md file if not inputted at first
        if ".md" not in read_input:
            read_input = f"{read_input}.md"

        #Passes to backend to have search_for_file ran
        #Takes the output and sets it to a variable, finds the length to find how many terms, then prints them.
        searchOutput = backend.search_for_filename(read_input)
        #Expecting some possible false statement if file doesn't exist.
        if searchOutput == 0:
            print("Error in search. Files could not exist or format was not properly used.")
            main()
        n = len(searchOutput)
        print(f"{blue_text}There are " + str(n)  + f"{blue_text} matches. They are: ")
        x = 0
        while x < n:
            print(searchOutput[x][0] + f"{blue_text}: Modified on " + searchOutput[x][1])
            x += 1
    
        time.sleep(1.5)

    print(f"{end_color}")
    main()
    
def ListNotes(): 
    print(f"{bold_text}{purple_text}\nList of Files{end_color}")
    print(f"{blue_text}")
    
    list_of_notes = (os.listdir("Notes"))
    for note in list_of_notes:
        print(note)
        
    time.sleep(2)
    print(f"{end_color}")
    main()
    
def ViewNotes(): 
    print(f"{bold_text}{purple_text}\nView Notes{end_color}")
    print(f"{blue_text}")
    read_file = input(f"{underline_text}Input the Markdown File you wish to view: {end_color}{blue_text}")
    if ".md" not in read_file:
        read_file = f"{read_file}.md"
    
    if not backend.view(read_file):
        print(f"{red_text}File does not exist{end_color}")
        time.sleep(1.5)
    else: 
        print(backend.view(read_file))
        time.sleep(2)
    
    print(f"{end_color}")
    main()

def ClearNotes():
    print(f"{bold_text}{purple_text}\nClear Notes{end_color}")
    print(f"{blue_text}")

    file = input("Input the filename you want to clear: ")
    if ".md" not in file:
        file = f"{file}.md"
    check_for_file = backend.del_file_contents(file)
    if not check_for_file:
        print(f"{end_color}{red_text}Error: {file} does not exist.{end_color}")
        time.sleep(1.5)
    
    else:
        print("Notes cleared Successfully")
        time.sleep(1.5)
    print(f"{end_color}")
    main()

def DeleteNote():
    print(f"{bold_text}{purple_text}\nDelete Note{end_color}")
    print(f"{blue_text}")

    filename = input("Enter the name of the file to delete (without .md extension): ")
    if ".md" not in filename:
        filename = f"{filename}.md"
    check_for_file = backend.remove_file(filename)
    if not check_for_file: 
        print(f"{end_color}{red_text}Error: {filename} does not exist.")
        time.sleep(1.5)
        
    else:
        print("Notes deleted Successfully")
        time.sleep(1.5)

    print(f"{end_color}")
    main()

#def MKDownToPdf():
#    read_input = input(f"{blue_text}Input the file name which you wish to convert to PDF. (Format: filename.md): ")
#    if not backend.MkDownToPDF(read_input):
#        print(f"{red_text}File does not exist{end_color}")
#        time.sleep(1.5)
#    else: 
#        print(f"File converted Successfully{end_color}")
#        time.sleep(1.5)
        
    main()
    
def main(): 
    print(f"{bold_text}{purple_text}\nHomepage{end_color}")
    print(f"{blue_text}{underline_text}")
    print("Available Functions:")
    print(f"{end_color}{blue_text}")
    print("     add: to add notes")
    print("     search: to search notes")
    print("     list: to list notes")
    print("     view: to view notes")
    print("     help: to access the help manual")
    print("     delete: to delete a note")
    print("     clear: to clear all notes")
    print("     convert: to convert MKdown to PDF")
    print("     exit: to exit the app\n")
    
    intended_action = input(f"{underline_text}What would you like to do?{end_color}{blue_text} ")
    
    if intended_action == "add":
        AddNotes()
    elif intended_action == "search":
        SearchNotes()
    elif intended_action == "list":
        ListNotes()
    elif intended_action == "view":
        ViewNotes()
    elif intended_action == "help":
        Help()
    elif intended_action == "delete":
        DeleteNote()
    elif intended_action == "clear":
        ClearNotes()
    elif intended_action == "convert":
        MKDownToPdf()
    elif intended_action == "exit":
        exit()
    else: 
        print(f"{red_text}Invalid input. Please try again.\n{end_color}")
        time.sleep(1.5)
        main()
    
    print(f"{end_color}")

def Introduction():
    print(f"{bold_text}{purple_text}__________________________________________________________________")
    print("__________________________________________________________________\n")
    print("Welcome to Noteworthy - The #1 Notetaking Application For Markdown")
    print("__________________________________________________________________")
    print("__________________________________________________________________")
    
    {end_color}
    main()

    
Introduction()
