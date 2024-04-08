class Person:
    def __init__(self):
        self.firstname = 'Brian'
        self.lastname = 'Madsen'
        self._age = 44
        self.gender = 'Male'
        self.jobdescription = 'Rocker in LTF'

    @property
    def gender(self):
        return self._gender
    
    @gender.setter
    def gender(self, x):
        self._gender = x

    @gender.deleter
    def gender(self):
        del self._gender

##############################

    def get_age(self):
        return self._age
    
    def set_age(self, age):
        if age < 0:
            print('Not valid age')
        else:
            self._age = age
    
    def del_age(self):
        del self.age
    
    age = property(get_age, set_age, del_age)