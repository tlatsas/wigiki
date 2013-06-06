import sys
from wigiki.generator import SiteGenerator
from wigiki.config import ConfigManager

def main():
    cm = ConfigManager()
    tpl_dir = cm.config['application']['templates']
    out_dir = cm.config['application']['output']
    generator = SiteGenerator(tpl_dir, out_dir,
        cm.config['gists'], cm.config['site'])
    generator.run()
