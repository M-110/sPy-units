from __future__ import annotations
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from base_unit_enums import BaseUnit, Dimension
print("Importing registry")
registry: Dict[Dimension, BaseUnit] = {}


def add(dimension: Dimension, unit: BaseUnit):
    print(f"Registered {unit}")
    registry[dimension] = unit
    
    
def get_unit(dimension: Dimension) -> BaseUnit:
    try:
        return registry[dimension]
    except KeyError:
        pass
