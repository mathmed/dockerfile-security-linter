class Token:
    def __init__(self, tokenTuple):
        self.directive = tokenTuple[0]
        self.original = tokenTuple[3]
        self.start_line = tokenTuple[4]
        self.end_line = tokenTuple[5]
        self.value = tokenTuple[7]
