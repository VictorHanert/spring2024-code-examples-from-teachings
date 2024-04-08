class Person:
    gender = 'Male' # class variable

    #instans:
    def __init__(self, age):
        self.age = age
        self.name = 'Victor' # public instans
    
    #methods:
    def getName(self):
        return self.name
    # underscore method
    def __len__(self):
        return len(self.name)
    
    def _set_age(self, age):
        if age < 0:
            print('Not valid age')
        else:
            self.age = age
    
    def _get_age(self):
        return self.age
    
    def _del_age(self):
        print('Deleted age')
        del self.age

    age = property(
        fget = _get_age,
        fset = _set_age,
        fdel = _del_age,
        doc = 'Age property'
    )