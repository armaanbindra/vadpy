import collections

class Option(object):
    def __init__(self, 
                 name = None,
                 description = '', 
                 parse_type = str, 
                 parse_func = None,
                 default = None):
        """

        default - default value (string, as if recieved from command-line)
        """
        self.name = name    # if None, will be set from attribute name
        self.module = None  # set by ModuleMetaclass 
        self.description = description
        self.parse_type = parse_type
        self.parse_func = parse_func
        self.default = default

        assert not parse_func or isinstance(parse_func, collections.Callable), 'Option has uncallable parse_func argument'

    def parse(self, value):
        if self.parse_func: 
            try:
                value = self.parse_func(value)
            except AttributeError:
                pass
        elif self.parse_type == bool and not isinstance(value, bool):
            value = value.lower() not in ['', '""', "''", 'no', 'false']
        else:
            value = self.parse_type(value) # type conversion
        
        return value
