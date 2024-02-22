import backend
from backend import input_pre_filled
from backend import enter_edit
# search for filename tests
assert (backend.search_for_filename("testnote.md"))
assert (backend.search_for_filename("doesntexist.md")) == False

# search by date

# search_for_modfication_on_date

# write
backend.write("Hello file", filename="test.md") # no optional
backend.write("Hello file") # no filename
backend.write("Goodbye file", date = '2023-07-22') # date no filename
backend.write("Both file", date='2023-08-01', filename='both.md') # both


# view
# assert backend.view("test.md") == "Hello file" difficult to write tests with date feature in file
print(backend.list())
print(backend.view('testnote.md'))


print("Tests passed.")

input_test = input_pre_filled("Here is some test stuff, edit it","Here is the premade text to edit")
print(input_test)
print("easyGUI + input_pre_filled test passed")

enter_edit("testnote.md")
print("editing passed")