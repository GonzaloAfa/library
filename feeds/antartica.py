from urllib import request, parse

import json, ssl
from lxml import html
from .views import normalize_isbn


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def getDataAntartica(config):

    config = normalize_isbn(config)
    url = "https://www.antartica.cl/antartica/servlet/LibroServlet?action=searchLibros"

    params = parse.urlencode({'busqueda': config['isbn']}).encode()
    req =  request.Request(url, data=params)
    response = request.urlopen(req, context=ctx)

    if(response.code == 200):
        id = parserIdSearch(config, response.read())

        if id != "":
            return getDetailsBook(id)


    return {
            'data': "",
            'status_code': response.code
        }


def parserIdSearch(config, data):
    tree = html.fromstring(data)

    url = tree.xpath('//a[contains(@class, "txtTitulosSubCategoria")]/@href')

    if url != []:
        url = url[0]
        return url[url.index("_libro=")+7:]
    else:
        return ""


def getDetailsBook(id):

    url_base = "https://www.antartica.cl/antartica/servlet/LibroServlet?action=fichaLibro&id_libro="
    url = url_base+str(id)

    response = request.urlopen(url, context=ctx)

    return {
        'data': response.read(),
        'status_code': response.code
    }


def parserToBookAntartica(query, data):
    tree = html.fromstring(data)

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

    title = tree.xpath('//span[contains(@class, "txtTitulosRutaSeccionLibros")]/b/text()')
    isbn = tree.xpath('//span[contains(@class, "txt")]/text()')

    author = tree.xpath('//a[contains(@class, "txtTitulosRutaSeccionLibros")]/text()')
    author = [line.strip() for line in author]

    img = tree.xpath('//img[contains(@alt,"'+title[0]+'")]/@src')

    response['title']       = str(title[0]).strip()
    response['ISBN']        = str(isbn[0])[5:].strip()
    # response['previewLink'] = url
    response['imagen']      = str(img[0])
    response['authors']     = [author[0]]

    return response
