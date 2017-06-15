# mjson
  

Quickly, freely host json data with this Python wrapper for the mysjon.com free beta service.

Anyone can read and alter this data as soon as you post it...

## Install
`pip install git+https://github.com/roundar/myjson`

## Use as module:

If you can use python's `json` module, you can use this one:

``` python
>>> import myjson
>>> o = {"test": "ing"}
>>> url = myjson.dump(o)
>>> url
'https://api.myjson.com/bins//183j9v'
>>> myjson.load(url)
{'test': 'ing'}
>>> id = myjson.dump({"another": "test"}, id_only=True)
>>> id
'12qmtv'
>>> myjson.load(id)
{'another': 'test'}

```

## As a script
```bash
~$ myjson --create my.json myother.json
https://myjson.com/y7ftv
https://myjson.com/47h22
~$ myjson --get https://myjson.com/y7ftv
{"example":"json"}
~$ myjson --get y7ftv
{"example":"json"}
~$ mysjon -h
usage: myjson [-h] (--get id | --update id file | --create [file [file ...]])
              [--id-only] [--compact]

A python commandline utility for working with https://myjson.com/

optional arguments:
  -h, --help            show this help message and exit
  --get id              Download the json associated with this ID (also
                        accepts full URL)
  --update id file      Updates the JSON associated with the given ID (or URL)
  --create [file [file ...]]
                        Upload JSON files to myjson
  --id-only             Only return the id instead of the full url. (Used with
                        --create)
  --compact             Compact output by removing whitespace. (Used with
                        --get)
```