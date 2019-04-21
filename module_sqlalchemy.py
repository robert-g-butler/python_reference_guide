
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
        return (f'<User(name={self.name}, '
                f'fullname={self.fullname}, '
                f'nickname={self.nickname})>')

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

# or...
# Session = sessionmaker()
# Session.configure(bind=engine)

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

ed_user.name = 'Edwardo'

fake_user = User(name='fakeuser', fullname='Invalid', nickname='12345')
session.add(fake_user)

session.query(User).filter(User.name.in_(['Edwardo', 'fakeuser'])).all()

session.rollback()

ed_user.name
fake_user in session

session.query(User).filter(User.name.in_(['ed', 'fakeuser'])).all()

# Querying -------------------------------------------------------------------

session.query(User).order_by(User.id)

for instance in session.query(User).order_by(User.id):
    print(instance.name, instance.fullname)

for name, fullname in session.query(User.name, User.fullname):
    print(name, fullname)

for row in session.query(User, User.name).all():
    print(row.User, row.name)

for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)

from sqlalchemy.orm import aliased

user_alias = aliased(User, name='user_alias')
for row in session.query(user_alias, user_alias.name):
    print(row)

for u in session.query(User).order_by(User.id)[1:3]:
    print(u)




