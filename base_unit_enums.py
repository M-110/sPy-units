from __future__ import annotations
from enum import Enum
from collections import namedtuple
import unit_registry

Dimension = namedtuple('Dimension', 'time length mass current temperature amount luminous_intensity angle')

si_units = (
    ('second', 's'),
    ('meter', 'm'),
    ('kilogram', 'g'),
    ('ampere', 'A'),
    ('kelvin', 'K'),
    ('mole', 'mol'),
    ('candela', 'cd'),
)


def set_dimensions(mass=0, length=0, time=0, current=0, temperature=0, amount=0, luminous_intensity=0, angle=0):
    def dimension_decorator(unit_enum):
        unit_enum.dimensions = {'time': time, 'length': length, 'mass': mass, 'current': current,
                                'temperature': temperature, 'amount': amount, 'luminous_intensity': luminous_intensity,
                                'angle': angle}
        unit_enum.dimensions = Dimension(time=time, length=length, mass=mass, current=current, temperature=temperature,
                                         amount=amount, luminous_intensity=luminous_intensity, angle=angle)
        unit_registry.add(unit_enum.dimensions, unit_enum)
        return unit_enum
    return dimension_decorator


class BaseUnit(Enum):
    def __new__(cls, value: float, symbol: str, proper_name: str, plural_form: str = None):
        member = object.__new__(cls)

        member._value_ = symbol
        member.multiplier = value
        member.symbol = symbol
        member.proper_name = proper_name
        member.plural_form = plural_form or proper_name + 's'
        
        return member

    def __repr__(self):
        return f'{self.__class__.__name__}.{self.name}'

    def __str__(self):
        return self.proper_name

    def convert(self, quantity: float, other: BaseUnit) -> float:
        """Converts quantity from other unit to self's unit.
        
        Args:
            quantity: the value to be converted.
            other: the unit to be converted from.
            
        Returns:
            quantity in the current unit type
        """
        if self is other:
            return quantity
        else:
            return quantity * other.multiplier / self.multiplier


class BaseTemperature(BaseUnit):
    def convert(self, quantity: float, other: BaseTemperature) -> float:
        """Converts quantity from another unit to this unit.
        
        Args:
            quantity: the value to be converted.
            other: the unit to be converted from.
            
        Returns:
            quantity in the current unit type
        """
        if self is other:
            print('no change')
            return quantity

        if self is Temperature.celsius:
            if other is Temperature.fahrenheit:
                print('f to c')
                return (quantity - 32) * 5 / 9
            else:
                print('k to c')
                return quantity * other.multiplier - 273.15
        elif self is Temperature.fahrenheit:
            if other is Temperature.celsius:
                print('c to f')
                return (quantity * 9 / 5) + 32
            else:
                print('k to f')
                return (quantity * other.multiplier - 273.15) * 9 / 5 + 32
        else:
            if other is Temperature.celsius:
                print('c to k')
                return (quantity + 273.15) / self.multiplier
            elif other is Temperature.fahrenheit:
                print('f to k')
                return ((quantity - 32) * 5 / 9 + 273.15) / self.multiplier
            else:
                print('k to k')
                return quantity * self.multiplier / other.multiplier


@set_dimensions(time=1)
class Time(BaseUnit):
    second = (1, 's', 'second')
    decasecond = (10.0, 'das', 'decasecond')
    hectosecond = (100.0, 'hs', 'hectosecond')
    kilosecond = (1000.0, 'ks', 'kilosecond')
    megasecond = (1000000.0, 'Ms', 'megasecond')
    gigasecond = (1000000000.0, 'Gs', 'gigasecond')
    terasecond = (1000000000000.0, 'Ts', 'terasecond')
    petasecond = (1000000000000000.0, 'Ps', 'petasecond')
    exasecond = (1e+18, 'Es', 'exasecond')
    zettasecond = (1e+21, 'Zs', 'zettasecond')
    yottasecond = (1e+24, 'Ys', 'yottasecond')
    decisecond = (0.1, 'ds', 'decisecond')
    centisecond = (0.01, 'cs', 'centisecond')
    millisecond = (0.001, 'ms', 'millisecond')
    microsecond = (1e-06, 'μs', 'microsecond')
    nanosecond = (1e-09, 'ns', 'nanosecond')
    picosecond = (1e-12, 'ps', 'picosecond')
    femtosecond = (1e-15, 'fs', 'femtosecond')
    attosecond = (1e-18, 'as', 'attosecond')
    zeptosecond = (1e-21, 'zs', 'zeptosecond')
    yoctosecond = (1e-24, 'ys', 'yoctosecond')
    planck_time = (5.39e-44, 'tP', 'Planck time')
    jiffy = (3e-24, 'j', 'jiffy', 'jiffies')
    minute = (60, 'min', 'minute')
    hour = (3600, 'h', 'hour')
    day = (86400, 'd', 'day')
    week = (604800, 'week', 'week')
    fortnight = (1209600, 'fortnight', 'fortnight')
    month = (2628000.0, 'mo', 'month')
    year = (31540000.0, 'yr', 'year')
    decade = (315600000.0, 'decade', 'decade')
    century = (3156000000.0, 'century', 'century', 'centuries')
    millennium = (31560000000.0, 'millennium', 'millennium', 'millennia')
    galactic_year = (7490000000000000.0, 'galactic year', 'galactic year')
    aeon = (3.154e+16, 'aeon', 'aeon')


@set_dimensions(length=1)
class Length(BaseUnit):
    meter = (1, 'm', 'meter')
    decameter = (10.0, 'dam', 'decameter')
    hectometer = (100.0, 'hm', 'hectometer')
    kilometer = (1000.0, 'km', 'kilometer')
    megameter = (1000000.0, 'Mm', 'megameter')
    gigameter = (1000000000.0, 'Gm', 'gigameter')
    terameter = (1000000000000.0, 'Tm', 'terameter')
    petameter = (1000000000000000.0, 'Pm', 'petameter')
    exameter = (1e+18, 'Em', 'exameter')
    zettameter = (1e+21, 'Zm', 'zettameter')
    yottameter = (1e+24, 'Ym', 'yottameter')
    decimeter = (0.1, 'dm', 'decimeter')
    centimeter = (0.01, 'cm', 'centimeter')
    millimeter = (0.001, 'mm', 'millimeter')
    micrometer = (1e-06, 'μm', 'micrometer')
    nanometer = (1e-09, 'nm', 'nanometer')
    picometer = (1e-12, 'pm', 'picometer')
    femtometer = (1e-15, 'fm', 'femtometer')
    attometer = (1e-18, 'am', 'attometer')
    zeptometer = (1e-21, 'zm', 'zeptometer')
    yoctometer = (1e-24, 'ym', 'yoctometer')
    angstrom = (1e-10, 'Å', 'angstrom')
    inch = (0.0254, 'in', 'inch', 'inches')
    foot = (0.3048, 'ft', 'foot', 'feet')
    yard = (0.9144, 'yd', 'yard')
    mile = (1609, 'mi', 'mile')
    league = (4828, 'league', 'league')
    fathom = (1.829, 'fathom', 'fathom')
    nautical_mile = (1852, 'nmi', 'nautical mile')
    rod = (5.029, 'rod', 'rod')
    chain = (20.12, 'chain', 'chain')
    earth_radius = (6378000.0, 'R⊕', 'Earth radius', 'Earth radii')
    lunar_distance = (403400000.0, 'LD', 'Lunar distance')
    astronomical_unit = (149600000000.0, 'au', 'astronomical unit')
    light_year = (9461000000000.0, 'ly', 'light-year')
    parsec = (3.086e+16, 'pc', 'parsec')
    kiloparsec = (3.086e+19, 'kpc', 'kiloparsec')
    megaparsec = (3.086e+22, 'Mpc', 'megaparsec')
    gigaparsec = (3.086e+25, 'Gpc', 'gigaparsec')
    hubble_length = (1.4e+26, 'cH0', 'Hubble length')
    electron_radius = (2.81794033e-15, 'r0', 'electron radius', 'electron radii')
    bohr_radius = (5.29177211e-11, 'a0', 'Bohr radius', 'Bohr radii')
    planck_length = (1.6163e-35, 'ℓP', 'Planck length')


@set_dimensions(mass=1)
class Mass(BaseUnit):
    gram = (0.001, 'g', 'gram')
    decagram = (0.01, 'dag', 'decagram')
    hectogram = (0.1, 'hg', 'hectogram')
    kilogram = (1, 'kg', 'kilogram')
    megagram = (1000.0, 'Mg', 'megagram')
    gigagram = (1000000.0, 'Gg', 'gigagram')
    teragram = (1000000000.0, 'Tg', 'teragram')
    petagram = (1000000000000.0, 'Pg', 'petagram')
    exagram = (1000000000000000.0, 'Eg', 'exagram')
    zettagram = (1e+18, 'Zg', 'zettagram')
    yottagram = (1e+21, 'Yg', 'yottagram')
    decigram = (0.0001, 'dg', 'decigram')
    centigram = (1e-05, 'cg', 'centigram')
    milligram = (1e-06, 'mg', 'milligram')
    microgram = (1e-09, 'μg', 'microgram')
    nanogram = (1e-12, 'ng', 'nanogram')
    picogram = (1e-15, 'pg', 'picogram')
    femtogram = (1e-18, 'fg', 'femtogram')
    attogram = (1e-21, 'ag', 'attogram')
    zeptogram = (1e-24, 'zg', 'zeptogram')
    yoctogram = (1e-27, 'yg', 'yoctogram')
    tonne = (1000.0, 't', 'tonne')
    short_ton = (907.2, 'sh tn', 'short ton')
    long_ton = (1016, 'lg tn', 'long ton')
    atomic_mass_unit = (1.66053907e-27, 'u', 'atomic mass unit')
    slug = (14.59, 'sl', 'slug')
    grain = (6.48e-05, 'gr', 'grain')
    ounce = (0.02835, 'oz', 'ounce')
    stone = (6.35, 'st', 'stone')
    pound = (0.4536, 'lb', 'pound')
    planck_mass = (2.1764e-08, 'mP', 'Planck mass', 'Planck masses')
    solar_mass = (1.988435e+30, 'M☉', 'solar mass', 'solar masses')


@set_dimensions(current=1)
class Current(BaseUnit):
    ampere = (1, 'A', 'ampere')
    decaampere = (10.0, 'daA', 'decaampere')
    hectoampere = (100.0, 'hA', 'hectoampere')
    kiloampere = (1000.0, 'kA', 'kiloampere')
    megaampere = (1000000.0, 'MA', 'megaampere')
    gigaampere = (1000000000.0, 'GA', 'gigaampere')
    teraampere = (1000000000000.0, 'TA', 'teraampere')
    petaampere = (1000000000000000.0, 'PA', 'petaampere')
    exaampere = (1e+18, 'EA', 'exaampere')
    zettaampere = (1e+21, 'ZA', 'zettaampere')
    yottaampere = (1e+24, 'YA', 'yottaampere')
    deciampere = (0.1, 'dA', 'deciampere')
    centiampere = (0.01, 'cA', 'centiampere')
    milliampere = (0.001, 'mA', 'milliampere')
    microampere = (1e-06, 'μA', 'microampere')
    nanoampere = (1e-09, 'nA', 'nanoampere')
    picoampere = (1e-12, 'pA', 'picoampere')
    femtoampere = (1e-15, 'fA', 'femtoampere')
    attoampere = (1e-18, 'aA', 'attoampere')
    zeptoampere = (1e-21, 'zA', 'zeptoampere')
    yoctoampere = (1e-24, 'yA', 'yoctoampere')
    abampere = (10, 'aA', 'abampere')


@set_dimensions(temperature=1)
class Temperature(BaseTemperature):
    kelvin = (1, 'K', 'kelvin')
    decakelvin = (10.0, 'daK', 'decakelvin')
    hectokelvin = (100.0, 'hK', 'hectokelvin')
    kilokelvin = (1000.0, 'kK', 'kilokelvin')
    megakelvin = (1000000.0, 'MK', 'megakelvin')
    gigakelvin = (1000000000.0, 'GK', 'gigakelvin')
    terakelvin = (1000000000000.0, 'TK', 'terakelvin')
    petakelvin = (1000000000000000.0, 'PK', 'petakelvin')
    exakelvin = (1e+18, 'EK', 'exakelvin')
    zettakelvin = (1e+21, 'ZK', 'zettakelvin')
    yottakelvin = (1e+24, 'YK', 'yottakelvin')
    decikelvin = (0.1, 'dK', 'decikelvin')
    centikelvin = (0.01, 'cK', 'centikelvin')
    millikelvin = (0.001, 'mK', 'millikelvin')
    microkelvin = (1e-06, 'μK', 'microkelvin')
    nanokelvin = (1e-09, 'nK', 'nanokelvin')
    picokelvin = (1e-12, 'pK', 'picokelvin')
    femtokelvin = (1e-15, 'fK', 'femtokelvin')
    attokelvin = (1e-18, 'aK', 'attokelvin')
    zeptokelvin = (1e-21, 'zK', 'zeptokelvin')
    yoctokelvin = (1e-24, 'yK', 'yoctokelvin')
    fahrenheit = ('f', '°F', 'degree Fahrenheit', 'degrees Fahrenheit')
    celsius = ('c', '°C', 'degree Celsius', 'degrees Celsius')


@set_dimensions(amount=1)
class Amount(BaseUnit):
    mole = (1, 'mol', 'mole')
    decamole = (10.0, 'damol', 'decamole')
    hectomole = (100.0, 'hmol', 'hectomole')
    kilomole = (1000.0, 'kmol', 'kilomole')
    megamole = (1000000.0, 'Mmol', 'megamole')
    gigamole = (1000000000.0, 'Gmol', 'gigamole')
    teramole = (1000000000000.0, 'Tmol', 'teramole')
    petamole = (1000000000000000.0, 'Pmol', 'petamole')
    examole = (1e+18, 'Emol', 'examole')
    zettamole = (1e+21, 'Zmol', 'zettamole')
    yottamole = (1e+24, 'Ymol', 'yottamole')
    decimole = (0.1, 'dmol', 'decimole')
    centimole = (0.01, 'cmol', 'centimole')
    millimole = (0.001, 'mmol', 'millimole')
    micromole = (1e-06, 'μmol', 'micromole')
    nanomole = (1e-09, 'nmol', 'nanomole')
    picomole = (1e-12, 'pmol', 'picomole')
    femtomole = (1e-15, 'fmol', 'femtomole')
    attomole = (1e-18, 'amol', 'attomole')
    zeptomole = (1e-21, 'zmol', 'zeptomole')
    yoctomole = (1e-24, 'ymol', 'yoctomole')
    atom = (6.022e+23, 'atom', 'atom')


@set_dimensions(luminous_intensity=1)
class LuminousIntensity(BaseUnit):
    candela = (1, 'cd', 'candela')
    decacandela = (10.0, 'dacd', 'decacandela')
    hectocandela = (100.0, 'hcd', 'hectocandela')
    kilocandela = (1000.0, 'kcd', 'kilocandela')
    megacandela = (1000000.0, 'Mcd', 'megacandela')
    gigacandela = (1000000000.0, 'Gcd', 'gigacandela')
    teracandela = (1000000000000.0, 'Tcd', 'teracandela')
    petacandela = (1000000000000000.0, 'Pcd', 'petacandela')
    exacandela = (1e+18, 'Ecd', 'exacandela')
    zettacandela = (1e+21, 'Zcd', 'zettacandela')
    yottacandela = (1e+24, 'Ycd', 'yottacandela')
    decicandela = (0.1, 'dcd', 'decicandela')
    centicandela = (0.01, 'ccd', 'centicandela')
    millicandela = (0.001, 'mcd', 'millicandela')
    microcandela = (1e-06, 'μcd', 'microcandela')
    nanocandela = (1e-09, 'ncd', 'nanocandela')
    picocandela = (1e-12, 'pcd', 'picocandela')
    femtocandela = (1e-15, 'fcd', 'femtocandela')
    attocandela = (1e-18, 'acd', 'attocandela')
    zeptocandela = (1e-21, 'zcd', 'zeptocandela')
    yoctocandela = (1e-24, 'ycd', 'yoctocandela')
    hefnerkerze = (0.903, 'HK', 'Hefnerkerze')
    candlepower = (0.981, 'cp', 'candlepower')
    violle = (20.17, 'violle', 'violle')

for key, value in unit_registry.registry.items():
    print(key, value)