# noteworthy
a local note taking app written in Python.

## Install
To install this package run
```
>>> git clone https://github.com/augustus-thomas/noteworthy
>>> cd noteworthy
>>> ./install
```


## Usage

### Help
For help with this package run
```
>>> noteworthy --help
```

### Add
Create a new file in the noteworthy directory.

```
>>> noteworthy add new_notes.md
>>> Added new_notes.md
>>>
```

Take your notes and then exit with CRTL+D.

### View
View a file saved in the noteworthy directory.
```
>>> noteworthy view new_notes.md
>>> Assume that software development exists... Then it can be said that
```

### List
Show files in the noteworthy directory.
```
>>> noteworthy list
>>> /new_notes.md
>>> /SoftwareDevelopment.md
>>> /AlgorithmicAnalysis.md
>>> /ComputationalPhysics.md
```

### Search
Search for a file in the noteworthy directory.

Search by date. 
You can search before a date.
```
>>> noteworthy search --after 2024-01-01
>>> There are 2 matches. They are:
>>> SoftwareDevelopment.md: Created on 2024-01-21
>>> AlgorithmicAnalysis.md: Created on 2024-02-3
```
You can search after a date.
```
>>> noteworthy search --before 2024-01-01
>>> There are 1 matches. They are:
>>> ComputationalPhysics.md: Created on 2023-12-13
```
Search by title.
```
>>> noteworthy search --title new_notes.md
>>> There is 1 match. Display it? (y/[n])
>>> Assume that software development exists... Then it can be said that
```

