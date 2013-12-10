import os
import json
import argparse
from wigiki import __version__
from wigiki.exceptions import WigikiConfigError


class ConfigReader(object):
    def __init__(self, filename):
        self.config = self.read_config(filename)

    def read_config(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        return data

    @property
    def gists(self):
        try:
            return self.config['gists']
        except KeyError:
            raise WigikiConfigError("No gists found in configuration")

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
        self.config = {}
        self.cli()

    def cli(self):
        """Read program parameters from command line and configuration files

        We support both command line arguments and configuration files.
        The command line arguments have always precedence over any
        configuration file parameters. This allows us to have most of
        our options in files but override them individually from the command
        line.
        """
        # first we parse only for a configuration file with an initial parser
        init_parser = argparse.ArgumentParser(
                description = __doc__,
                formatter_class = argparse.RawDescriptionHelpFormatter,
                add_help = False)

        # we don't use a file metavar because we need to support both json/yml
        init_parser.add_argument("-c", "--config", action="store",
                help = "read from target configuration file")

        args, remaining_args = init_parser.parse_known_args()

        # read from supplied configuration file or try to find one in the
        # current working directory
        reader = None
        if args.config:
            reader = ConfigReader(args.config)
        else:
            config_file = self.detect_config()
            if config_file:
                reader = ConfigReader(config_file)

        # implement the rest cli options
        parser = argparse.ArgumentParser(
                parents = [init_parser],
                add_help = True,
                description = "Static wiki generator using Github's gists as pages")

        application_opts = reader.application if reader else {}
        default_options = self.merge_with_default_options(application_opts)
        parser.set_defaults(**default_options)

        parser.add_argument("-v", "--version", action="version",
                version="%(prog)s {0}".format(__version__))

        parser.add_argument("-t", "--templates", action="store",
                help="read templates from specified folder")

        parser.add_argument("-o", "--output", action="store",
                help="generate static files in target folder")

        parser.add_argument("-u", "--baseurl", action="store",
                help="use a specific base URL instead of /")

        if reader:
            self.config = reader.config
        self.config['app'] = vars(parser.parse_args(remaining_args))

        # parsing of command line argumenents is done check if we have gists
        if 'gists' not in self.config:
            raise WigikiConfigError("Cannot read gists. "
                                    "Check your configuration file.")

    def detect_config(self):
        """check in the current working directory for configuration files"""
        default_files = ("config.json", "config.yml")
        for file_ in default_files:
            if os.path.exists(file_):
                return file_

    def merge_with_default_options(self, config_opts):
        """merge options from configuration file with the default options"""
        return dict(list(self.defaults.items()) + list(config_opts.items()))
