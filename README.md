# Realtime earthquakes with USGS

This project serves as a basic way to get started with RethinkDB and ReQL (its
query language), by building a simple app that shows an updated feed of the
latest earthquakes, reported by [USGS](http://www.usgs.gov/).

### Basic requirements

You'll need the following:

  - Python 2.7+
  - The `flask` module (`pip install Flask`)
  - The `rethinkdb` module (`pip install rethinkdb`)
  - A running RethinkDB instance. Note that RethinkDB runs on OS X and Linux
    (if you run Windows, you can use
    [Vagrant](https://github.com/zoontek/vagrant-rethinkdb) or [a hosted
    service](https://www.compose.io/rethinkdb/)).

### Writing your first query

You'll need to write your first ReQL query to get the app running. Open
`app.py` and look for the TODOs in the code. They should explain what needs to
be included. You might find the [RethinkDB API](http://rethinkdb.com/api) and
[documentation](http://rethinkdb.com/docs) helpful.

Once you get the basic query filled out, you can try running the app:

```
python app.py
```

A solution is provided in the `solution` directory, in case you get stuck.
