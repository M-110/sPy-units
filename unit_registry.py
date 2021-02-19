from __future__ import annotations
from typing import Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from base_unit_enums import BaseUnit, Dimension

registry: Dict[Dimension, BaseUnit] = {}


def add(dimension: Dimension, unit: BaseUnit):
    registry[dimension] = unit
    
    
def get_unit(dimension: Dimension) -> BaseUnit:
    try:
        return registry[dimension]
    except KeyError:
        pass
    
    