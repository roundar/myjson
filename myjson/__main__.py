import sys
import argparse
import json

from . import get, update, create


def main():

    parser = argparse.ArgumentParser(
        prog='myjson',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        description='A python commandline utility for working with https://myjson.com/',
    )
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        '--get',
        nargs=1,
        help="Download the json associated with this ID (also accepts full URL)",
        metavar='id'
    )
    group.add_argument(
        '--update',
        nargs=2,
        help="Updates the JSON associated with the given ID (or URL)",
        metavar=('id', 'file')
    )
    group.add_argument(
        '--create',
        nargs='*',
        help='Upload JSON files to myjson',
        metavar='file',
        type=argparse.FileType('r'),
        default=sys.stdin,
    )
    parser.add_argument(
        '--id-only',
        help="Only return the id instead of the full url. (Used with --create)",
        action='store_true'
    )
    parser.add_argument(
        '--compact',
        help='Compact output by removing whitespace. (Used with --get)',
        action='store_true',
    )
    parser.add_argument(
        '--debug',
        help="Extended error output",
        action='store_true'
    )

    args = parser.parse_args()

    try:
        if args.get:
            j = get(args.get[0])
            if args.compact:
                print(json.dumps(j, separators=(',',':')))
            else:
                print(json.dumps(j, indent=4))

        elif args.update:
            with open(args.update[1]) as file:
                print(update(args.update[0], file=file))

        elif args.create:
            [print(create(jsonable=json.loads(s), id_only=args.id_only)) for s in args.create]

    except Exception as e:
        if args.debug:
            raise e
        else:
            print(str(e))

if __name__ == '__main__':
    main()