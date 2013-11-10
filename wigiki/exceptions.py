class WigikiError(Exception):
    pass


class WigikiConfigError(WigikiError):
    def __init__(self, msg=None):
        self.code = 2
        self.msg = msg or "Configuration error, try the --help switch"

    def __str__(self):
        return self.msg


class WigikiParserError(WigikiError):
    def __init__(self, msg=None):
        self.code = 3
        self.msg = msg or ("Error while parsing gist data, check your "
                           "configuration format")

    def __str__(self):
        return self.msg


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
