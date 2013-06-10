import os
import json
import argparse
from wigiki import __version__

class UnknownConfigFileException(Exception):
    pass

class WrongConfigOptionException(Exception):
    pass

class EmptyConfigException(Exception):
    pass


class ConfigReader(object):
    def __init__(self, filename):
        self.filename = filename
        self.config = self._read_config()

    def _read_config(self):
        with open(self.filename, 'r') as f:
            data = json.loads(f.read())
        return data

    @property
    def gists(self):
        try:
            return self.config['gists']
        except KeyError:
            raise EmptyConfigException()

    @property
    def site(self):
        try:
            return self.config['site']
        except KeyError:
            return {}

    @property
    def application(self):
        try:
            return self.config['app']
        except KeyError:
            return {}


class ConfigManager(object):
    defaults = {
        'templates': 'templates',
        'output': 'site',
        'baseurl': '/'
    }

    def __init__(self):
        self.config = None
        self.cli()

    def cli(self):
        # first we parse only for a configuration file with an initial parser
        init_parser = argparse.ArgumentParser(
                description = __doc__,
                formatter_class = argparse.RawDescriptionHelpFormatter,
                add_help = False)

        # we don't use a file metavar because we need to support both json/yml
        init_parser.add_argument("-c", "--config", action="store",
                help = "read from target configuration file")

        args, remaining_args = init_parser.parse_known_args()

        # read from supplied config file or try to find one on cwd
        if args.config:
            cr = ConfigReader(args.config)
        else:
            config_file = self.detect_config()
            if config_file:
                cr = ConfigReader(config_file)
            else:
                raise UnknownConfigFileException()

        # implement the rest cli options
        parser = argparse.ArgumentParser(
                parents = [init_parser],
                add_help = True,
                description = "Simple static site generator that uses Gists as pages")

        default_options = self.merge_with_default_options(cr.application)
        parser.set_defaults(**default_options)

        parser.add_argument("-v", "--version", action="version",
                version="%(prog)s {0}".format(__version__))

        parser.add_argument("-t", "--templates", action="store",
                help="read templates from specified folder")

        parser.add_argument("-o", "--output", action="store",
                help="generate static files in target folder")

        parser.add_argument("-u", "--baseurl", action="store",
                help="use a specific base URL instead of /")

        self.config = cr.config
        self.config['application'] = vars(parser.parse_args(remaining_args))

    def detect_config(self):
        default_files = ("config.json", "config.yml")
        for file_ in default_files:
            if os.path.exists(file_):
                return file_

    def merge_with_default_options(self, cfg_options):
        """merge options from configuration file with the default options"""
        return dict(list(self.defaults.items()) + list(cfg_options.items()))
