"""
Usage:
    create_room (Living|Office) <room_name>...
    add_person <person_name> (Fellow|Staff) [--accomodation=no]
    reallocate_person <person_name> <new_room_name>
    load_people <filename>
    print_allocations [<file_name>]
    print_unallocated [--o=filename]
    print_room <room_name>
    save_state [--db=sqalchemy_database]
    load_state <sqalchemy_database>
    quit

Options:
    --h               Show this screen.
    --o               Specify filename
    --db              Name of SQAlchemy database
    --accommodation   If person needs accommodation [default='no']

"""

from docopt import docopt, DocoptExit
import cmd
from app.amity import Amity

amity = Amity()


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as exit:
            # Thrown when args do not match

            print("You have entered an invalid command!")
            print(exit)
            return

        except SystemExit:
            # Prints the usage for --help
            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


def intro():
    print ("WELCOME TO AMITY SPACE ALLOCATION!".center(70))
    print ("Allocate rooms to staff and fellows in Amity".center(70))
    print ("-> help".center(70))
    print ("-> quit".center(70))


class AmityInteractive(cmd.Cmd):
    prompt = 'Amity#  '

    @docopt_cmd
    def do_create_room(self, arg):
        """Usage: create_room <room_name> <room_type>"""
        room_name = arg['<room_name>']
        room_type = arg['<room_type>']

        amity.create_room(room_name, room_type)
        print amity.all_rooms

    @docopt_cmd
    def do_add_person(self, arg):
        """
        Creates a person and assign them to a room in Amity.
        Usage:
            add_person <first_name> <last_name> <role> [--wants_accomodation='N']
        """
        name = arg['<first_name>'] + " " + arg["<last_name>"]
        role = arg['<role>']
        wants_accomodation = arg['--wants_accomodation']
        amity.add_person(name, role, wants_accomodation)
        print '%s has been created and given a room' % name

    @docopt_cmd
    def do_reallocate_person(self, arg):
        """
        Reallocated a person to a new room
        Usage:
            reallocate_person <first_name> <last_name> <new_room>
        """
        name = arg['<first_name>'] + " " + arg["<last_name>"]
        new_room = arg['<new_room>']
        amity.reallocate_person(name, new_room)
        print '%s now has %s' % (amity.office_rooms[1], amity.office_rooms[1].members)

    @docopt_cmd
    def do_load_people(self, arg):
        """
        this function reads a lists of people and allocates them a room
        Usage:
            load_people <file_name>
        """
        filename = arg['<file_name>']
        amity.load_people(filename)
        print 'People in %s have been added and allocated rooms' % filename
        print '%s ' % amity.all_people

    @docopt_cmd
    def do_print_allocations(self, arg):
        """
        This fuction prints a list of all people who have been allocated a room
        Usage:
            print_allocations [<file_name>]
        """
        filename = arg['<file_name>']
        amity.print_allocations(filename)
        print 'The names have been printed to %s' % filename

    @docopt_cmd
    def do_print_un_allocated(self, arg):
        """
        This fuction prints a list of all fellows without living spaces
        Usage:
            print_un_allocated [<file_name>]
        """
        filename = arg['<file_name>']
        amity.print_un_allocated(filename)
        print 'The names have been printed to %s' % filename

    @docopt_cmd
    def do_print_room(self, arg):
        """
        This function prints the members of a given room
        Usage:
            print_room <room_name>
        """
        room_name = arg['<room_name>']
        amity.print_room(room_name)

    @docopt_cmd
    def do_save_state(self, arg):
        """
        This function prints the members of a given room
        Usage:
            save_state [--db_name=amity_db]
        """
        db_name = arg['--db_name']
        amity.save_state(db_name)




if __name__ == '__main__':
    AmityInteractive().cmdloop()
