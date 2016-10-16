class Room(object):
    '''
    Creates a Person object. Classes Fellow and Staff inherit from it.
    '''

    def __init__(self, name):
        self.occupants = []
        self.name = name

    def __repr__(self):
        return '<Room %s >' % self.name

    @property
    def room_type(self):
        return self.__class__.__name__


class Office(Room):

    capacity = 6

    def __init__(self, name):
        super(Office, self).__init__(name)

        def __repr__(self):
            return '<Office %s >' % self.name


class LivingSpace(Room):

    capacity = 4

    def __init__(self, name):
        super(LivingSpace, self).__init__(name)

    def __repr__(self):
        return '<LivingSpace %s >' % self.name
