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

    


