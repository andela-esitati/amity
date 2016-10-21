import unittest
from models.amity import Amity


class TestAmity(unittest.TestCase):
    def setUp(self):
        self.amity = Amity()

    def test_create_room(self):
        '''test to confirm a room has been created'''
        rooms = self.amity.all_rooms
        # making sure the rooms are empty
        self.assertEqual(len(rooms), 0)
        self.amity.create_room('haskel', 'livingspace')
        # checking to see if rooms have been added
        self.assertEqual(len(rooms), 1)

    def test_office_is_created(self):
        '''test to confirm an office is created'''
        office = self.amity.office_rooms
        self.assertEqual(len(office), 0)
        self.amity.create_room('valhalla', 'office')
        self.assertEqual(len(office), 1)

    def test_living_space_is_created(self):
        '''test to confirm that living space is created'''
        livingspace = self.amity.livingspaces
        self.assertEqual(len(livingspace), 0)
        self.amity.create_room('php', 'livingspace')
        self.assertEqual(len(livingspace), 1)

    def test_fellow_is_created(self):
        '''tesst to confirm a fellow is created'''
        self.amity.create_room('valhalla', 'office')
        fellow = self.amity.fellows
        self.assertEqual(len(fellow), 0)
        self.amity.add_person('chironde', 'fellow')
        self.assertEqual(len(fellow), 1)

    def test_staff_is_created(self):
        '''test to confirm staff is created'''
        self.amity.create_room('hogwarts', 'office')
        staff = self.amity.staff
        self.assertEqual(len(staff), 0)
        self.amity.add_person('njira', 'staff')
        self.assertEqual(len(staff), 1)

    def test_people_are_added_to_all_peole_list(self):
        '''test if all people are added to the people list
        regardles wether they are fellows or staff '''
        everyone = self.amity.all_people
        self.assertEqual(len(everyone), 0)
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        self.amity.add_person('njira', 'staff')
        self.amity.add_person('joy', 'fellow', 'Y')
        self.assertEqual(len(everyone),2)

