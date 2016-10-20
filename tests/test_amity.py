import unittest
from models.amity import Amity


class TestAmity(unittest.TestCase): 
    def setUp(self):
        self.amity = Amity()

    def test_create_room(self):
        rooms = self.amity.all_rooms
        self.assertEqual(len(rooms), 0)
        self.amity.create_room('valhalla', 'office')
        self.assertEqual(len(rooms), 1)
