import json
import re
import sys
from urllib.request import Request, urlopen, HTTPError

URL = 'https://api.myjson.com/bins/{id}'

valid_id = re.compile("[a-zA-Z0-9]{3,8}")


class MyjsonException(Exception):
    pass


def _get_id(url):
    if not url.startswith('https://api.myjson.com/bins/'):
        raise MyjsonException("Invalid url: {}".format(url))
    return url.split('/')[-1]


def _get_url(id):
    # Forgive including url in place of an ID
    if id.startswith('https://api.myjson.com/bins/'):
        id = id.split('/')[-1]

    if not valid_id.match(id):
        raise MyjsonException("Invalid ID: {} (Must be 2-8 alphanumeric characters)".format(id))

    return URL.format(id=id)


def get(id):
    """ Return the json object from associated with this ID (also accepts a full URL)"""
    u = _get_url(id)
    try:
        resp = urlopen(u)
    except HTTPError as e:
        if e.code == 404:
            raise MyjsonException("{} does not exist.".format(u)) from None
        else:
            raise e
    return json.loads(resp.read().decode())


def create(jsonable=None, file=None, id_only=False):
    """Host a new json endpoint"""

    if jsonable is None and file is None:
        raise MyjsonException("Create requires a json-able object or a file as input.")

    if jsonable and file:
        raise MyjsonException("Specify a json-able object OR a file as input to store json.")

    if file:
        with open(file, 'r') as f:
            jsonable = json.load(f)

    request = Request(URL.format(id=''), data=json.dumps(jsonable).encode())
    request.add_header('Content-Type', 'application/json')
    uri = json.loads(urlopen(request).read().decode())['uri']
    return uri.split('/')[-1] if id_only else uri


def update(id, jsonable=None, file=None):
    """Update an existing json endpoint"""

    if jsonable is None and file is None:
        raise MyjsonException("Update requires a json-able object or a file as input.")

    if jsonable and file:
        raise MyjsonException("Specify a json-able object OR a file as input for an update.")

    if file:
        with open(file, 'r') as f:
            jsonable = json.load(f)

    u = _get_url(id)
    request = Request(u, data=json.dumps(jsonable).encode())
    request.add_header('Content-Type', 'application/json')
    request.get_method = lambda: 'PUT'

    try:
        urlopen(request)
    except HTTPError as e:
        if e.code == 404:
            raise MyjsonException("{} does not exist to update.".format(u)) from None
        else:
            raise e

    return "{} successfully updated".format(u)