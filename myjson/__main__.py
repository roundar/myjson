import argparse

from . import get, store


def main():

    parser = argparse.ArgumentParser(
        prog='myjson', description='A python commandline utility for working with https://myjson.com/')

    subs = parser.add_subparsers(help="mjson commands")

    get_parser = subs.add_parser('get')
    get_parser.add_argument('id_or_url', help="The id or url to get")
    get_parser.add_argument('--compact', action='store_true', help="Condense output by removing extra whitespace.")
    get_parser.set_defaults(func=lambda args: get(args.id_or_url, not args.compact))

    store_parser = subs.add_parser('store')
    store_parser.add_argument('--update', metavar='id_or_url',
                              help="Update the given id or url instead of creating a new store")
    store_parser.add_argument('--id-only', action='store_true',
                              help="Only return the id's of the endpoints instead of the full urls.")
    store_parser.add_argument('json', nargs='?', type=argparse.FileType('r'), default='-',
                              help="File to read json from (defaults to stdin if no file is specified).")
    store_parser.set_defaults(func=lambda args: store(args.json.read(), args.update, args.id_only))

    args = parser.parse_args()

    try:
        print(args.func(args))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()