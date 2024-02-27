# Description 
Welcome to Noteworthy! We are the #1 notetaking application for markdown files. Some of our current available functions >>> include writing, viewing, searching, listing, deleting, and clearing. If you have any questions relating to Markdown the link below provides useful information
[Markdown Guide](https://www.markdownguide.org/)

# Set Up/Installation 
You can access the required code for the Noteworthy application using the "Noteworthy Code" link. Furthermore, it is worth noting that this is a command line application so no external downloads are required. Finally, you need to ensure you have a "Notes" subfolder inside of your Noteworthy directory and a csv file with the name of "lastmodified.csv". Furthermore, if you wish to run this application from the command line then the file you should run is "Frontend.py"
[Noteworthy Code](https://github.com/augustus-thomas/noteworthy)

Additionally, you can install Noteworthy from the command line by running
```
$ git clone https://github.com/augustus-thomas/noteworth
```

Finally, install the Python package requirements by navigating to `noteworthy` and running

```
$ pip3 install -r requirements.txt
```

# Current Functions
### Home Page 
The purpose of the homepage is to allow you to access all the available functions for the application. For example, if you want to add notes to a file then you would type "add" while on the homepage. Furthermore, if you wish to exit the app this can also be done through the home page. 

Code Example
```
>>> What would you like to do? add
```

### Write to file 
This function allows you to both write to existing files and create new files to write to. This writing function can be accessed in the home page by typing "add" when prompted to specify the action you want to perform. The creation of a new file can be done by typing in the name of the file you wish to create when prompted. Furthermore, when you access this function you will be prompted to specify the name of a file you wish to write to, the date (yyyy/mm/dd), and finally what you wish to write. You can press your return key to start a new line and '*END' to stop writing to a file. 

Code example: 
```
>>>  Name of Markdown File to add to: file.md
>>>  Input today's date: yyyy/mm/dd
```

### Viewing text in a file 
This function allows you to see the notes you have written in a specified file. This function can be accessed in the home page by typing "view" when prompted to specify the action you wish to perform. In order to view the notes of a file you simply type in the name of the Markdown file you wish to view when prompted and its contents will print to the command line. 

Code example:
```
>>> Input the Markdown File you wish to view: file.md
```

### Searching for a file 
This function allows you to see the notes included in the Notes folder. This is useful so that users do not need to manually look into their file explorer to see modified dates and note names. This can be accessed in the home page by typing "search" when prompted to specify the action you wish to perform. Afterwards, you specify whether you wish to search for files by modified date or by filename and enter the parameter you wish to search by.

Code example:
```
>>> Would you like to search for file by modified date or by filename?
>>> Input 'date' or 'filename' for preferred search parameters: date
>>> Input the date you wish to search for and specify before or after (Format: 2000/12/31 before): 2024/20/2 after
>>> There are 1 matches. They are:
>>> jump.md: Modified on 2024/22/2
```

### Listing all files 
This function prints out the name of every markdown file you have created for your notes into the command line. This function can be accessed in the home page by typing "list" when prompted to specify the action you wish to perform.

### Deleting a file
This function is used to delete markdown files that you no longer want in your notes. This function can be accessed in the home page by typing "delete" when prompted to specify an action you wish to perform. This function can be used by typing the name of the file you want to delete into the command line when prompted. 

Code example:
```
>>> Enter the name of the note to delete: file.md
```

### Clear a file 
This function is used to clear all the information from a specified markdown file but keep the file itself. This function can be accessed in the home page by typing "clear" when prompted to specify an action you wish to perform. This function can be used by typing the name of the file you wish to clear into the command line when prompted 

Code example:
```
>>> Enter the name of the note to clear: file.md
```

### Help function
This function can be used if you need additional help while using the application. This function can be accessed in the homepage by typing "help" into the command line when prompted to specify an action you wish to perform. Additionally, after accessing this function there are currently three things the user can get help with with prompted.
- "syntax" - allows access to information relating to markdown syntax
- "date" - allows you to access information about date formatting for this application
- "end_of_file" : allows you to access information about how to stop writing to a file

### Exiting the app
You can exit the application from the homepage by typing "exit" into the command line when prompted to specify the action you wish to perform. 

Code example:
```
>>> exit
```

# Contributors 
Christopher Vann, Augustus Thomas, Nicco Herman, Jecolia Teferi, Trenton Ferrel


