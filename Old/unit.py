from enum import Enum

class Dimensions:
    DIMENSION_NAMES = ('time', 'length', 'mass', 'electric current', 'thermodynamic temperature', 'amount of substance',
                       'luminous intensity')
    
    def __init__(self,
                 time: int = 0,
                 length: int = 0,
                 mass: int = 0,
                 electric_current: int = 0,
                 thermodynamic_temperature: int = 0,
                 amount_of_substance: int = 0,
                 luminous_intensity: int = 0):
        self.time = time
        self.length = length
        self.mass = mass
        self.electric_current = electric_current
        self.thermodynamic_temperature = thermodynamic_temperature
        self.amount_of_substance = amount_of_substance
        self.luminous_intensity = luminous_intensity
        self.dimensions = (time,
                           length,
                           mass,
                           electric_current,
                           thermodynamic_temperature,
                           amount_of_substance,
                           luminous_intensity)
        
    def _dimensions_as_tuple(self) -> tuple:
        return (self.time,
                self.length,
                self.mass,
                self.electric_current,
                self.thermodynamic_temperature,
                self.amount_of_substance,
                self.luminous_intensity)
    
    def __str__(self):
        return ' '.join([f'{name}^{count}'
                         for name, count in zip(self.DIMENSION_NAMES, self._dimensions_as_tuple())
                         if count])

    def __eq__(self, other):
        if not isinstance(other, Dimensions):
            return NotImplemented

        return self.time == other.time and \
            self.length == other.length and \
            self.mass == other.mass and \
            self.electric_current == other.electric_current and \
            self.amount_of_substance == other.amount_of_substance and \
            self.luminous_intensity == other.luminous_intensity
    
    def __mul__(self, other):
        if not isinstance(other, Dimensions):
            other = Dimensions()
        self_dimensions = self._dimensions_as_tuple()
        other_dimensions = other._dimensions_as_tuple()
        
        new_dimensions = (self_dim + other_dim for self_dim, other_dim in zip(self_dimensions, other_dimensions))
        
        return Dimensions(*new_dimensions)
    
    def __truediv__(self, other):
        if not isinstance(other, Dimensions):
            other = Dimensions()
        self_dimensions = self._dimensions_as_tuple()
        other_dimensions = other._dimensions_as_tuple()

        new_dimensions = (self_dim - other_dim for self_dim, other_dim in zip(self_dimensions, other_dimensions))

        return Dimensions(*new_dimensions)
    
    def __pow__(self, power, modulo=None):
        self_dimensions = self._dimensions_as_tuple()
        
        new_dimensions = (self_dim * power for self_dim in self_dimensions)
        
        return Dimensions(*new_dimensions)
    
    
class Unit:
    def __init__(self, value: float = 1, dimensions: Dimensions = None):
        if dimensions is None:
            dimensions = Dimensions()
        self.value = value
        self.dimensions = dimensions
    
    def __repr__(self):
        return f'{self.value} {self.dimensions}'
    
    def __add__(self, other):
        try:
            if self.dimensions == other.dimensions:
                return Unit(self.value + other.value, self.dimensions)
            else:
                raise ValueError('Units must be of the same dimensions to be added.')
        except AttributeError:
            return NotImplemented
        
    __radd__ = __add__
    
    def __sub__(self, other):
        try:
            if self.dimensions == other.dimensions:
                return Unit(self.value - other.value, self.dimensions)
            else:
                raise ValueError('Units must be of the same dimensions to be subtracted')
        except AttributeError:
            return NotImplemented
        
    def __rsub__(self, other):
        try:
            if self.dimensions == other.dimensions:
                return Unit(other.value - self.value, self.dimensions)

            else:
                raise ValueError('Units must be of the same dimensions to be subtracted.')
        except AttributeError:
            return NotImplemented
        
    def __mul__(self, other):
        try:
            return Unit(self.value * other.value,
                        (self.dimensions * other.dimensions))
        except AttributeError:
            try:
                return Unit(self.value * other, self.dimensions)
            except TypeError:
                return NotImplemented
        
    __rmul__ = __mul__
    
    def __truediv__(self, other):
        try:
            return Unit(self.value / other.value,
                        (self.dimensions / other.dimensions))
        except AttributeError:
            try:
                return Unit(self.value / other, self.dimensions)
            except TypeError:
                return NotImplemented

    def __rtruediv__(self, other):
        try:
            return Unit(other.value / self.value,
                        (other.dimensions / self.dimensions))
        except AttributeError:
            try:
                return Unit(other / self.value, self.dimensions)
            except TypeError:
                return NotImplemented
            
    def __floordiv__(self, other):
        try:
            return Unit(self.value // other.value,
                        (self.dimensions / other.dimensions))
        except AttributeError:
            try:
                return Unit(self.value // other, self.dimensions)
            except TypeError:
                return NotImplemented

    def __rfloordiv__(self, other):
        try:
            return Unit(other.value // self.value,
                        (other.dimensions / self.dimensions))
        except AttributeError:
            try:
                return Unit(other // self.value, self.dimensions)
            except TypeError:
                return NotImplemented
            
    def __pow__(self, power, modulo=None):
        try:
            return Unit(self.value ** power,
                        self.dimensions ** power)
        except TypeError:
            return NotImplemented 
    
    def __neg__(self):
        return Unit(-self.value, *self.dimensions.dimensions)
        
class MetricUnits(Enum):
    # Metric Multiples
    base = (1, '', '')
    deca = (1E1, 'da', 'deca')
    hecto = (1E2, 'h', 'hecto')
    kilo = (1E3, 'k', 'kilo')
    mega = (1E6,'M', 'mega')
    giga = (1E9,'G', 'giga')
    tera = (1E12, 'T', 'tera')
    peta = (1E15, 'P', 'peta')
    exa = (1E18, 'E', 'exa')
    zetta = (1E21, 'Z', 'zetta')
    yotta = (1E24, 'Y', 'yotta')
    
    # Metric Submultiples
    deci = (1E-1, 'd', 'deci')
    centi = (1E-2, 'c', 'centi')
    milli = (1E-3, 'm', 'milli')
    micro = (1E-6,'mu', 'micro')
    nano = (1E-9,'n', 'nano')
    pico = (1E-12, 'p', 'pico')
    femto = (1E-15, 'f', 'femto')
    atto = (1E-18, 'a', 'atto')
    zepto = (1E-21, 'z', 'zepto')
    yocto = (1E-24, 'y', 'yocto')
    
    def __new__(cls, value: float, symbol: str, name: str):
        member = object.__new__(cls)
        
        member._value_ = value
        member.symbol = symbol
        member.full_name = name
        
        return member
    
    @classmethod
    def get_multiple_conversion(cls, from_unit, to_unit):
        return to_unit.value / from_unit.value
    
    
m = Dimensions(length=1)
s = Dimensions(time=1)

        
a = Unit(5, m)
b = Unit(3, m)
c = Unit(2, s)
d = Unit(0, s)
e = Unit()

#(200 * m/s + 400 mi/h)^2
