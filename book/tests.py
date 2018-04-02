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
        

    def test_empty_list(self):
        #given
        #when
        books = Book()
        #then
        self.assertTrue(books.is_empty())
    
    def test_add_task(self):
        #given
        books = Book()
        #when
        #then
    
    def test_list_tasks(self):
        #given
        books = Book()
        #when
        #then

    def test_add_many_tasks(self):
        #given
        books = Book()
        #when
        #then