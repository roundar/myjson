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
        help="Upload JSON files to myjson",
        metavar='file',
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

    args = parser.parse_args(['-h'])

    try:
        if args.get:
            j = get(args.get[0])
            if args.compact:
                print(json.dumps(j, separators=(',',':')))
            else:
                print(json.dumps(j, indent=4))
        elif args.update:
            print(update(args.update[0], file=args.update[1]))

        elif args.create:
            for file in args.create:
                print(create(file=file, id_only=args.id_only))

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    main()