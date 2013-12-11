from nose.tools import assert_equals
from wigiki.builder import Builder

def test_gist():
    assert_equals(Builder.gist(100),
                  '<script src="https://gist.github.com/100.js"></script>')

def test_page_list():
    assert_equals(Builder.page_list(['foo', 'bar']),
                  ['<a href="/foo">foo</a>', '<a href="/bar">bar</a>'])

def test_page_list_with_slug():
    assert_equals(Builder.page_list(['foo bar']),
                  ['<a href="/foo-bar">foo bar</a>'])

def test_slug_with_no_special_char():
    assert_equals(Builder.slugify('hello'), 'hello')

def test_slug_with_spaces():
    assert_equals(Builder.slugify('hello world'),'hello-world')

def test_slug_with_multiple_dashes():
    assert_equals(Builder.slugify('hello---world-'),'hello-world')

def test_slug_with_multiple_dashes_and_spaces():
    assert_equals(Builder.slugify('hello- -world'), 'hello-world')

def test_slug_with_trailing_space():
    assert_equals(Builder.slugify('hello '), 'hello')
