redis-completion
================

autocompletion with `redis <http://redis.io>`_ based on:

* http://antirez.com/post/autocomplete-with-redis.html
* http://stackoverflow.com/questions/1958005/redis-autocomplete/1966188
* http://patshaughnessy.net/2011/11/29/two-ways-of-using-redis-to-build-a-nosql-autocomplete-search-index

redis-completion is capable of storing a large number of phrases and quickly
searching them for matches.  Rich data can be stored and retrieved, helping you
avoid trips to the database when retrieving search results.

check out the `documentation <http://redis-completion.rtfd.org/>`_ for more info.

usage
-----

If you just want to store really simple things, like strings:

::

    engine = RedisEngine()
    titles = ['python programming', 'programming c', 'unit testing python',
              'testing software', 'software design']
    map(engine.store, titles)

    >>> engine.search('pyt')
    ['python programming', 'unit testing python']

    >>> engine.search('test')
    ['testing software', 'unit testing python']


If you want to store more complex data, like blog entries:

::

    Entry.create(title='an entry about python', published=True)
    Entry.create(title='all about redis', published=True)
    Entry.create(title='using redis with python', published=False)

    for entry in Entry.select():
        engine.store_json(entry.id, entry.title, {
            'published': entry.published,
            'title': entry.title,
            'url': entry.get_absolute_url(),
        })

    >>> engine.search_json('pytho')
    [{'published': True, 'title': 'an entry about python', 'url': '/blog/1/'},
     {'published': False, 'title': 'using redis with python', 'url': '/blog/3/'}]

    # just published entries, please
    >>> engine.search_json('redis', filters=[lambda i: i['published'] == True])
    [{u'published': True, u'title': u'all about redis', u'url': u'/blog/2/'}]


installing
----------

Install with pip::

    pip install redis-completion


Install via git::

    git clone https://github.com/coleifer/redis-completion.git
    cd redis-completion
    python setup.py install


schema
------

.. image:: http://redis-completion.readthedocs.org/en/latest/_images/schema.jpg



branch feature
------
Chinese support
