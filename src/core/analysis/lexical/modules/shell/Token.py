class Token:

    def __init__(self, directive = "", value = []):
        self.directive = directive
        self.value = value

    def set_directive(self, directive):
        self.directive = directive

    def set_value(self, value):
        self.value = value