import sys
from wigiki.generator import SiteGenerator
from wigiki.config import ConfigReader

def main():
    config = ConfigReader(sys.argv[1])
    generator = SiteGenerator('templates', 'site',
        config.gists(), config.site())
    generator.run()
