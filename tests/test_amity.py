import unittest
from  app.amity import Amity
from app.person import Fellow, Staff


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
        self.assertEqual(len(everyone), 2)

    def test_person_is_allocated_a_room(self):
        '''test if a person has been reallocated to a specified room'''
        self.amity.create_room('occulus', 'office')
        self.amity.add_person('rehema', 'fellow')
        person = self.amity.fellows[0]
        roomname = person.office.name
        self.assertEqual(roomname, 'occulus')

    def test_a_room_has_a_person(self):
        '''test a that rooms take in people'''
        self.amity.create_room('cyan', 'office')
        self.amity.add_person('jackie', 'fellow')
        office = self.amity.office_rooms[0]
        person = office.members[0]
        person_name = person.name
        self.assertEqual(person_name, 'jackie')

    def test_a_person_has_been_reallocated(self):
        '''test that a person has been reallocated to a different room'''
        self.amity.create_room('mordor', 'office')
        self.amity.add_person('joshua', 'staff')
        staff = self.amity.staff[0]
        office_name = staff.office.name
        self.assertEqual(office_name, 'mordor')
        self.amity.create_room('winterfell', 'office')
        self.amity.reallocate_person('joshua', 'winterfell')
        new_office_name = staff.office.name
        self.assertEqual(new_office_name, 'winterfell')

    def test_a_person_has_been_removed_from_a_room_after_reallocation(self):
        '''test that a person has been removed from a room after reallocation'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.add_person('rehema', 'fellow')
        office = self.amity.office_rooms[0]
        members = office.members
        self.assertEqual(len(members), 1)
        self.amity.create_room('Occulus', 'office')
        self.amity.reallocate_person('rehema', 'Occulus')
        office = self.amity.office_rooms[0]
        members = office.members
        self.assertEqual(len(members), 0)

    def test_print_allocations_to_terminal(self):
        '''test that allocated people are printed to the terminal'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        self.amity.add_person('sam maina', 'staff')
        self.amity.add_person('tom wilkins', 'fellow')
        self.amity.add_person('valt honks', 'fellow', 'Y')
        self.amity.print_allocations(None)

    def test_print_allocations_file(self):
        '''test that allocated people are printed to a file'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        self.amity.add_person('sam maina', 'staff')
        self.amity.add_person('tom wilkins', 'fellow')
        self.amity.add_person('valt honks', 'fellow', 'Y')
        self.amity.print_allocations('allocations.txt')

    def test_people_without_rooms_are_added_to_unallocated_list(self):
        '''test that people without rooms are added to unallocated list'''
        unallocated = self.amity.unallocated
        self.assertEqual(len(unallocated), 0)
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        self.amity.add_person('sam gaamwa', 'fellow')
        self.amity.add_person('tom wilkins', 'fellow')
        self.amity.add_person('tom shitonde', 'fellow', 'Y')
        self.amity.print_un_allocated(None)
        unallocated = self.amity.unallocated
        self.assertEqual(len(unallocated), 2)

    def test_print_unallocated_people_to_terminal(self):
        '''test that unallocated people are printed to a the terminal'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        self.amity.add_person('sam maina', 'staff')
        self.amity.add_person('tom wilkins', 'fellow')
        self.amity.add_person('valt honks', 'fellow', 'Y')
        self.amity.print_un_allocated(None)

    def test_print_unallocated_people_to_a_file(self):
        '''test that unallocated people are printed to a file'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        self.amity.add_person('sam maina', 'staff')
        self.amity.add_person('tom wilkins', 'fellow')
        self.amity.add_person('valt honks', 'fellow', 'Y')
        self.amity.print_un_allocated('unallocated.txt')

    def test_members_of_a_room_are_printed(self):
        '''test that members of a room are printed'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        self.amity.add_person('sam gaamwa', 'fellow')
        self.amity.add_person('sam maina', 'staff')
        self.amity.add_person('tom wilkins', 'fellow')
        self.amity.print_room('hogwarts')

    def test_people_are_added_to_allocated_(self):
        '''test that alloacted people are added to a list'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        allocated = self.amity.allocated
        self.assertEqual(len(allocated), 0)
        self.amity.add_person('sam gaamwa', 'fellow')
        self.amity.add_person('sam maina', 'staff')
        self.amity.add_person('tom wilkins', 'fellow')
        self.amity.print_allocations(None)
        self.assertEqual(len(allocated), 3)

    def test_fellow_are_allocated_to_allocated_list(self):
        '''test that an allocated staff is added to allocated list'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        self.amity.add_person('sam maina', 'fellow')
        self.amity.print_allocations(None)
        allocated = self.amity.allocated
        fellow = allocated[0]
        self.assertIsInstance(fellow, Fellow)

    def test_fellow_are_allocated_to_unallocated_list(self):
        '''test that the person in an unallocated list is a fellow'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        self.amity.add_person('sam maina', 'fellow')
        self.amity.print_un_allocated(None)
        unallocated = self.amity.unallocated
        fellow = unallocated[0]
        self.assertIsInstance(fellow, Fellow)

    def test_unalloacted_people_are_added_to_unallocated_list(self):
        '''test that fellows without living space are added to a list'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        unallocated = self.amity.unallocated
        self.assertEqual(len(unallocated), 0)
        self.amity.add_person('sam gaamwa', 'fellow')
        self.amity.add_person('sam maina', 'staff')
        self.amity.add_person('tom wilkins', 'fellow')
        self.amity.print_un_allocated(None)
        self.assertEqual(len(unallocated), 2)

    def test_load_people_from_file(self):
        '''test that people are added from a list and given a room'''
        self.amity.create_room('hogwarts', 'office')
        self.amity.create_room('php', 'livingspace')
        staff_list = self.amity.staff
        fellows_list = self.amity.fellows
        self.assertEqual(len(staff_list), 0)
        self.assertEqual(len(fellows_list), 0)
        self.amity.load_people("test_people.txt")
        self.assertEqual(len(staff_list), 3)
        self.assertEqual(len(fellows_list), 4)
