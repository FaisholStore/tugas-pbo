from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# setting koneksi ke database
engine = create_engine('sqlite:///example.db')

# membuat tabel
Base = declarative_base()
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

Base.metadata.create_all(engine)

# membuat session
Session = sessionmaker(bind=engine)
session = Session()

# menambahkan data ke tabel
user = User(name="John Doe", age=30)
session.add(user)
session.commit()

# mengambil data dari tabel
users = session.query(User).all()
for user in users:
    print(user.name, user.age)
