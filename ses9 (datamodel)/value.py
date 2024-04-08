class Value:
    def __init__(self, data, op='', parents=(), label=''):
        self.data = data
        self.op = op
        self.parents = parents
        self.label = label

    def __repr__(self):
        return f'{self.__dict__}'
    # Can now call a instead of a.__repr__()

    def __str__(self):
        return f'Value of the data is: {self.data}'
    
    def __add__(self, other):
        return Value(self.data + other.data, '+', (self, other))

a = Value(19, 'a')
b = Value(31, 'b')
c = a + b
