from base_unit_enums import Length
import derived_unit
from unit import Unit
from unit_registry import registry

a = Unit(2, Length.meter)
b = Unit(3, Length.meter)
c = a * b

# new_unit = create_custom_derived_unit(Length.meter, Length.meter)
# 
# print(repr(new_unit))