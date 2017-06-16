# mjson
  

Quickly, freely host json data with this Python wrapper for the mysjon.com free beta service.

Warning: Anyone can read and alter this data as soon as you post it...

## Install
`pip install git+https://github.com/roundar/myjson`

## Use as module:

If you can use python's `json` module, you can use this one:

``` python

>>> import myjson
>>> import json
>>> url = myjson.store(json.dumps({"test": "ing"}))
>>> url
'https://api.myjson.com/bins/ccq2j'
>>> json.loads(myjson.get(url))["test"]
'ing'
>>> id = myjson.store(json.dumps({"alpha": "beta"}), update=url, id_only=True)
>>> print(myjson.get(id))
{"alpha":"beta"}
>>> print(myjson.get(url))
{"alpha":"beta"}
>>> id
'ccq2j'
>>> url
'https://api.myjson.com/bins/ccq2j'
```

## As a script
```bash
~$ myjson -h
usage: myjson [-h] {get,store} ...

A python commandline utility for working with https://myjson.com/

positional arguments:
  {get,store}  mjson commands

optional arguments:
  -h, --help   show this help message and exit
~$ myjson store example.json
https://api.myjson.com/bins/ut5tn
~$ myjson get ut5n --compact
[1,2,3]

```