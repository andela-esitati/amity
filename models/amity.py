from person import Fellow, Staff
from rooms import LivingSpace, Office
import random


class Amity(object):
    '''This class contains all rooms and all people in amity'''

    def __init__(self):
        self.all_rooms = []
        self.office_rooms = []
        self.livingspaces = []
        self.all_vacant_rooms = []
        self.vacant_offices = []
        self.vacant_living_space = []
        self.all_people = []
        self.fellows = []
        self.staff = []
        self.all_allocated_people = []
        self.all_unallocated_people = []
        self.allocated_fellows = []
        self.unallocated_fellows = []


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
       