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

    def add_person(self, name, role, wants_accomodation=N):
        if role == 'Staff':
            person = Staff(name)
            self.staff.append(person)
            self.all_people.append(person)
        elif role == 'Fellow':
            person = Fellow(name, wants_accomodation)
            self.fellows.append(person)
            self.all_people.append(person)

         # the indexes of the office list randomized
        randomized_offices_list = random.shuffle(self.office_rooms)
        last_room_index = len(randomized_offices_list - 1)
        room_index = 0
        while(room_index <= last_room_index):

            if not randomized_offices_list[room_index].is_full:
                randomized_offices_list[room_index].append(person)
                break
            else:
                room_index += 1

            if room_index == last_room_index and randomized_offices_list[last_room_index].is_full:
                self.all_unallocated_people.append(person)
                return 'all rooms are full '


               

        # now getting the office and adding a person to the member list
