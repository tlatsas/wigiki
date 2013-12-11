import sys

from nose import with_setup
from nose.tools import assert_equals, raises

from wigiki.config import ConfigReader
from wigiki.exceptions import *


if sys.version_info >= (3,):
    from io import StringIO
else:
    from StringIO import StringIO


class TestReaderMinimal():
    """Test reader with a minimal configuration file"""

    def setup(self):
        config = '''
        {
            "gists": {
                "user": { "title": "id" }
            }
        }
        '''
        f = StringIO(config)
        self.reader = ConfigReader(f.read())

    def test_read_site(self):
        assert_equals(self.reader.site, {})

    def test_read_gists(self):
        data = {'user': {'title': 'id'}}
        assert_equals(self.reader.gists, data)

    def test_read_app(self):
        assert_equals(self.reader.application, {})


class TestReaderInvalid():
    """Test reader with a wrong configuration file"""

    def setup(self):
        config = '''
        {
            "app" : { "baseurl": "/" }
        }
        '''
        f = StringIO(config)
        self.reader = ConfigReader(f.read())

    @raises(WigikiConfigError)
    def test_read_sists(self):
        self.reader.gists
