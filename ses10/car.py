class Car:
    def __init__(self, make, model, bhp, mph):
        self.make = make
        self.model = model
        self.bhp = bhp  # brake horsepower
        self.mph = mph

    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, make):
        self._make = make

    @property
    def model(self):
        return self._model
    
    @model.setter
    def model(self, model):
        self._model = model

    @property
    def bhp(self):
        return self._bhp
    
    @bhp.setter
    def bhp(self, bhp):
        if bhp > 0:
            self._bhp = bhp
        else:
            raise ValueError("Brake horsepower must be more than zero")

    @property
    def mph(self):
        return self._mph
    
    @mph.setter
    def mph(self, mph):
        if mph > 0:
            self._mph = mph
        else:
            raise ValueError("Miles per hour must be more than zero")


car1 = Car('Ford', 'Focus', 150, 190)

print(car1.make)  # Output: 'Ford'
print(car1.model)
