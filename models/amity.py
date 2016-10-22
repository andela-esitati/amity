from person import Fellow, Staff
from rooms import LivingSpace, Office
import random


class Amity(object):
    '''This class contains all rooms and all people in amity'''

    def __init__(self):
        self.all_rooms = []
        self.office_rooms = []
        self.livingspaces = []
        self.all_people = []
        self.fellows = []
        self.staff = []

    def create_room(self, name, type_room):
        '''this method create rooms.its can create multiple rooms'''
        if type_room == 'livingspace':
            room = LivingSpace(name)
            self.livingspaces.append(room)
            self.all_rooms.append(room)

        elif type_room == 'office':
            room = Office(name)
            self.office_rooms.append(room)
            self.all_rooms.append(room)

    def add_person(self, name, role, wants_accomodation='N'):
        '''this method creates a person and allocats the person a room'''
        if role == 'fellow':
            person = Fellow(name)
            # pick an office at random from the office_list
            randomized_office = random.choice(self.office_rooms)
            # assign an office to a person
            if randomized_office.is_not_full:
                person.office = randomized_office
                # adding a person to the member list in office
                randomized_office.members.append(person)
            if wants_accomodation == 'Y':
                # pick a random living space from living space lists
                random_livingspace = random.choice(self.livingspaces)
                if random_livingspace.is_not_full:
                    # assign living space to a person
                    person.hostel = random_livingspace
                    # add a person to the member list in office
                    random_livingspace.members.append(person)
            # add the person to fellows list
            self.fellows.append(person)
            # add the person to all rooms
            self.all_people.append(person)

        elif role == 'staff':
            person = Staff(name)
            # pick a random office
            randomized_office = random.choice(self.office_rooms)
            if randomized_office.is_not_full:
                # assign an office to a person
                person.office = randomized_office
                # adding a person to the member list in staff
                randomized_office.members.append(person)

            # assign the person to the staff list
            self.staff.append(person)
            # add staff to all people
            self.all_people.append(person)

    def reallocate_person(self, name, new_room):
        # go through the list of all people
        for people in self.all_people:
            # checking if that person exists
            if name == people.name:
                person_found = people
                break

        # go through a list of all_rooms
        for room in self.all_rooms:
            # check that new room is already there
            if new_room == room.name:
                # check wether room is an office
                if isinstance(room, Office):
                    # check that room is not full
                    if room.is_not_full:
                        # add person to members of a room
                        room.members.append(person_found)
                        # remove the person from the previous office
                        person_found.office.members.remove(person_found)
                        # renaming person office
                        person_found.office = room
                # check wether  room is a living space
                if isinstance(room, LivingSpace):
                    # check that room is not full
                    if room.is_not_full:
                        room.members.append(person_found)
                        person_found.hostel.members.remove(person_found)
                        person_found.hostel = person_found

    def load_people(self, file):
        '''this function reads a lists of people and allocates them a room'''
        with open(file, 'r') as file:
            # read the file content line by line
            file_content = file.readlines()
            # go through the list of file content
            for line in file_content:
                information = line.split()
                first_name = information[0]
                second_name = information[1]
                name = first_name + ' ' + second_name
                person_role = information[2].lower()
                # look for wanting accomadation option
                try:
                    staying = information[3]
                # incase there is no accomodation info
                except IndexError:
                    pass
                self.add_person(name, person_role, staying)

    def print_allocations(self, filename='nofilename'):
        '''this function prints everyone who has been alloacted a room'''
        rooms = self.all_rooms
        if filename is None:
            # go through all rooms in amity
            for room in rooms:
                # go through each member in a room
                for member in room.members:
                    print member
        else:
            for room in rooms:
                for member in room.members:
                    with open(filename, 'a') as allocated_people:
                        allocated_people.write(member.name)

    def print_un_allocated(self, filename='nofilename'):
        '''this fuction prints a list of all fellows without living spaces'''
        if filename is None:
            allocated_people = []
            hostels = self.livingspaces
            for hostel in hostels:
                for member in hostel.members:
                    allocated_people.append(member)
            fellows = self.fellows
            for fellow in fellows:
                if fellow not in allocated_people:
                    print fellow.name
        else:
            allocated_people = []
            hostels = self.livingspaces
            for hostel in hostels:
                for member in hostel.members:
                    allocated_people.append(member)
            fellows = self.fellows
            for fellow in fellows:
                if fellow not in allocated_people:
                    with open(filename, 'a') as unallocated_people:
                        unallocated_people.write(fellow.name)


amity = Amity()
amity.create_room('valhalla', 'office')
amity.create_room('php', 'livingspace')
amity.create_room('haskel', 'livingspace')
amity.add_person('sam', 'fellow')
print amity.all_rooms
print amity.office_rooms
y = amity.fellows[0]
print y
print y.office
print amity.office_rooms[0].members
amity.create_room('hogwarts', 'office')
print amity.all_rooms
print amity.office_rooms
amity.reallocate_person('sam', 'hogwarts')
y = amity.fellows[0]
print y.office
print amity.office_rooms[0].members
print amity.office_rooms[1].members
print 'hae'
amity.load_people('people.txt')
print amity.all_people
print 'hae'
amity.print_allocations()
print 'unallocated'
amity.print_un_allocated()
