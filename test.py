import backend

assert (backend.search_for_filename("testnote.md"))
assert (backend.search_for_filename("doesntexist.md")) == False
print(backend.list())

print("Tests passed.")
