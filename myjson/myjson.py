import re
import json
from urllib.request import Request, urlopen, HTTPError

URL = 'https://api.myjson.com/bins/{id}'

valid_id = re.compile("[a-zA-Z0-9]+")


class MyjsonNotFoundException(Exception):
    """Raised when no JSON is found at the requested endpoint."""
    def __init__(self, endpoint, *args):
        super().__init__("No JSON found at {}".format(endpoint))
        self.endpoint = endpoint


def _get_url(id_or_url):

    if not id_or_url:
        return URL.format(id='')

    if id_or_url.startswith('https://api.myjson.com/bins/'):
        id = id_or_url.split('/')[-1]
    else:
        id = id_or_url

    return URL.format(id=id)


def load(id_or_url, **kwargs):
    """Load json from a myjson endpoint

    :param id_or_url: ID (3-8 alphanumeric characters, e.g., 23ff9) of
        the json OR the full URL (E.g., https://api.myjson.com/bins/23ff9)
    :param kwargs: additional arguments (identical to json.loads)
    :return: The JSON object found at the requested myjson endpoint
    :raises:
        :class:`MyjsonNotFoundException` if the endpoint does not exist
    """
    url = _get_url(id_or_url)

    try:
        resp = urlopen(url)
    except HTTPError as e:
        if e.code == 404:
            raise MyjsonNotFoundException(url) from None
        else:
            raise e

    return json.loads(resp.read().decode(), **kwargs)


def dump(obj, id=None, id_only=False, **kwargs):
    """Update or create a myjson endpoint

    :param obj:
    :param id: ID (3-8 alphanumeric characters, e.g., 23ff9) of
        the json OR the full URL (E.g., https://api.myjson.com/bins/23ff9)
    :param id_only: Only return the ID of the updated/created endpoint instead of the full URL
    :param kwargs: Any remaining arguments found in json.dumps
    :return: The URL of the hosted JSON (or the ID if id_only is specified)
    :raises:
        :class:`MyjsonNotFoundException` if the endpoint is specified and does not exist
    """
    url = _get_url(id)
    request = Request(url, data=json.dumps(obj, **kwargs).encode())
    request.add_header('Content-Type', 'application/json')
    request.get_method = lambda: 'PUT' if id else 'POST'

    try:
        resp = urlopen(request)
    except HTTPError as e:
        if e.code == 404:
            raise MyjsonNotFoundException(url) from None
        else:
            raise e

    uri = json.loads(resp.read().decode())['uri']
    return uri.split('/')[-1] if id_only else uri