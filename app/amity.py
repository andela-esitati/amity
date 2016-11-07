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
        self.all_people = []
        self.unallocated = []

    def create_room(self, name, type_room):
        '''this method create rooms.it can create multiple rooms'''
        if type_room.lower() == 'livingspace':
            room = LivingSpace(name)
            self.all_rooms.append(room)

        elif type_room.lower() == 'office':
            room = Office(name)
            self.all_rooms.append(room)
        else:
            return 'Invalid Room Type'

    def offices_with_space(self):
        offices_with_space = []
        for room in self.all_rooms:
            if isinstance(room, Office):
                check_capacity = self.is_room_full(room)
                if not check_capacity:
                    offices_with_space.append(room)
        return offices_with_space

    def livingspaces_with_space(self):
        livingspaces_with_space = []
        for room in self.all_rooms:
            if isinstance(room, LivingSpace):
                check_capacity = self.is_room_full(room)
                if not check_capacity:
                    livingspaces_with_space.append(room)
        return livingspaces_with_space

    def add_person(self, name, role, wants_accomodation='N'):
        '''this method creates a person and allocats the person a room'''
        # get offices with spaces
        offices_with_space = self.offices_with_space()

        if role == 'fellow':
            livingspaces_with_space = self.livingspaces_with_space()
            person = Fellow(name)
            # check if its there is no office with space
            if not offices_with_space and not livingspaces_with_space:
                person.living_space = 'N'
                person.office = 'N'
                self.unallocated.append(person)
                print 'No Rooms with spaces'
                return

            if offices_with_space:
                randomized_office = random.choice(offices_with_space)
                randomized_office.members.append(person)
                self.all_people.append(person)
                person.office = randomized_office.name
            else:
                person.office = 'N'
                self.unallocated.append(person)

            if not wants_accomodation or wants_accomodation is 'N':
                person.living_space = 'N'
                self.unallocated.append(person)
                return
            livingspaces_with_space = self.livingspaces_with_space()
            if livingspaces_with_space:
                randomized_livingspace = random.choice(livingspaces_with_space)
                randomized_livingspace.members.append(person)
                person.living_space = randomized_livingspace.name
                if person not in self.all_people:
                    self.all_people.append(person)
            else:
                if person in self.unallocated:
                    return
                else:
                    person.living_space = 'N'
                    self.unallocated.append(person)

        elif role == 'staff':
            person = Staff(name)
            if not offices_with_space:
                person.office = 'N'
                self.unallocated.append(person)
                print('No offices available')
                return

            randomized_office = random.choice(offices_with_space)

            # assign an office to a person
            person.office = randomized_office.name
            # adding a person to the member list in staff
            randomized_office.members.append(person)
            # add staff to all people
            self.all_people.append(person)
        else:
            return 'Invalid Role'

    def is_room_full(self, random_room):
        '''this method checks a room is full'''
        if len(random_room.members) == random_room.capacity:
            return True

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
                    # add person to members of a room
                    check_capacity = self.is_room_full(room)
                    if not check_capacity:
                        room.members.append(person_found)
                        # remove the person from the previous office
                        current_room = person_found.office
                        for room in self.all_rooms:
                            if room.name == current_room:
                                room.members.remove(person_found)
                        # renaming person office
                        person_found.office = room.name

                # check wether  room is a living space
                if isinstance(room, LivingSpace):
                    check_capacity = self.is_room_full(room)
                    if not check_capacity:
                        room.members.append(person_found)
                        current_room = person_found.living_space
                        for room in self.all_rooms:
                            if room.name == current_room:
                                room.members.remove(person_found)
                        person_found.living_space = room.name

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
        if not self.all_rooms:
            print('No Rooms Available')
            return 'No Rooms'

        # go through all rooms in amity
        for room in self.all_rooms:
            text = '\n\t' + room.name + '\n' + '-' * 50
            print text
            # go through each member in a room
            for member in room.members:
                print '\t' + member.name
            if filename:
                for room in self.all_rooms:
                    for member in room.members:
                        with open(filename, 'a') as allocated_people:
                            allocated_people.write(member.name)
        return 'Printed'

    def print_un_allocated(self, filename):
        '''this fuction prints a list of all fellows without living spaces'''
        if not self.all_rooms:
            print('No Rooms Available')
            return 'No Rooms'

        for person in self.unallocated:
            if isinstance(person, Staff):
                print(person.name + '\t\t' + 'Office')
            elif isinstance(person, Fellow):
                if person.office is 'N' and person.living_space is 'N':
                    print(person.name + '\t\t' + 'Office, Livingspace')
                elif person.office is 'N' and person.living_space is not 'N':
                    print(person.name + '\t\t' + 'Office')
                elif person.office is not 'N' and person.living_space is 'N':
                    print(person.name + '\t\t' + 'Livingspace')
        if filename:
            for person in self.unallocated:
                with open(filename, 'a') as unallocated:
                    if isinstance(person, Staff):
                        unallocated.write(
                            person.name + '\t\t' + 'Office')
                    elif isinstance(person, Fellow):
                        if person.office is 'N' and person.living_space is 'N':
                            unallocated.write(
                                person.name + '\t\t' + 'Office, Livingspace')
                        elif person.office is 'N' and \
                                person.living_space is not 'N':
                            unallocated.write(
                                person.name + '\t\t' + 'Office')
                        elif person.office is not 'N' and \
                                person.living_space is 'N':
                            unallocated.write(
                                person.name + '\t\t' + 'Livingspace')
        return 'Printed'

    def print_room(self, room_name):
        '''this function prints the members of a given room'''
        rooms = self.all_rooms
        print room_name + '\n' + '-' * 40
        for room in rooms:
            if room_name == room.name:
                for member in room.members:
                    print member.name
        return 'members have been printed'

    def save_state(self, db_name='amity_db'):
        '''This methods saves informatin from
        the application to the database'''

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
                    fellow.office = person.office
                if person.living_space is None:
                    fellow.living_space = "no room"
                else:
                    fellow.living_space = person.living_space

                session.add(fellow)
                session.commit()

            # condition for a Staff object
            elif isinstance(person, Staff):
                staff = Mtu()
                # put data to columns
                staff.name = person.name
                staff.role = 'Staff'

                staff.office = person.office

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
            self.all_rooms.append(office_object)

        for hostel in livingspaces:
            hostel_name = hostel.name
            hostel_object = LivingSpace(hostel_name)
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
                self.all_people.append(person_object)
            elif role == 'Fellow':
                person_object = Fellow(full_name)
                self.all_people.append(person_object)
