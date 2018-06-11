from django.test import TestCase
from feeds.views import getDataGoogleBook, parserToBook

import json

# Create your tests here.
class FeedsTest(TestCase):

    def test_connection(self):
        #given
        #act
        response = getDataGoogleBook({'isbn': ""})

        #assert
        self.assertEqual(200, response['status_code'])


    def test_get_data_empty(self):
        #given
        query  = {'isbn': ""}
        response = getDataGoogleBook(query)
        #when
        result = parserToBook(query, response['data'])

        #then
        self.assertEqual(200, response['status_code'])
        self.assertEqual(result, {
            'title': '',
            'subtitle':  '',
            'description':'',
            'ISBN':'',
            'previewLink':'',
            'imagen': '',
            'authors':[],
            'categories': [],
        })

    def test_get_data_isbn(self):
        #given
        query  = {'isbn': "9788474324198"}

        data = ''

        with open('feeds/data/example1.json') as data_file:
            data = json.load(data_file)

        #when
        result = parserToBook(query, data)

        #then
        self.assertEqual(result['title'], 'De cuerpo presente')
        self.assertEqual(result['subtitle'], 'las ciencias cognitivas y la experiencia humana')
        self.assertEqual(result['description'], '')
        self.assertEqual(result['ISBN'], '9788474324198')
        self.assertEqual(result['previewLink'], 'https://books.google.cl/books?id=fTJJcAAACAAJ&dq=ISBN%3C9788474324198%3E&hl=&cd=1&source=gbs_api')
        self.assertEqual(result['imagen'], 'https://books.google.com/books/content?id=fTJJcAAACAAJ&printsec=frontcover&img=1&zoom=1&source=gbs_api')
        self.assertEqual(result['authors'], ["Francisco J. Varela","Evan Thompson","Eleanor Rosch"])
        self.assertEqual(result['categories'], ["Philosophy"])


    def test_get_multiples_isbn(self):

        list_ISBN = [
                    {'ISBN' : "978-847-432-419-8",'ISBN_test' : "9788474324198",  'file': 'example1', 'title': "De cuerpo presente"},
                    {'ISBN' : " 9789569725005 ",'ISBN_test' : "9789569725005",  'file': 'example2', 'title': "El tranco del pueblo"},
                    {'ISBN' : " 9-789-562-823-463",'ISBN_test' : "9789562823463",  'file': 'example3', 'title': "Dialectos en transición"},
                    {'ISBN' : "9562821536",'ISBN_test' : "9562821536",     'file': 'example4', 'title': "Autonomía, espacio y gestión"},
                    {'ISBN' : "9789568410391",'ISBN_test' : "9789568410391",  'file': 'example5', 'title': "Conversaciones con Carlos Altamirano"},
                    {'ISBN' : "9684270682",'ISBN_test' : "",     'file': 'example6', 'title': ""},
                    {'ISBN' : "9789568410711",'ISBN_test' : "9789568410711",  'file': 'example7', 'title': "El país que soñamos"}
                ]
        for item in list_ISBN:
            #given
            query  = {'isbn': item['ISBN']}
            data = ''

            with open(('feeds/data/%s.json'% (item['file']))) as data_file:
                data = json.load(data_file)

            #when
            result = parserToBook(query,data)

            #then
            self.assertEqual(result['ISBN'], item['ISBN_test'])
            self.assertEqual(result['title'], item['title'])
