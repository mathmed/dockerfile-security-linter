class Token:
    def __init__(self, token_tuple):
        self.directive = token_tuple[0]
        self.original = token_tuple[3]
        self.start_line = token_tuple[4]
        self.end_line = token_tuple[5]
        self.value = token_tuple[7]
