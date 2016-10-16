from rooms import Office, LivingSpace


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
        self.unallocated_staff = []
