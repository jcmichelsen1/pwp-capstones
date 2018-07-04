################################################################################
'''
Populate.py tests TomeRater.py an application that stores users, books, and user
reviews.
'''
################################################################################
# created:  06/20/2018, jcm
# revised:  06/21/2018, jcm
# revised:  06/21/2018, jcm
# revised:  07/02/2018, jcm
################################################################################print('Start of populate.py')
print('Begin populate.py')

from TomeRater import *

Tome_Rater = TomeRater()

print('Create users ...')
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu")
Tome_Rater.add_user("David Marr", "david@computation.org")
Tome_Rater.add_user("Jeff Michelsen", "jcmichelsen1@gmail.com")
# Tome_Rater.add_user("JoAnn Michelsen", "joannmichelsen@gmail.com")

print('Create books ...')
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
book2 = Tome_Rater.create_book("Society of 2018", 98765432)
book3 = Tome_Rater.create_book("Society of 1900", 87656321)
book4 = Tome_Rater.create_book("Society of 1800", 87654321)

print('Create fiction books ...')
fiction1 = Tome_Rater.create_fiction("Alice In Wonderland", "Lewis Carroll", 9781536831139)
fiction2 = Tome_Rater.create_fiction("The Diamond Age", "Neal Stephenson", 10101010)
fiction3 = Tome_Rater.create_fiction("There Will Come Soft Rains", "Ray Bradbury", 10001000)
fiction4 = Tome_Rater.create_fiction("There Will Come Hard Rains", "Ray Bradbury", 10001002)

print('Create non-fiction books ...')
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence II", "AI", "advanced", 11111938)
nonfiction3 = Tome_Rater.create_non_fiction("Machines", "Machines", "intermediate", 13111938)
nonfiction4 = Tome_Rater.create_non_fiction("Automobiles", "Automobiles", "beginner", 13111538)

print('Add books to a user with rating ...')
# Tome_Rater.add_book_to_user(book1, 'joannmichelsen@gmail.com', 0)

Tome_Rater.add_book_to_user(nonfiction1, "marvin@mit.edu", 1)
Tome_Rater.add_book_to_user(nonfiction2, "marvin@mit.edu", 1)
Tome_Rater.add_book_to_user(nonfiction3, "marvin@mit.edu", 1)

Tome_Rater.add_book_to_user(book1, "david@computation.org", 2)
Tome_Rater.add_book_to_user(book2, "david@computation.org", 2)
Tome_Rater.add_book_to_user(book3, "david@computation.org", 2)
Tome_Rater.add_book_to_user(fiction1, "david@computation.org", 2)
Tome_Rater.add_book_to_user(fiction2, "david@computation.org", 2)
Tome_Rater.add_book_to_user(fiction3, "david@computation.org", 2)

Tome_Rater.add_book_to_user(book1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(book2, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(book3, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(fiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(fiction2, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(fiction3, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction3, "alan@turing.com", 3)

Tome_Rater.add_book_to_user(book1, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(book2, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(book3, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(book4, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(fiction1, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(fiction2, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(fiction3, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(fiction4, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(nonfiction1, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(nonfiction2, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(nonfiction3, "jcmichelsen1@gmail.com", 4)
Tome_Rater.add_book_to_user(nonfiction4, "jcmichelsen1@gmail.com", 4)

# test invalid user

# Tome_Rater.add_book_to_user(book1, "jmichelsen@aol.com", 5)

print('\nPrint book catalog ... ')
Tome_Rater.print_catalog()

print('\nPrint users ... ')
Tome_Rater.print_users()

print("\nPrint most read book ... " )
print(''),
print(Tome_Rater.most_read_book())

print("\nPrint highest rated book ... ")
print(''),
print(Tome_Rater.highest_rated_book())

print("\nPrint most positive user ... ")
print(''),
print(Tome_Rater.most_positive_user())

print('\nEnd of populate.py')
