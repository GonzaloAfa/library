from django.test import TestCase, Client
from models import Book

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
        self.assertIn("list books", response.content)
        

    def test_empty(self):
        #given
        #when
        book = Book()
        #then
        self.assertEqual(book.title, '')
        self.assertEqual(book.author, None)
        self.assertEqual(book.publisher, None)
        self.assertEqual(book.ISBN, '')
        self.assertEqual(book.abstract, '')

    def test_add_book(self):
        #given
        book = Book()

        #when
        book.title = "What's up?"
        book.author = "Gonzalo"
        book.publisher = "Palito"
        book.ISBN = "123123123123"
        book.abstract = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vehicula est accumsan, ultricies nulla at, varius nisi. Pellentesque tempus pretium massa. Aliquam tempor sodales metus vitae rutrum. Morbi eget rhoncus odio. Sed bibendum porttitor mattis. Vestibulum molestie commodo blandit. Donec fringilla ante id risus rhoncus laoreet ac in velit."
        book.save()


        #then
        all_books = Book.objects.all()
        self.assertEqual(len(all_books), 1)
        
        book_db = all_books[0]
        self.assertEqual(book_db, book)

        self.assertEqual(book_db.title, "What's up?")
        self.assertEqual(book_db.author, "Gonzalo")
        self.assertEqual(book_db.publisher, "Palito")
        self.assertEqual(book_db.ISBN, "123123123123")
        self.assertEqual(book_db.abstract, "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vehicula est accumsan, ultricies nulla at, varius nisi. Pellentesque tempus pretium massa. Aliquam tempor sodales metus vitae rutrum. Morbi eget rhoncus odio. Sed bibendum porttitor mattis. Vestibulum molestie commodo blandit. Donec fringilla ante id risus rhoncus laoreet ac in velit.")



    def test_add_book_equals_isbn(self):
        #given
        book1 = Book()
        book2 = Book()

        #when
        book1.title = "What's up?"
        book1.author = "Gonzalo"
        book1.publisher = "Palito"
        book1.ISBN = "123123123123"
        book1.abstract = "Lorem ipsum dolor"
        book1.save()

        book2.title = "What's up?"
        book2.author = "Gonzalo"
        book2.publisher = "Palito"
        book2.ISBN = "123123123123"
        book2.abstract = "Lorem ipsum dolor"
        book2.save()

        #then
        books_by_ISBN = Book.objects.filter(ISBN="123123123123")
        self.assertEqual(len(books_by_ISBN), 1)


    def test_add_book_ISBN(self):
        #given
        book = Book()

        #when
        book.title = "What's up?"
        book.author = "Gonzalo"
        book.publisher = "Palito"
        book.ISBN = " 123-123-123-123  "
        book.abstract = "Lorem ipsum dolor sit amet"
        book.save()
        
        
        #then
        book_by_isbn = Book.objects.filter(ISBN = "123123123123")
        self.assertEqual(len(book_by_isbn), 1)
        