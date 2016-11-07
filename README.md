

Amity has rooms which can be offices or living spaces. An office can occupy a maximum of 6 people. A living space can inhabit a maximum of 4 people.

A person to be allocated could be a fellow or staff. Staff cannot be allocated living spaces. Fellows have a choice to choose a living space or not.

This system will be used to automatically allocate spaces to people at random.

# Installation

Clone this repo:
```
$ git clone https://github.com/andela-esitati/amity
```


Navigate to the `amity` directory:
```
$ cd amity
```

Create a virtual environment and activate it using [this guide](http://docs.python-guide.org/en/latest/dev/virtualenvs/)

Install dependancies:
```
$ pip install -r requirements.txt
```


Run tests to ensure everything is working as expected:
~~~
$ python tests.py
............
----------------------------------------------------------------------
Ran 12 tests in 0.232s

OK
~~~

# Usage

Get into interactive mode:
~~~
$ ./amity.py -i
Welcome to Amity. Amity helps you allocate rooms to people at random.
 (type help for a list of commands.)
~~~

### Help
Typing help gives you a list of available commands
~~~
(Amity) help

Documented commands (type help <topic>):
========================================
add_person     help         print_all_rooms    print_unallocated  save_state
create_room    load_people  print_allocations  quit
get_person_id  load_state   print_room         reallocate_person
~~~
Typing `help` with a command shows information about that command:
~~~
(Amity) help print_room

        Prints  the names of all the people in room_name on the screen

        Usage:
            print_room <room_name>
~~~

### Create room(s)
~~~
create_room <room_name> <room_type>
~~~
Creates a room in Amity.
Specify if the room is an office or living space by entering the required option when prompted:
~~~
(Amity) create_room Room1 office
Room1 has been created successfully
~~~

### Add person
~~~
(Amity) add_person <person_first_name> <person_other_name> <person_type> [<wants_accommodation>]
~~~
Adds a person to the system and allocates the person to a random room.
`wants_accommodation` here is an optional argument which can be either Y or N. The default value if it is not provided is N.
~~~
(Amity) add_person Elsis Sitati Fellow Y
FELLOW Jimmy Kamau has been added to the system. The office: Room1, and living space: Living3 has been allocated to them
~~~
~~~
(Amity) add_person Jane Doe Staff
STAFF Jane Doe has been added to the system. The office: Room1 has been allocated to them
~~~

### Reallocate person
~~~
(Amity) reallocate_person <person_identifier> <new_room_name>
~~~
Reallocate the person with `person_identifier` to `new_room_name`.
~~~
(Amity) reallocate_person 1 Room2
Jimmy Kamau has been moved to Room2
~~~

### Load people
~~~
(Amity) load_people <filename>
~~~
Adds people to rooms from a txt file
~~~
(Amity) load_people test_people.txt
FELLOW John Doe has been added to the system. The office: Room1, and living space: Living3 has been allocated to them
STAFF An Other has been added to the system. The office: Room2 has been allocated to them
FELLOW Jack Knife has been added to the system. The office: Room1, and living space: Living3 has been allocated to them
FELLOW Young Person has been added to the system. The office: Room2 has been allocated to them
STAFF New Staff has been added to the system. The office: Room2 has been allocated to them
Finished adding people
~~~

### Print allocations
~~~
(Amity) print_allocations [-o <file_location>]
~~~
Prints a list of allocations onto the screen.
~~~
(Amity) print_allocations
Living1
----------------------------------------



Room1
----------------------------------------
Jane Doe, John Doe, Jack Knife,


Room2
----------------------------------------
Elsis Sitati, An Other, Young Person, New Staff,


Living3
----------------------------------------
Elsis Sitati, John Doe, Jack Knife,


Living2
----------------------------------------

~~~
Specifying the optional `-o` option here outputs the registered allocations to the txt file specified by `<file_location>`.

### Print unallocated
~~~
(Amity) print_unallocated [-o <file_location>]
~~~
Prints a list of unallocated people to the screen.
~~~
(Amity) print_unallocated
Witha Knife hasn't been allocated to an office or a living space
Wither Spoon hasn't been allocated to an office
~~~
Specifying the optional `-o` option here outputs the information to the txt file specified by `<file_location>`.

### Database operations
#### Saving to database



# To do

* Fix `print_allocations` and `print_unallocated` tests failing if called after index 7
* Find a better way to order tests
* Add functionality to automatically allocate unallocated people to rooms
* Add functionality to delete databases from the interactive interface
