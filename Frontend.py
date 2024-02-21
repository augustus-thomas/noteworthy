import os
import backend
import time 

bold_text = '\033[1m'
end_color = '\033[0m'
purple_text = '\033[95m'
underline_text = '\033[4m'
blue_text = '\033[96m'
underline_text = '\033[4m'
red_text = '\033[0;31m'
#Idea - Text editor in the command line 
#Does anyone have any other ideas 
#C - add, view, main, stylstic choices (color, bold), help, introduction, Noteworthy User Manual
#T - search, markdown to PDF (I just figure we can add this feature because it shouldn't be too difficult), 
#J - clear notes, delete files, list notes, edit notes (This one might be difficult to do)

def Help(): 
    print(f"\n{bold_text}{purple_text}Noteworthy Help Manuel{end_color}\n")
    print(f"{blue_text}")
    
    print(f"{underline_text}Help Functions{end_color}{blue_text}")
    print("     syntax: information relating to Markdown Syntax")
    print("     date: information about date formatting for this app")
    print("     end_of_file: information about how to stop taking notes\n")
    
    help_variable = input(f"{underline_text}What do you need help with?{end_color}{blue_text} ")

    if help_variable == "syntax":
        print ("Markdown Syntax Guide: https://www.markdownguide.org/")
    elif help_variable == "date": 
        print ("Date Format: yyyy-mm-dd")
    elif help_variable == "end_of_file":
        print ("Stop Writing to File: 'ctrl + D' ")
    else: 
        print ("Function not Available")
        exit()
        
    
    print(f"{end_color}")
    main()
    
def AddNotes(): 
    print (f"{bold_text}{purple_text}\nAdd Notes{end_color}")
    print (f"{blue_text}")
    name_of_file = input(f"{underline_text}Name of Markdown File to add to:{end_color}{blue_text} ")
    name_of_file = f"Notes/{name_of_file}"
    date_of_file = input(f"{underline_text}Input today's Date:{end_color}{blue_text} ")
    date_of_file = f"Date: {date_of_file}"
    if not ".md" in name_of_file:
        name_of_file = f"{name_of_file}.md"
    
    print(f"{underline_text}Type notes below: {end_color}{blue_text}\n")
    print("     return key: Start a new line")
    print("     ctrl + d keys: Stop typing to file\n")
    
    content = []
    while True: 
        try: 
            line = input("")
        except EOFError:
            break 
        content.append(f"\n{line}")

    content_string = ' '.join([str(item) for item in content])
    backend.write(content_string, date_of_file, name_of_file)
        
    print(f"{end_color}")
    main()
    
def SearchNotes():
    print(f"{bold_text}{purple_text}\nSearch Notes{end_color}")
    print(f"{blue_text}Would you like to search for file by modified date or by filename?")
    #Takes user input for date or filename for preference.
    read_input = input(f"{blue_text}Input 'date' or 'filename' for preferred search parameters: ")
    if read_input == "date":
        read_input = input(f"{blue_text}Input the date you with to search for (Format: 2000/12/31): ")
        #Passes to backend to have search_for_file ran
        print("There are " + n + " matches. They are: ")
        #print(##search_by_date filenameoutput + ": Created on " + ##search_for_file dateoutput)

    if read_input == "filename":
    
        read_input = input(f"{blue_text}Input the filename that you wish to search for (Format: filename.md): ")
        #Makes it an .md file if not inputted at first
        if ".md" not in read_input:
            read_input = f"{read_input}.md"
        #Passes to backend to have search_for_file ran
        print("There are " + n  + " matches. They are: ")
        #print(##search_for_file filenameoutput ": Created on " ##search_for_file dateoutput)
    
    
    print(f"{end_color}")
    main()

def ListNotes(): 
    print(f"{bold_text}{purple_text}\nList of Files{end_color}")
    print(f"{blue_text}")
    
    list_of_notes = (os.listdir("Notes"))
    for note in list_of_notes:
        print(note)
    
    print(f"{end_color}")
    main()
    
def ViewNotes(): 
    print(f"{bold_text}{purple_text}\nView Notes{end_color}")
    print(f"{blue_text}")
    read_file = input(f"{underline_text}Input the Markdown File you wish to view: {end_color}{blue_text}")
    if ".md" not in read_file:
        read_file = f"{read_file}.md"
        
    print(backend.view(read_file))
    
    print(f"{end_color}")
    main()

def ClearNotes():
    print(f"{bold_text}{purple_text}\nClear Notes{end_color}")
    print(f"{blue_text}")

    confirmation = input("Are you sure you want to clear all notes? (yes/no): ").lower()
    if confirmation == "yes":
        for file in os.listdir("Notes"):
            os.remove(os.path.join("Notes", file))
        print("All notes have been cleared.")
    elif confirmation == "no":
        print("Clear operation cancelled.")
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

    print(f"{end_color}")
    main()

def DeleteNote():
    print(f"{bold_text}{purple_text}\nDelete Note{end_color}")
    print(f"{blue_text}")

    filename = input("Enter the name of the note to delete (without .md extension): ")
    if ".md" not in filename:
        filename += ".md"
    filepath = os.path.join("Notes", filename)

    if os.path.exists(filepath):
        os.remove(filepath)
        print(f"{filename} has been deleted.")
    else:
        print(f"Error: {filename} does not exist.")

    print(f"{end_color}")
    main()

def MKDownToPdf():
    read_input = input(f"{blue_text}Input the file name which you wish to convert to PDF. (Format: filename.md): ")
    
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
    elif intended_action == "exit":
        exit()
    else: 
        print(f"{red_text}Invalid input. Please try again.\n{end_color}")
        time.sleep(1)
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
