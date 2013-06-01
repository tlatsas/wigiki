import json

class ConfigReader(object):
    def __init__(self, filename):
        self.filename = filename
        self.config = self._read_config()


    def _read_config(self):
        with open(self.filename, 'r') as f:
            data = json.loads(f.read())
        return data


    def gists(self):
        return self.config['gists']


    def site(self):
        return self.config['site']

