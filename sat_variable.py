class Variable:

    def __init__(self, id, neg=False):
        self.ident = id
        self.negation = neg
        self.value = False

    def print(self):
        if self.negation:
            print('~', end='')
        print(self.ident, end=' ')
