from django.test import TestCase, Client
from book.models import Book

# Create your tests here.
class BookTest(TestCase):

    def test_reachable(self):
        #arrange
        client = Client()

        #act
        response = client.get("/books")

        #assert
        self.assertEqual(200, response.status_code)

    def test_book_list(self):
        #arrange
        client = Client()

        #act
        response = client.get("/books")

        #assert
        self.assertIn("list books", str(response.content))


    def test_empty(self):
        #given
        #when
        book = Book()
        #then
        self.assertEqual(book.title, '')
        self.assertEqual(book.ISBN, '')

    def test_add_book(self):
        #given
        book = Book()

        #when
        book.title = "What's up?"
        book.ISBN = "123123123123"
        book.save()

        #then
        all_books = Book.objects.all()
        self.assertEqual(len(all_books), 1)

        book_db = all_books[0]
        self.assertEqual(book_db, book)

        self.assertEqual(book_db.title, "What's up?")
        self.assertEqual(book_db.ISBN, "123123123123")



    def test_add_book_equals_isbn(self):
        #given
        book1 = Book()
        book2 = Book()

        #when
        book1.title = "What's up?"
        book1.ISBN = "123123123123"
        book1.save()

        book2.title = "What's up?"
        book2.ISBN = "123123123123"
        book2.save()

        #then
        books_by_ISBN = Book.objects.filter(ISBN="123123123123")
        self.assertEqual(len(books_by_ISBN), 1)


    def test_add_book_ISBN(self):
        #given
        book = Book()

        #when
        book.title = "What's up?"
        book.ISBN = " 123-123-123-123  "
        book.save()


        #then
        book_by_isbn = Book.objects.filter(ISBN = "123123123123")
        self.assertEqual(len(book_by_isbn), 1)
