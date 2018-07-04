# -*- coding: cp1252 -*-
################################################################################
'''
TomeRater is an application that stores users, books, and user reviews.

In this capstone, you will create an application called TomeRater that
allows users to read and rate books.  The purpose of this capstone is to practice
implementing and testing classes in Python. You will be given specifications for
methods for five different classes that interact with each other. To create these
methods you will use your knowledge of lists, loops, dictionaries, strings,
control flow, and of course, basic Python syntax.
'''
################################################################################
# created:  06/20/2018, jcm
# revised:  06/21/2018, jcm
# revised:  06/21/2018, jcm
# revised:  07/02/2018, jcm
################################################################################

class User(object):
    
    ''' User class to keep track of users '''

    # print('User class definition')
    
    def __init__(self, name, email):

        ''' will map a Book object to a user’s rating of the book '''

        # print('User class init function')
        self.name  = name  # string
        self.email = email # string
        self.books = {}    # dictionary

    def get_email(self):
        
        ''' will return the e-mail associated with the user '''

        # print('User class get email function')
        return self.email

    def change_email(self, address):

        ''' will update the e-mail address associated with the user '''

        # print('User class change email function')
        self.email = address
        return 'User' + self.name + ' has email address ' + self.email

    def __repr__(self):

        ''' will print out the user object '''

        # print('User class print user object function')
        return self.name + ', email: ' + self.email + ', books read: ' + str(len(self.books))

    def __eq__(self, other_user):

        ''' function to check user names and e-mail addresses '''

        # print('User class check user name function')
        if self.name == other_user.name and self.email == other_user.email:
          return True
        else:
          return False

    def read_book(self, book, rating=None):

        ''' function to add key:value pair to self.books (book:rating) '''

        # print('User class read book function')
        if rating == 'None':
          rating = 0
        self.books[book] = rating

    def get_average_rating(self):

        ''' function to add key:value pair to self.books (book:rating) '''

        # print('User class get average rating user function')
        avg = 0
        books_rated = 0
        for value in self.books.values():
          if value:
            avg = avg + value
            books_rated = books_rated + 1
            # print(value)
        if books_rated == 0:
          print('No books rated for user' )
        else: 
          avg = avg/books_rated
        return avg
        
class Book(object):
    
    ''' Book class to keep track of books '''

    # print('Book class definition')
    
    def __init__(self, title, isbn):

        ''' will map a Book object '''

        # print('Book class init function')
        self.title   = title # string
        self.isbn    = isbn  # string
        self.ratings = []    # list

    def get_title(self):

        ''' function to return title of book '''

        # print('Book class get title function')
        return self.title

    def get_isbn(self):

        ''' function to return isbn of book '''

        # print('Book class get ISBN function')
        return self.isbn

    def set_isbn(self, isbn):

        ''' function to set isbn of book '''

        # print('Book class set ISBN function')
        self.isbn = isbn
        return 'The ISBN of Book ' + self.title + ' is: ' + str(self.isbn)

    def add_rating(self, rating):

        ''' function to add rating to a book '''

        # print('Book class add rating function')
        if rating >= 0 and rating <= 4:
          self.ratings.append(rating)
          print(' Rating added')
        else:
          print(' Invalid Rating')

    def __eq__(self, book, isbn):

        ''' function to check book title and ISBN '''

        # print('Book class check book title and ISBN function')
        if self.title == other_book.title and self.isbn == other_book.isbn:
          return True
        else:
          return False

    def get_average_rating(self):

        ''' function to calculate average rating '''

        # print('Book class get average rating book function')
        avg = 0
        for rating in self.ratings:
          avg += rating
        avg = avg/len(self.ratings)
        return avg
        
    def __hash__(self):

        ''' function to deal with Type:Error: unhashable type:'list' '''

        # print('Book class hash function')
        return hash((self.title, self.isbn))

    def __repr__(self):

        ''' function to print title '''

        # print('Book class repr function')
        return self.title

class Fiction(Book):

    ''' fiction class to keep track of fiction books '''

    # print('Fiction class definition')

    def __init__(self, title, author, isbn):

        ''' will map a fiction book object '''

        # print('Fiction Book class init function')
        self.title  = title  # string
        self.isbn   = isbn   # string
        self.author = author # string

        # call parent class with title and ISBN
        Book.__init__(self, title, isbn)

    def get_author(self, title):

        ''' function to return author of book '''

        # print('Fiction class get author function')
        return self.author

    def __repr__(self):

        ''' will print out the fiction book object '''

        # print('Fiction class print fiction book object function')
        return self.title + " by " + self.author
        
class Non_fiction(Book):

    ''' non-fiction class to keep track of non-fiction books '''

    # print('Non-fiction class definition')
    
    def __init__(self, title, subject, level, isbn):

        ''' will map a non-fiction book object '''

        # print('Non-fiction book class init function')
        self.subject = subject # string
        self.level   = level   # string

        # call parent class with title and ISBN
        Book.__init__(self, title, isbn)
    
    def get_subject(self):

        ''' function to return subject of book '''

        # print('Non-fiction class get subject function')
        return self.subject
    
    def get_level(self):

        ''' function to return level of book '''

        # print('Non-fiction class get level function')
        return self.level

    def __repr__(self):

        ''' will print out the non-fiction book object '''

        # print('Non-fiction class print non-fiction book object function')
        return self.title + ", a " + self.level + " manual on " + self.subject

class TomeRater(object):

    ''' application to store users '''

    # print('TomeRater class definition')

    def __init__(self):

      ''' function to initialize dictionaries '''

      # print('TomeRater class init fuction')
      self.users = {} # dictionary user:email
      self.books = {} # dictionary book:users

    def create_book(self, title, isbn):

      ''' function to create book object with title and isbn (book) '''

      # print('TomeRater class create book function')
      print(' Adding book ' + title + ', ' + 'with ISBN ' + str(isbn))
      new_book = Book(title, isbn)
      return new_book

    def create_fiction(self, title, author, isbn):

      ''' function to creat fiction book object with title, author and isbn '''

      # print('TomeRater class create fiction function')
      print(' Adding book ' + title + ', ' + 'with ISBN ' + str(isbn))
      new_book = Fiction(title, author, isbn)
      return new_book

    def create_non_fiction(self, title, subject, level, isbn):

      ''' function to creat non fiction book object with title, subject, level and isbn '''

      # print('TomeRater class create non-fiction function')
      print(' Adding book ' + title + ', ' + 'with ISBN ' + str(isbn))
      new_book = Non_fiction(title, subject, level, isbn)
      return new_book
              
    def add_book_to_user(self, book, email, rating=0):

      ''' function to add books and '''

      # print('TomeRater class add book to user function')
      # get user from self.users with email as the key
      user = self.users.get(email, None)
      # if the users exists
      #    call read_book with book and rating
      #    call add_rating on book with rating
      if user:
        user.read_book(book, rating)
        # if the book exists in self.books
        #   increase the value by 1
        # if the book does not exist in self.books
        #   add the key book with a value of 1
        if book not in self.books:
          self.books[book] = 0
        self.books[book] = self.books[book] + 1
        book.add_rating(rating)
      else:
        # if the user does not exist print ('No user with email {email}')
        print(" No user with email " + email + ' exists')

    def add_user(self, name, email):
        
      ''' add a user '''

      # print('TomeRater class add user function')
      print(' Adding ' + name + ', with e-mail ' + email + ' ...')
      # create a new user from name and email
      new_user = User(name, email)
      self.users[email] = new_user
      # if books are provided it should loop through the list and
      # call add_book_to_user
      # if user_books:
      #   for book in user_books:
      #     self.add_book_to_user(book, email)

    def print_catalog(self):

      ''' will iterate through all of the keys in self.books
          (which are Book objects), and prints them '''

      # print('TomeRater class print catalog function')
      # print(self.books)
      for book in self.books:
        print(''),
        print(book)

    def print_users(self):

      ''' print_users , which iterates through all of the values
          of self.users (which are the User objects), and prints them '''

      # print('TomeRater class print users function')
      # print(self.users)
      for user in self.users.values():
        print(''),
        print(user)

    def most_read_book(self):

      ''' will iterate through all of the books in self.books and
          return the book that has been read the most.
          Remember that the keys of self.books are Books, and the values
          are how many times they’ve been read. '''

      # print('TomeRater class most read book function')
      # max_reads = float("-inf")
      max_reads = 0
      most_read = None
      for book in self.books:
        num_reads = self.books[book]
        if num_reads > max_reads:
          max_reads = num_reads
          most_read = book
      return most_read

    def highest_rated_book(self):

      ''' will iterate through all of the books in self.books and
          return the book that has the highest average rating.
          Remember that the keys of self.books are Books, and you can
          call book.get_average_rating() on a Book object book. '''

      # print('TomeRater class highest rated book function')
      # highest_rating = float("-inf")
      highest_rating = 0
      best_book = None
      for book in self.books:
        avg = book.get_average_rating()
        if avg > highest_rating:
          highest_rating = avg
          best_book = book
      return best_book

    def most_positive_user(self):

      ''' will iterate through all of the users in self.users and
          return the user that has the highest average rating.
          Remember that the values of self.users are Users, and you can
          call user.get_average_rating() on a User object user. '''

      # print('TomeRater class most positive user function')
      # highest_rating = float("-inf")
      highest_rating = 0
      most_positive_user = ''
      for user in self.users.values():
        # print(''),
        # print(user)
        avg = user.get_average_rating()
        if avg > highest_rating:
          highest_rating = avg
          most_positive_user = user
      return most_positive_user
