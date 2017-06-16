
`{} mjson <http://mysjon.com>`_
========================

Quickly, freely host json data with this Python wrapper for the `{} mjson <http://mysjon.com>`_ free beta service.

Install
~~~~~~~
::

   pip install myjson

Use as module:
~~~~~~~~~~~~~~

::

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


As a script
~~~~~~~~~~~

::

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

Thanks
======
`@lance_ramoth <https://twitter.com/lance_ramoth>`_ for providing `this service! <http://myjson.com/about>`_
