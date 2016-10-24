from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine('sqlite:///amity_db')
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Person(Base):
    __tablename__ = 'people'
    person_id = Column(Integer(), primary_key=True)
    name = Column(String(50))
    role = Column(String(50))
    office = Column(String(50))
    living_space = Column(String(50))

    def __repr__(self):
        return 'Person %s role %s' % (self.name, self.role)


class Office(Base):
    __tablename__ = 'offices'
    office_id = Column(Integer, primary_key=True)
    name = Column(String(50), ForeignKey('people.office'))
    person = relationship('Person', backref=backref('offices'))

    def __repr__(self):
        return 'Office %s' % (self.name)


class LivingSpace(Base):
    __tablename__ = 'livingspaces'
    living_space_id = Column(Integer(), primary_key=True)
    name = Column(String(50), ForeignKey('people.living_space'))
    person = relationship('Person', backref=backref('livingspaces'))

    def __repr__(self):
        return 'Livingspace %s' % (self.name)

Base.metadata.create_all(engine)
