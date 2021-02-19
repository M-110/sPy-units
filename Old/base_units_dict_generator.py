# region Define SI Units
metric_dict = {
    '': (1, ''),
    'deca': (1E1, 'da'),
    'hecto': (1E2, 'h'),
    'kilo': (1E3, 'k'),
    'mega': (1E6, 'M'),
    'giga': (1E9, 'G'),
    'tera': (1E12, 'T'),
    'peta': (1E15, 'P'),
    'exa': (1E18, 'E'),
    'zetta': (1E21, 'Z'),
    'yotta': (1E24, 'Y'),

    'deci': (1E-1, 'd'),
    'centi': (1E-2, 'c'),
    'milli': (1E-3, 'm'),
    'micro': (1E-6, 'μ'),
    'nano': (1E-9, 'n'),
    'pico': (1E-12, 'p'),
    'femto': (1E-15, 'f'),
    'atto': (1E-18, 'a'),
    'zepto': (1E-21, 'z'),
    'yocto': (1E-24, 'y'),
}

si_time = {
    prefix + 'second': (value, abbreviation + 's', prefix + 'second')
    for prefix, (value, abbreviation) in metric_dict.items()
}

si_length = {
    prefix + 'meter': (value, abbreviation + 'm', prefix + 'meter')
    for prefix, (value, abbreviation) in metric_dict.items()
}

si_mass = {
    'gram': (1E-3, 'g', 'gram'),
    'decagram': (1E-2, 'dag', 'decagram'),
    'hectogram': (1E-1, 'hg', 'hectogram'),
    'kilogram': (1, 'kg', 'kilogram'),
    'megagram': (1E3, 'Mg', 'megagram'),
    'gigagram': (1E6, 'Gg', 'gigagram'),
    'teragram': (1E9, 'Tg', 'teragram'),
    'petagram': (1E12, 'Pg', 'petagram'),
    'exagram': (1E15, 'Eg', 'exagram'),
    'zettagram': (1e+18, 'Zg', 'zettagram'),
    'yottagram': (1e+21, 'Yg', 'yottagram'),

    'decigram': (1E-4, 'dg', 'decigram'),
    'centigram': (1E-05, 'cg', 'centigram'),
    'milligram': (1E-06, 'mg', 'milligram'),
    'microgram': (1E-09, 'μg', 'microgram'),
    'nanogram': (1E-12, 'ng', 'nanogram'),
    'picogram': (1E-15, 'pg', 'picogram'),
    'femtogram': (1E-18, 'fg', 'femtogram'),
    'attogram': (1E-21, 'ag', 'attogram'),
    'zeptogram': (1E-24, 'zg', 'zeptogram'),
    'yoctogram': (1E-27, 'yg', 'yoctogram')
}

si_current = {
    prefix + 'ampere': (value, abbreviation + 'A', prefix + 'ampere')
    for prefix, (value, abbreviation) in metric_dict.items()
}

si_temperature = {
    prefix + 'kelvin': (value, abbreviation + 'K', prefix + 'kelvin')
    for prefix, (value, abbreviation) in metric_dict.items()
}

si_amount = {
    prefix + 'mole': (value, abbreviation + 'mol', prefix + 'mole')
    for prefix, (value, abbreviation) in metric_dict.items()
}

si_intensity = {
    prefix + 'candela': (value, abbreviation + 'cd', prefix + 'candela')
    for prefix, (value, abbreviation) in metric_dict.items()
}
# endregion

# region Define non-SI units

other_time = {
    'planck_time': (5.39E-44, 'tP', 'Planck time'),
    'jiffy': (3E-24, 'j', 'jiffy', 'jiffies'),
    'minute': (60, 'min', 'minute'),
    'hour': (3600, 'h', 'hour'),
    'day': (86_400, 'd', 'day'),
    'week': (604_800, 'week', 'week'),
    'fortnight': (1_209_600, 'fortnight', 'fortnight'),
    'month': (2.628E6, 'mo', 'month'),
    'year': (3.154E7, 'yr', 'year'),
    'decade': (3.156E8, 'decade', 'decade'),
    'century': (3.156E9, 'century', 'century', 'centuries'),
    'millennium': (3.156E10, 'millennium', 'millennium', 'millennia'),
    'galactic_year': (7.49E15, 'galactic year', 'galactic year'),
    'aeon': (3.154E16, 'aeon', 'aeon')
}

other_length = {
    'angstrom': (1E-10, 'Å', 'angstrom'),
    'inch': (0.0254, 'in', 'inch', 'inches'),
    'foot': (.3048, 'ft', 'foot', 'feet'),
    'yard': (.9144, 'yd', 'yard'),
    'mile': (1609, 'mi', 'mile'),
    'league': (4828, 'league', 'league'),
    'fathom': (1.829, 'fathom', 'fathom'),
    'nautical_mile': (1852, 'nmi', 'nautical mile'),
    'rod': (5.029, 'rod', 'rod'),
    'chain': (20.12, 'chain', 'chain'),
    'earth_radius': (6.378E6, 'R⊕', 'Earth radius', 'Earth radii'),
    'lunar_distance': (4.034E8, 'LD', 'Lunar distance'),
    'astronomical_unit': (1.496E11, 'au', 'astronomical unit'),
    'light_year': (9.461E12, 'ly', 'light-year'),
    'parsec': (3.086E16, 'pc', 'parsec'),
    'kiloparsec': (3.086E19, 'kpc', 'kiloparsec'),
    'megaparsec': (3.086E22, 'Mpc', 'megaparsec'),
    'gigaparsec': (3.086E25, 'Gpc', 'gigaparsec'),
    'hubble_length': (1.4E26, 'cH0', 'Hubble length'),

    'electron_radius': (2.81794033E-15, 'r0', 'electron radius', 'electron radii'),
    'bohr_radius': (5.29177211E-11, 'a0', 'Bohr radius', 'Bohr radii'),
    'planck_length': (1.6163E-35, 'ℓP', 'Planck length')
}

other_mass = {
    'tonne': (1E3, 't', 'tonne'),
    'short_ton': (907.2, 'sh tn', 'short ton'),
    'long_ton': (1016, 'lg tn', 'long ton'),
    'atomic_mass_unit': (1.66053907E-27, 'u', 'atomic mass unit'),
    'slug': (14.59, 'sl', 'slug'),
    'grain': (6.48E-5, 'gr', 'grain'),
    'ounce': (0.02835, 'oz', 'ounce'),
    'stone': (6.35, 'st', 'stone'),
    'pound': (0.4536, 'lb', 'pound'),
    'planck_mass': (2.1764E-8, 'mP', 'Planck mass', 'Planck masses'),
    'solar_mass': (1.988435E30, 'M☉', 'solar mass', 'solar masses')
}

other_current = {
    'abampere': (10, 'aA', 'abampere'),
}

other_temperature = {
    'fahrenheit': (2, '°F', 'Fahrenheit', 'Fahrenheit'),
    'celsius':  (3, '°C', 'Celsius', 'Celsius')
    
}

other_amount = {
    'atom': (6.022E23, 'atom', 'atom')
}

other_intensity = {
    'hefnerkerze': (0.903, 'HK', 'Hefnerkerze'),
    'candlepower': (0.981, 'cp', 'candlepower'),
    'violle': (20.17, 'violle', 'violle')
}

# endregion


unit_dict = {
    'time': {**si_time, **other_time},
    'length': {**si_length, **other_length},
    'mass': {**si_mass, **other_mass},
    'current': {**si_current, **other_current},
    'temperature': {**si_temperature, **other_temperature},
    'amount': {**si_amount, **other_amount},
    'intensity': {**si_intensity, **other_intensity}
}

for name, dic in unit_dict.items():
    print(name)
    for key, value in dic.items():
        print(f'{key} = {value}')
    print('\n')