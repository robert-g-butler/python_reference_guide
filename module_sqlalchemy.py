
# SOURCE: https://docs.sqlalchemy.org/en/13/orm/tutorial.html

import sqlalchemy
from sqlalchemy import create_engine

sqlalchemy.__version__

# Connecting -----------------------------------------------------------------

engine = create_engine('sqlite:///:memory:', echo=True)
#engine = create_engine('sqlite://sqlalchemy.db')
#engine = create_engine('postgresql://scott:tiger@localhost/test')

# Declare a Mapping ----------------------------------------------------------

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        return f'<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>'

# Create a Schema ------------------------------------------------------------

User.__table__

# Create all tables
Base.metadata.create_all(engine)

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')
ed_user.name
ed_user.nickname
str(ed_user.id)

# Creating a Session ---------------------------------------------------------

from sqlalchemy.orm import sessionmaker

Session = sessionmaker(bind=engine)
# or
Session = sessionmaker()
Session.configure(bind=engine)

session = Session()

# Adding and Updating Objects ------------------------------------------------

ed_user = User(name='ed', fullname='Ed Jones', nickname='edsnickname')

session.add(ed_user)

our_user = session.query(User).filter_by(name='ed').first()
our_user
ed_user is our_user

session.add_all([
    User(name='wendy', fullname='Wendy Williams', nickname='windy'),
    User(name='mary', fullname='Mary Contrary', nickname='mary'),
    User(name='fred', fullname='Fred Flintstone', nickname='freddy')
])

ed_user.nickname = 'eddie'

session.dirty
session.new

session.commit()

ed_user.id

# Rolling Back ---------------------------------------------------------------

















