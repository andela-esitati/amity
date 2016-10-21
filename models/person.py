class Person(object):
    '''This class models a person.Fellow and staff inherit from it '''

    def __init__(self, name):
        self.name = name
        self.employer_id = id(self)
        self.office = None

    def __repr(self):
        return '<Person %s>' % self.name


class Staff(Person):

    def __init__(self, name):
        super(Staff, self).__init__(name)
        self.employer_id = id(self)

    def __repr__(self):
        return '<Staff %s>' % self.name


class Fellow(Person):

    def __init__(self, name, wants_accomodation='N'):
        super(Fellow, self).__init__(name)
        self.employer_id = id(self)
        self.wants_accomodation = wants_accomodation
        self.hostel = 'None'

    def __repr__(self):
        return '<Fellow %s>' % self.name
