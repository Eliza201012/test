# class Instagram:
# 	def __init__(self, name, reels, stories, friends):
# 		self.name = name
# 		self.reels = reels
# 		self.stories = stories
# 		self.friends = friends
	
# 	def print_name(self):
# 		print(f"Ви зайшли на сторінку {self.name}")
	
# 	def saw_reels(self):
# 		print(f"Ви подивилися {self.reels} reels")

# 	def saw_stories(self):
# 		if self.stories >= 5:
# 			print("Сторіси закінчилися")
# 		else:
# 			self.stories += 1

# 	def saw_all_stories(self):
# 		print(self.stories)
	
# 	def add_friends(self):
# 		self.friends += 1
	
# 	def print_all_friends(self):
# 		print(self.friends)


# social_media = Instagram(name="formula1", reels=6, stories=3, friends=2)
# social_media.print_name()
# social_media.saw_reels()
# social_media.saw_stories()
# social_media.saw_all_stories()
# social_media.add_friends()
# social_media.print_all_friends()















# class BankAccount:
# 	def __init__(self, owner, balance):
# 		self.owner = owner
# 		self.balance = balance

# 	def deposit(self, amount):
# 		self.balance += amount
# 		return self.balance
	
# 	def withdraw(self, amount):
# 		if self.balance < amount:
# 			message = "Недостатньо коштів"
# 			print(message)
# 			return message
# 		else:
# 			self.balance -= amount
# 			return self.balance
	
# 	def print_account(self):
# 		print(self.balance)
		

# account = BankAccount(owner="Ivan", balance=1000)
# account.deposit(amount=500)
# account.print_account()
# account.withdraw(amount=300)
# account.print_account()
# account.withdraw(amount=5000)













# class Website:
# 	def __init__(self, user_name, password, friends):
# 		self.user_name = user_name
# 		self.password = password
# 		self.friends = []

# 	def create_user(self, user):
# 		if self.user_name not in user:
# 			user = {self.user_name : self.password}
# 			return user
# 		else:
# 			print("Такий користувач вже існує")
	
# 	def check_user_name(self, name):
# 		bad_words = ["Damn", "Shit", "Bullshit"]
# 		for i in bad_words:
# 			if i == name:
# 				print("Shibal")
# 			else:
# 				print("Ok")

# 	def check_password(self, pas):
# 		if len(pas) >= 8:
# 			print("Ok")
# 		else:
# 			print("Не окей")

# 	def add_friend(self):
# 		friend = input("Enter friend: ")
# 		if friend not in self.friends:
# 			self.friends.append(friend)
# 			return self.friends
# 		else:
# 			print("Такий друг вже існує")

# 	def print_info(self):
# 		print(self.user_name, self.password, self.friends)


# create_website = Website(user_name="Book", password="hello world", friends=[])

# create_website.create_user(user="Book")
# create_website.check_user_name(name="Shit")
# create_website.check_password(pas="Book")
# create_website.add_friend()
# create_website.print_info()









# class Shape:
# 	def __init__(self, side_a, side_b):
# 		self.side_a = side_a
# 		self.side_b = side_b
	
# 	def area(self):
# 		return self.side_a, self.side_b
	
# 	def perimeter(self):
# 		return self.side_a, self.side_b


# class Rectangle(Shape):
# 	def __init__(self, side_a, side_b):
# 		super().__init__(side_a, side_b)

# 	def area(self):
# 		return self.side_a * self.side_b
	
# 	def perimeter(self):
# 		return (self.side_a + self.side_b) * 2
	
# my_rectangle = Rectangle(side_a=4, side_b=8)
# print(my_rectangle.area())
# print(my_rectangle.perimeter())


# class Triangle(Shape):
# 	def __init__(self, side_a, side_b, side_c):
# 		self.side_a = side_a
# 		self.side_b = side_b
# 		self.side_c = side_c

# 	def area(self):
# 		return self.side_a + self.side_b + self.side_c
	
# 	def perimeter(self):
# 		return self.side_a + self.side_c

# my_rectangle = Triangle(side_a=3, side_b=6, side_c=1)
# print(my_rectangle.area())
# print(my_rectangle.perimeter())










# class Zoo:
# 	def __init__(self):
# 		self.__animals = []

# 	def add_animal(self, animal):
# 		self.__animals.append(animal)
# 		return self.__animals

# 	def show_all_animals(self):
# 		print(self.__animals)


# class Animal(Zoo):
# 	def __init__(self, name, age):
# 		super().__init__()
# 		self.__name = name
# 		self.__age = age

# 	def get_name(self):
# 		return self.__name
	
# 	def set_name(self, new_name):
# 		a = self.__name = new_name
# 		return a

# 	def make_sound(self):
# 		pass

# 	def info(self):
# 		return self.__name and self.__age
	

# class Lion(Animal):
# 	def make_sound(self):
# 		return "Ррррр!"
	
# class Parrot(Animal):
# 	def make_sound(self):
# 		return "Чирік-чирік!"

# class Fish(Animal):
# 	def make_sound(self):
# 		return "Буль-буль!"



# make_zoo = Zoo()
# print(make_zoo.add_animal(animal=Parrot))
# print(make_zoo.show_all_animals())

# create_animal = Animal(name="Григорій", age=34)
# print(create_animal.get_name())
# create_animal.set_name(new_name="Dmytro")
# print(create_animal.info())







# class Book:
# 	def __init__(self, title, author, year, is_available):
# 		self.__title = title
# 		self.__author = author
# 		self.__year = year
# 		self.__is_available = is_available

# 	def get_title(self):
# 		return self.__title
	
# 	def get_author(self):
# 		return self.__author
	
# 	def get_year(self):
# 		return self.__year
	
# 	def get_is_available(self):
# 		return self.__is_available
	
# 	def set_title(self, title):
# 		if title:
# 			self.__title = title
# 		else:
# 			print("Назва не може бути порожньою")

# 	def set_author(self, author):
# 		if author:
# 			self.__author = author
# 		else:
# 			print("Ви не ввели автора!")

# 	def set_year(self, year):
# 		if year > 0:
# 			self.__year = year
# 		else:
# 			print("Рік не може бути від'ємним!")
	
# 	def set_is_available(self, status):
# 		if status:
# 			self.__is_available = status
# 		else:
# 			print("Статус не може бути порожнім")

	
# 	def borrow(self):
# 		if self.__is_available == "Yes":
# 			self.__is_available = "No"
# 		else:
# 			print("Книга вже зайнята")

# 	def return_book(self):
# 		if self.__is_available == "No":
# 			self.__is_available = "Yes"
# 		else:
# 			print("Книга зайнята")
	
# 	def info(self):
# 		print(f"'Назва': {self.__title}, 'Автор': {self.__author}, 'Рік': {self.__year}, 'Статус': {self.__is_available}")


# class Library:
# 	def __init__(self):
# 		self.__books = []
# 		self.borrow = Book(title="Alice's Adventures in Wonderland", author="Lewis Carroll", year=1865, is_available="Yes")

# 	def add_book(self, title):
# 		self.__books.append(title)
# 		print("Книгу додано")
	
# 	def show_books(self):
# 		if self.__books:
# 			for title in self.__books:
# 				return title.info()
# 		else:
# 			print("Бібліотека порожня")
		
# 	def find_book_by_title(self, title):
# 		for book in self.__books:
# 			if book.get_title() == title:
# 				return book
# 			else:
# 				print("Книгу не знайдено")
# 				return None

# 	def borrow_book(self, title):
# 		book = self.find_book_by_title(title)
# 		if book:
# 			book.borrow()
		
# 	def return_book(self, title):
# 		book = self.find_book_by_title(title)
# 		if book:
# 			book.return_book()


# library = Library()
# book = book = Book(title="Alice's Adventures in Wonderland", author="Lewis Carroll", year=1865, is_available="Yes")

# library.add_book(book)
# library.show_books()

# library.borrow_book(title="Alice's Adventures in Wonderland")
# library.show_books()

# library.return_book(title="Alice's Adventures in Wonderland")
# library.show_books()














class Room:
	def __init__(self, number, capacity, is_booked):
		self.__number = number
		self.__capacity = capacity
		self.__is_booked = is_booked

	def get_capacity(self):
		return self.__capacity

	def book(self):
		if self.__is_booked == "No":
			self.__is_booked = "Yes"
			print("Кімната заброньована")
		else:
			print("Кімната вже заброньована")

	def free(self):
		if self.__is_booked == "Yes":
			self.__is_booked = "No"
			print("Гарної дороги")
		else:
			print("Error")

	def get_info(self):
		print(f"'Кімната №': {self.__number}, 'Місць': {self.__capacity}, 'Заброньована': {self.__is_booked}")

	def __str__(self):
		 return f"'Кімната №': {self.__number}, 'Місць': {self.__capacity}, 'Заброньована': {self.__is_booked}"


class Hotel:
	def __init__(self):
		self.__rooms = []

	def add_room(self, room):
		if room not in self.__rooms:
			self.__rooms.append(room)
			print("Кімната додана")
		else:
			print("Така кімната вже існує")
	
	def show_rooms(self):
		for room in self.__rooms:
			return room.get_info()
		
	def find_available_room(self, capacity):
		for room in self.__rooms:
			if room.get_capacity() == capacity:
				return room
			else:
				print("Такої кімнати не існує")



room1 = Room(number=203, capacity=6, is_booked="Yes")
room2 = Room(number=302, capacity=2, is_booked="No")

hotel = Hotel()
hotel.add_room(room1)
hotel.add_room(room2)

room2.book()
room1.free()
hotel.show_rooms()

print("Your room")
availible_room = hotel.find_available_room(capacity=6)
if availible_room:
	print(availible_room)