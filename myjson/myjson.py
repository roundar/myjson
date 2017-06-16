from json import loads

try:
    from urllib.request import Request, urlopen, HTTPError
except:
    from urllib2 import urlopen, Request, HTTPError

URL = 'https://api.myjson.com/bins/{id}'


class MyjsonNotFoundException(Exception):
    """Raised when no JSON is found at the requested endpoint."""
    def __init__(self, endpoint, *args):
        super(self.__class__, self).__init__("No JSON found at {}".format(endpoint))
        self.endpoint = endpoint


def _get_url_and_id(id_or_url):

    if not id_or_url:
        id = None
    elif id_or_url.startswith(URL.format(id='')):
        id = id_or_url.split('/')[-1]
    else:
        id = id_or_url

    return URL.format(id=id if id else ''), id


def read_url(url):
    try:
        resp = urlopen(url)
    except HTTPError as e:
        if e.code == 404:
            raise MyjsonNotFoundException(url if isinstance(url, str) else url.url())
        else:
            raise e
    return resp.read().decode()


def get(id_or_url, pretty=False):
    """Load json from a myjson endpoint

    :param id_or_url: ID (3-8 alphanumeric characters, e.g., 23ff9) of
        the json OR the full URL (E.g., https://api.myjson.com/bins/23ff9)
    :param pretty: Structure the json string with linebreaks and indents
    :return: JSON string
    :raises:
        :class:`MyjsonNotFoundException` if the endpoint does not exist
    """
    url, id = _get_url_and_id(id_or_url)

    if not id:
        raise ValueError('No mysjon id specified')

    if pretty:
        url += "?pretty"

    return read_url(url)


def store(json, update=None, id_only=False):

    """Update or create a myjson endpoint

    :param json: JSON serialized string to host at mjson.com
    :param update: ID (3-8 alphanumeric characters, e.g., 23ff9) of
        the json OR the full URL (E.g., https://api.myjson.com/bins/23ff9) to update.
    :param id_only: Only return the ID of the updated/created endpoint instead of the full URL.
    :return: The URL of the hosted JSON (or the ID if id_only is specified).
    :raises:
        :class:`MyjsonNotFoundException` if the endpoint is specified and does not exist
    """

    url, id = _get_url_and_id(update)
    request = Request(url, data=json.encode())
    request.add_header('Content-Type', 'application/json')
    request.get_method = lambda: 'PUT' if id else 'POST'

    response = read_url(request)

    if not id:
        url, id = _get_url_and_id(loads(response)['uri'])

    return id if id_only else url
