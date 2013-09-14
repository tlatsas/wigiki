class WigikiError(Exception):
    pass


class WigikiConfigError(WigikiError):
    def __init__(self):
        self.code = 2

    def __str__(self):
        return "Configuration error, try the --help switch"


class WigikiParserError(WigikiError):
    def __init__(self):
        self.code = 3

    def __str__(self):
        return "Error while parsing gist data, check your configuration format"


class WigikiGeneratorError(WigikiError):
    def __init__(self):
        self.code = 4

    def __str__(self):
        return "Error while generating site files"


class WigikiTemplateError(WigikiError):
    def __init__(self):
        self.code = 5

    def __str__(self):
        return "Error while handling template files"
