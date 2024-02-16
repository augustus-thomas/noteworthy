import backend

assert (backend.search_for_file("testnote.md"))
assert (backend.search_for_file("doesntexist.md")) == False


print("Tests passed.")