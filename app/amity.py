from database import Office as Ofisi, LivingSpace as Hostel, Person as Mtu
from person import Fellow, Staff
from rooms import LivingSpace, Office
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import random
from database import Base


class Amity(object):
    '''This class contains all rooms and all people in amity'''

    def __init__(self):
        self.all_rooms = []
        self.office_rooms = []
        self.livingspaces = []
        self.all_people = []
        self.fellows = []
        self.staff = []
        self.allocated = []
        self.unallocated = []

    def create_room(self, name, type_room):
        '''this method create rooms.it can create multiple rooms'''
        if type_room.lower() == 'livingspace':
            room = LivingSpace(name)
            self.livingspaces.append(room)
            self.all_rooms.append(room)

        elif type_room.lower() == 'office':
            room = Office(name)
            self.office_rooms.append(room)
            self.all_rooms.append(room)

    def add_person(self, name, role, wants_accomodation='N'):
        '''this method creates a person and allocats the person a room'''
        if role == 'fellow':
            person = Fellow(name)
            # pick an office at random from the office_list
            # import pdb; pdb.set_trace()
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

    def print_allocations(self, filename):
        '''this function prints everyone who has been alloacted a room'''
        rooms = self.all_rooms
        if filename is None:
            # go through all rooms in amity
            for room in rooms:
                text = '\n\t' + room.name + '\n' + '-' * 50
                print text
                # go through each member in a room
                for member in room.members:
                    self.allocated.append(member)
                    print '\t' + member.name
        else:
            for room in rooms:
                for member in room.members:
                    self.allocated.append(member)
                    with open(filename, 'a') as allocated_people:
                        allocated_people.write(member.name)

    def print_un_allocated(self, filename):
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
                    self.unallocated.append(fellow)

            print self.unallocated
        else:
            allocated_people = self.allocated
            fellows = self.fellows
            for fellow in fellows:
                if fellow not in allocated_people:
                    self.unallocated.append(fellow)
                    with open(filename, 'a') as unallocated_people:
                        unallocated_people.write(fellow.name)

    def print_room(self, room_name):
        '''this function prints the members of a given room'''
        rooms = self.all_rooms
        print room_name + '\n' +'-'*40
        for room in rooms:
            if room_name == room.name:
                for member in room.members:
                    print member.name 

    def save_state(self, db_name='amity_db'):
        '''This methods saves informatin from the application to the database'''

        if db_name:
            engine = create_engine('sqlite:///%s' % db_name)

        else:
            engine = create_engine('sqlite:///amity_db')

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        # go through every person
        for person in self.all_people:
            # condition for a fellow object
            if isinstance(person, Fellow):
                fellow = Mtu()
                # put data to columns
                fellow.name = person.name
                fellow.role = 'Fellow'
                if person.office is None:
                    fellow.office = 'has no office'
                else:
                    fellow.office = person.office.name
                if person.hostel is None:
                    fellow.living_space = "no room"
                else:
                    fellow.living_space = person.hostel.name

                session.add(fellow)
                session.commit()

            # condition for a Staff object
            elif isinstance(person, Staff):
                staff = Mtu()
                # put data to columns
                staff.name = person.name
                staff.role = 'Staff'

                staff.office = person.office.name

                session.add(staff)
                session.commit()

        # go through all rooms
        for room in self.all_rooms:
            if isinstance(room, Office):
                office_room = Ofisi()
                office_room.name = room.name

                session.add(office_room)
                session.commit()

            elif isinstance(room, LivingSpace):
                hostel_room = Hostel()
                hostel_room.name = room.name
                session.add(hostel_room)
                session.commit()

    def load_state(self, db_name='amity_db'):
        '''this method gets data from the database and feeds it to the app'''
        if db_name is None:
            engine = create_engine('sqlite:///amity_db')
        else:
            engine = create_engine('sqlite:///%s' % db_name)
        Session = sessionmaker(bind=engine)
        session = Session()
        people = session.query(Mtu).all()
        offices = session.query(Ofisi).all()
        livingspaces = session.query(Hostel).all()

        for office in offices:
            office_name = office.name
            office_object = Office(office_name)
            self.office_rooms.append(office_object)
            self.all_rooms.append(office_object)

        for hostel in livingspaces:
            hostel_name = hostel.name
            hostel_object = LivingSpace(hostel_name)
            self.livingspaces.append(hostel_object)
            self.all_rooms.append(hostel_object)

        for person in people:
            full_name = person.name
            role = person.role
            office = person.office
            if role == 'Staff':
                p = Staff(full_name)
                for room in self.all_rooms:
                    if office == room.name:
                        room.members.append(p)
                        break
            elif role == 'Fellow':
                p = Fellow(full_name)
                for room in self.all_rooms:
                    if office == room.name:
                        room.members.append(p)
                        break

                l_space = person.living_space
                for room in self.all_rooms:
                    if room.name == l_space:
                        room.members.append(p)                 
                    
                    
            if role == 'Staff':
                person_object = Staff(full_name)
                self.staff.append(person_object)
                self.all_people.append(person_object)
            elif role == 'Fellow':
                person_object = Fellow(full_name)
                self.fellows.append(person_object)
                self.all_people.append(person_object)

        

# amity = Amity()
# amity.create_room('valhalla', 'office')
# amity.create_room('php', 'livingspace')
# amity.create_room('haskel', 'livingspace')
# amity.add_person('sam maina', 'fellow')
# print amity.all_rooms
# print amity.office_rooms
# y = amity.fellows[0]
# print y
# print y.office
# print amity.office_rooms[0].members
# amity.create_room('hogwarts', 'office')
# print amity.all_rooms
# print amity.office_rooms
# amity.reallocate_person('sam maina', 'hogwarts')
# y = amity.fellows[0]
# print y.office
# print amity.office_rooms[0].members
# print amity.office_rooms[1].members
# print 'hae'
# amity.load_people('people.txt')
# print amity.all_people
# print 'hae'
# amity.print_allocations()
# print 'unallocated'
# amity.print_un_allocated()
# print 'members'
# amity.print_room('php')
# print 'save state'
# amity.save_state()
# print 'load_state'
# amity.load_state()
