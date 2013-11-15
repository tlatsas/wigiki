# wigiki

## about

Wigiki is a python application which can render static html wiki-like 
sites using Github's Gists as pages. I use Gists to keep quick notes, but
the important ones can get quickly lost due to the high signal to noise
ratio. With wigiki I can group the important ones in a single place which
I can deploy anywhere as it is just html+css files. Here is how it
[looks][site-sample] using the default template theme.


## installation

To install from pypi:
```
$ pip install wigiki
```

To install from source, clone the repo and then run:

```
$ python setup.py install
```

If you want to install wigiki in order to contribute code, clone
the repo and then run:

```
$ pip install -e .
```

It is also a good idea to use a virtual environment (virtualenv/virtualenvwrapper).

## getting started

Using wigiki is as simple as creating a configuration file (see [sample][cfg-sample])
and running `wigiki`.

For a list of command line arguments use `--help` or consult the documentation.

* [documentation][gh-docs]
* [issues][gh-issues]
* [source code][gh-source]


## license

See `LICENSE`.

[gh-docs]: http://tlatsas.github.io/wigiki/
[gh-issues]: https://github.com/tlatsas/wigiki/issues
[gh-source]: https://github.com/tlatsas/wigiki
[cfg-sample]: https://github.com/tlatsas/wigiki/blob/master/config.json.sample
[site-sample]: https://dl.kodama.gr/notes
