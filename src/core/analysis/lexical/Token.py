class Token:

    def __init__(self, directive, original, start_line, end_line, value):

        self.directive = directive
        self.original = original
        self.start_line = start_line
        self.end_line = end_line
        self.value = value

    def set_value(self, value):
        self.value = value