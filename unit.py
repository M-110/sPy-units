from base_unit_enums import BaseUnit, Length, Time
import base_unit_enums
import derived_unit
import unit_registry


class Unit:
    def __init__(self, quantity: float, unit: BaseUnit):
        self.quantity = quantity
        self.unit = unit

    def __repr__(self):
        return f'{self.quantity} {self.unit.symbol}'

    def __add__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        if self.unit.dimensions != other.unit.dimensions:
            raise TypeError("Cannot add units of different dimensions.")

        if self.unit is other.unit:
            result = self.quantity + other.quantity
        else:
            result = self.quantity + self.unit.convert(other.quantity, other.unit)

        return Unit(result, self.unit)

    # __radd__ = __add__

    def __sub__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented

        if self.unit.dimensions != other.unit.dimensions:
            raise TypeError("Cannot add units of different dimensions.")

        if self.unit is other.unit:
            result = self.quantity - other.quantity
        else:
            result = self.quantity - self.unit.convert(other.quantity, other.unit)

        return Unit(result, self.unit)
    
    def __mul__(self, other):
        if not isinstance(other, BaseUnit):
            return NotImplemented
        

    def convert_to(self, new_unit: BaseUnit):
        return Unit(new_unit.convert(self.quantity, self.unit), new_unit)


a = Unit(5000, Length.meter)
b = Unit(3, Length.kilometer)

c = Unit(1, Time.hour)
d = Unit(3, Time.hour)

e = a.convert_to(Length.decameter)

print(e)

print(a - b)
print(b - b)

print(c - d)
print(c - c)

print(unit_registry.registry.items())
