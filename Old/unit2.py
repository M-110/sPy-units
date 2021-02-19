class Dimensions:
    DIMENSION_NAMES = ('time', 'length', 'mass', 'electric_current', 'thermodynamic_temperature', 'amount_of_substance',
                       'luminous_intensity')

    def __init__(self,
                 time: int = 0,
                 length: int = 0,
                 mass: int = 0,
                 electric_current: int = 0,
                 thermodynamic_temperature: int = 0,
                 amount_of_substance: int = 0,
                 luminous_intensity: int = 0):
        self.dimensions = (time, length, mass, electric_current, thermodynamic_temperature, amount_of_substance,
                           luminous_intensity)

    def __str__(self):
        return ' '.join([f'{name}^{count}'
                         for name, count in zip(self.DIMENSION_NAMES, self.dimensions)
                         if count])

    __repr__ = __str__

    def __eq__(self, other):
        if not isinstance(other, Dimensions):
            return NotImplemented

        return self.dimensions == other.dimensions

    def __hash__(self):
        return hash(self.dimensions)

    def __mul__(self, other):
        new_dimensions = tuple(x + y for x, y in zip(self.dimensions, other.dimensions))
        if not isinstance(other, Dimensions):
            new_dimensions = self.dimensions
        return Dimensions(*new_dimensions)

    def __truediv__(self, other):
        new_dimensions = tuple(x - y for x, y in zip(self.dimensions, other.dimensions))
        if not isinstance(other, Dimensions):
            new_dimensions = self.dimensions
        return Dimensions(*new_dimensions)
    
    def __invert__(self):
        new_dimensions = tuple(-dimension for dimension in self.dimensions)
        return Dimensions(*new_dimensions)
    
    def __pow__(self, power, modulo=None):
        new_dimensions = tuple(dimension * power for dimension in self.dimensions)
        return Dimensions(*new_dimensions)

    @property
    def time(self):
        return self.dimensions[0]

    @property
    def length(self):
        return self.dimensions[1]

    @property
    def mass(self):
        return self.dimensions[2]

    @property
    def electric_current(self):
        return self.dimensions[3]

    @property
    def thermodynamic_temperature(self):
        return self.dimensions[4]

    @property
    def amount_of_substance(self):
        return self.dimensions[5]

    @property
    def luminous_intensity(self):
        return self.dimensions[6]


m = Dimensions(length=1)
ms = Dimensions(length=1, time=-1)

s = Dimensions(time=1)
