from urllib.request import urlopen
import json, ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url_base = "https://www.googleapis.com/books/v1/volumes?q="

def normalize_isbn(config):
    config['isbn'] = config['isbn'].replace("-", "").replace("/", "").strip()
    return config

def check_field(book, field):
    return (book[field].replace("http://","https://")) if field in book else ""

def check_field_child(book, field, field_child):
    return (book[field][field_child].replace("http://","https://")) if field in book else ""

def check_isbn(book, isbn):
    if 'industryIdentifiers' in book:

        try:
            return book['industryIdentifiers'][0]['identifier'] == isbn or book['industryIdentifiers'][1]['identifier'] == isbn
        except IndexError:
            return False
    else:
        return False


def getDataGoogleBook(config):

    config = normalize_isbn(config)

    url = url_base+"ISBN<"+config['isbn']+">"
    data_google_book = urlopen(url, context=ctx)

    data = data_google_book.read() if (data_google_book.getcode() == 200) else ""

    response = {
        'data': json.loads(data),
        'status_code': data_google_book.getcode()
        }

    return response


def parserToBook(config, data):

    config = normalize_isbn(config)

    response = {
        'title': '',
        'subtitle':  '',
        'description':'',
        'ISBN':'',
        'previewLink':'',
        'imagen': '',
        'authors':[],
        'categories': [],
    }


    for item in data['items']:

        book = item['volumeInfo']

        if check_isbn(book, config['isbn']):

            response['ISBN'] = config['isbn']
            response['title'] = check_field(book, 'title')
            response['subtitle'] =  check_field(book, 'subtitle')
            response['description'] =  check_field(book, 'description')
            response['previewLink'] = check_field(book, 'previewLink')
            response['imagen'] = check_field_child(book, 'imageLinks', 'thumbnail')

            if 'authors' in book:
                response['authors'] = list(map(str, (book['authors'])))

            if 'categories' in book:
                response['categories'] = list(map(str, (book['categories'])))

            return response

    return response
