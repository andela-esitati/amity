class Room(object):
    '''
    Creates a Person object. Classes Fellow and Staff inherit from it.
    '''

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.members = []
        self.is_not_full = len(self.members) < capacity

    def __repr__(self):
        return '<Room %s >' % self.name


class Office(Room):

    def __init__(self, name):
        super(Office, self).__init__(name, capacity=6)

        def __repr__(self):
            return '<Office %s >' % self.name


class LivingSpace(Room):

    def __init__(self, name):
        super(LivingSpace, self).__init__(name, capacity=4)

    def __repr__(self):
        return '<LivingSpace %s >' % self.name
