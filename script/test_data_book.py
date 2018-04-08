
# isbn = "9788474324198"
# isbn = "9789569725005"
# isbn = "9789562823463"
# isbn = "9562821536"
# isbn = "9789568410391"
isbn = "9684270682"

from urllib.request import urlopen
import json, ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://www.googleapis.com/books/v1/volumes?q=ISBN%3C"+isbn+"%3E"
print ("URL: "+url)


response = urlopen(url, context=ctx)
data = json.loads(response.read())


def check_field(book, field):
    return (book[field]) if field in book else ""

def check_field_child(book, field, field_child):
    return (book[field][field_child]) if field in book else ""

def check_isbn(book, isbn):
    return book['industryIdentifiers'][0]['identifier'] == isbn or book['industryIdentifiers'][1]['identifier'] == isbn


for item in data['items']:

    book = item['volumeInfo']

    if check_isbn(book, isbn):

        print ("---------------------------------")
        print ("Titulo    \t: ", check_field(book, 'title') )
        print ("Subtitulo \t: ", check_field(book, 'subtitle'))

        if 'authors' in book:
            print ('Autores   \t: %s' % ', '.join(map(str, (book['authors']))))

        if 'categories' in book:
            print ('Categorias\t: %s' % ', '.join(map(str, (book['categories']))))

        print ("GBook    \t: " + check_field(book, 'previewLink'))

        print ("Imagen   \t: " + check_field_child(book, 'imageLinks', 'thumbnail'))
        print ("---------------------------------")
        print ("\n")
        break
    else:
        print ("not found results")
