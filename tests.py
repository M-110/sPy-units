from derived_unit import create_custom_derived_unit
from base_unit_enums import Length
from unit import Unit

a = Unit(2, Length.meter)
b = Unit(3, Length.meter)
#c = a * b

new_unit = create_custom_derived_unit(Length.meter, Length.meter)

print(repr(new_unit))