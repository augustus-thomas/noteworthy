import os
bold_text = '\033[1m'
end_color = '\033[0m'
purple_text = '\033[95m'
underline_text = '\033[4m'
blue_text = '\033[96m'
underline_text = '\033[4m'
red_text = '\033[91m'

def Help(): 
    print(f"\n{bold_text}{purple_text}Noteworthy Help Manuel{end_color}\n")
    print(f"{blue_text}")
    print("Type 'syntax' for information relating to Markdown Syntax")
    print("Type 'date' for information about date formatting for this app\n")
    
    help_variable = input("What do you need help with? ")

    if help_variable == "syntax":
        print ("Markdown Syntax Guide: https://www.markdownguide.org/")
    elif help_variable == "date": 
        print ("Date Format: mm-dd-yyyy")
    else: 
        print ("Function not Available")
        exit()
    
    print(f"{end_color}")
    
def AddNotes(): 
    print (f"{bold_text}{purple_text}\nAdd Notes{end_color}")
    print (f"{blue_text}")
    name_of_file = input("Name of Markdown File to add to: ")
    name_of_file = f"Notes/{name_of_file}"
    date_of_file = input(f"Input today's Date: ")

    if not ".md" in name_of_file:
        name_of_file = f"{name_of_file}.md"
    
    with open(name_of_file, 'a') as w: 
        w.write(date_of_file)
        print("Type notes here (Press return for new line and type END whenever you are done with your notes): ")
        continue_adding = True
        while continue_adding == True: 
            notes = input()
            if notes == "END": 
                break
            w.write('\n')
            w.write(notes)

        w.write('\n\n')
    print(f"{end_color}")

#Start of Trenton New Code
    
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

#End of Trenton New Code
    
#Start of mkdown pdf conversion

def MKDownToPdf():
    read_input = input(f"{blue_text}Input the file name which you wish to convert to PDF. (Format: filename.md): ")
    #Passes to backend for conversion
    


#End of mkdown pdf conversion
def ListNotes(): 
    print(f"{bold_text}{purple_text}\nList of Files{end_color}")
    print(f"{blue_text}")
    
    list_of_notes = (os.listdir("Notes"))
    for note in list_of_notes:
        print(note)
    
    print(f"{end_color}")
    
def ViewNotes(): 
    print(f"{bold_text}{purple_text}\nView Notes{end_color}")
    print(f"{blue_text}")
    read_file = input("Input the Markdown File you wish to view: ")
    if ".md" not in read_file:
        read_file = f"{read_file}.md"
    
    read_file = f"Notes/{read_file}"
        
    if not os.path.isfile(read_file):
        print(f"{read_file} Does Not Exist")
        print("Use the AddNotes() function if you wish to create this file")
        exit()
    else:    
        with open(read_file, 'r') as r:
            note_content = r.read()
            print(note_content)
    
    print(f"{end_color}")
    
def main(): 
    print(f"{bold_text}{purple_text}Welcome to Noteworthy - The #1 Notetaking Application For Markdown{end_color}\n")
    print(f"{blue_text}")
    print("Available Functions:")
    print("'add': to add notes")
    print("'search': to search notes")
    print("'list': to list notes")
    print("'view': to view notes")
    print("'help': to access the help manuel")
    
    intended_action = input("Do you wish to add, search, list, view, or access the help manuel? ")
    
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
    else: 
        print("This function does not exist\n")
        exit()
    
    print(f"{end_color}")
    
main()