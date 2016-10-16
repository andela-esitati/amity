from person import Fellow, Staff
from rooms import LivingSpace, Office


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

# create_room('Ocxulus', 'livingspace')
# create_room({'livingspace': ['A', 'S']})

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
