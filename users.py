import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DB_PATH = "sqlite:///sochi_athletes.sqlite3"
Base = declarative_base()

class User(Base):
	__tablename__ = 'user'
	id = sa.Column(sa.Integer, primary_key=True)
	first_name = sa.Column(sa.Text)
	last_name = sa.Column(sa.Text)
	gender = sa.Column(sa.Text)
	email = sa.Column(sa.Text)
	birthdate = sa.Column(sa.Text)
	height = sa.Column(sa.Float)

engine = sa.create_engine(DB_PATH)
Base.metadata.create_all(engine)
Sessions = sessionmaker(engine)
session = Sessions()

def request_data():
	print("Привет! Я запишу твои данные!")
	first_name = input("Введите своё имя: ")
	last_name = input("А теперь фамилию: ")
	gender = input("Укажите свой пол: ")
	email = input("Мне еще понадобится адрес твоей электронной почты: ")
	birthdate = input("Так же укажите свой день рождения: ")
	height = input("И желательно свой рост: ")
	user = User(
		first_name=first_name,
		last_name=last_name,
		gender=gender,
		email=email,
		birthdate=birthdate,
		height=float(height)
		)
	return user
	
def main():
	user = request_data()
	session.add(user)
	session.commit()
	print("Спасибо, данные сохранены!")

if __name__ == "__main__":
	main()

