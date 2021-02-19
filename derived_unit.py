﻿from enum import Enum
from base_unit_enums import set_dimensions, BaseUnit


def create_custom_derived_unit(unit1: BaseUnit, unit2: BaseUnit):
    new_unit = BaseUnit('CustomUnit', [('BaseCustomMultiplier', (1, 'M^2', 'square meter', 'square meter'))])
    return new_unit('M^2')


class DerivedUnit(BaseUnit):
    pass


@set_dimensions(time=-1)
class Frequency(DerivedUnit):
    hertz = (1, 'Hz', 'hertz', 'hertz')
    decahertz = (10.0, 'daHz', 'decahertz', 'decahertz')
    hectohertz = (100.0, 'hHz', 'hectohertz', 'hectohertz')
    kilohertz = (1000.0, 'kHz', 'kilohertz', 'kilohertz')
    megahertz = (1000000.0, 'MHz', 'megahertz', 'megahertz')
    gigahertz = (1000000000.0, 'GHz', 'gigahertz', 'gigahertz')
    terahertz = (1000000000000.0, 'THz', 'terahertz', 'terahertz')
    petahertz = (1000000000000000.0, 'PHz', 'petahertz', 'petahertz')
    exahertz = (1e+18, 'EHz', 'exahertz', 'exahertz')
    zettahertz = (1e+21, 'ZHz', 'zettahertz', 'zettahertz')
    yottahertz = (1e+24, 'YHz', 'yottahertz', 'yottahertz')
    decihertz = (0.1, 'dHz', 'decihertz', 'decihertz')
    centihertz = (0.01, 'cHz', 'centihertz', 'centihertz')
    millihertz = (0.001, 'mHz', 'millihertz', 'millihertz')
    microhertz = (1e-06, 'μHz', 'microhertz', 'microhertz')
    nanohertz = (1e-09, 'nHz', 'nanohertz', 'nanohertz')
    picohertz = (1e-12, 'pHz', 'picohertz', 'picohertz')
    femtohertz = (1e-15, 'fHz', 'femtohertz', 'femtohertz')
    attohertz = (1e-18, 'aHz', 'attohertz', 'attohertz')
    zeptohertz = (1e-21, 'zHz', 'zeptohertz', 'zeptohertz')
    yoctohertz = (1e-24, 'yHz', 'yoctohertz', 'yoctohertz')


@set_dimensions(mass=1, length=1, time=-2)
class Force(DerivedUnit):
    newton = (1, 'N', 'newton')
    decanewton = (10.0, 'daN', 'decanewton')
    hectonewton = (100.0, 'hN', 'hectonewton')
    kilonewton = (1000.0, 'kN', 'kilonewton')
    meganewton = (1000000.0, 'MN', 'meganewton')
    giganewton = (1000000000.0, 'GN', 'giganewton')
    teranewton = (1000000000000.0, 'TN', 'teranewton')
    petanewton = (1000000000000000.0, 'PN', 'petanewton')
    exanewton = (1e+18, 'EN', 'exanewton')
    zettanewton = (1e+21, 'ZN', 'zettanewton')
    yottanewton = (1e+24, 'YN', 'yottanewton')
    decinewton = (0.1, 'dN', 'decinewton')
    centinewton = (0.01, 'cN', 'centinewton')
    millinewton = (0.001, 'mN', 'millinewton')
    micronewton = (1e-06, 'μN', 'micronewton')
    nanonewton = (1e-09, 'nN', 'nanonewton')
    piconewton = (1e-12, 'pN', 'piconewton')
    femtonewton = (1e-15, 'fN', 'femtonewton')
    attonewton = (1e-18, 'aN', 'attonewton')
    zeptonewton = (1e-21, 'zN', 'zeptonewton')
    yoctonewton = (1e-24, 'yN', 'yoctonewton')
    
    dyne = (1e-05, 'dyne', 'dyne')
    kilopond = (9.80665, 'kp', 'kilopond')
    pound_force = (4.448222, 'lbf', 'pound-force')
    poundal = (0.138255, 'pdl', 'poundal')


@set_dimensions(mass=1, length=-1, time=-2)
class Pressure(DerivedUnit):
    pascal = (1, 'Pa', 'pascal')
    decapascal = (10.0, 'daPa', 'decapascal')
    hectopascal = (100.0, 'hPa', 'hectopascal')
    kilopascal = (1000.0, 'kPa', 'kilopascal')
    megapascal = (1000000.0, 'MPa', 'megapascal')
    gigapascal = (1000000000.0, 'GPa', 'gigapascal')
    terapascal = (1000000000000.0, 'TPa', 'terapascal')
    petapascal = (1000000000000000.0, 'PPa', 'petapascal')
    exapascal = (1e+18, 'EPa', 'exapascal')
    zettapascal = (1e+21, 'ZPa', 'zettapascal')
    yottapascal = (1e+24, 'YPa', 'yottapascal')
    decipascal = (0.1, 'dPa', 'decipascal')
    centipascal = (0.01, 'cPa', 'centipascal')
    millipascal = (0.001, 'mPa', 'millipascal')
    micropascal = (1e-06, 'μPa', 'micropascal')
    nanopascal = (1e-09, 'nPa', 'nanopascal')
    picopascal = (1e-12, 'pPa', 'picopascal')
    femtopascal = (1e-15, 'fPa', 'femtopascal')
    attopascal = (1e-18, 'aPa', 'attopascal')
    zeptopascal = (1e-21, 'zPa', 'zeptopascal')
    yoctopascal = (1e-24, 'yPa', 'yoctopascal')
    
    # TODO: bar, atm, Torr, psi


@set_dimensions(mass=1, length=2, time=-2)
class Energy(DerivedUnit):
    joule = (1, 'J', 'joule')
    decajoule = (10.0, 'daJ', 'decajoule')
    hectojoule = (100.0, 'hJ', 'hectojoule')
    kilojoule = (1000.0, 'kJ', 'kilojoule')
    megajoule = (1000000.0, 'MJ', 'megajoule')
    gigajoule = (1000000000.0, 'GJ', 'gigajoule')
    terajoule = (1000000000000.0, 'TJ', 'terajoule')
    petajoule = (1000000000000000.0, 'PJ', 'petajoule')
    exajoule = (1e+18, 'EJ', 'exajoule')
    zettajoule = (1e+21, 'ZJ', 'zettajoule')
    yottajoule = (1e+24, 'YJ', 'yottajoule')
    decijoule = (0.1, 'dJ', 'decijoule')
    centijoule = (0.01, 'cJ', 'centijoule')
    millijoule = (0.001, 'mJ', 'millijoule')
    microjoule = (1e-06, 'μJ', 'microjoule')
    nanojoule = (1e-09, 'nJ', 'nanojoule')
    picojoule = (1e-12, 'pJ', 'picojoule')
    femtojoule = (1e-15, 'fJ', 'femtojoule')
    attojoule = (1e-18, 'aJ', 'attojoule')
    zeptojoule = (1e-21, 'zJ', 'zeptojoule')
    yoctojoule = (1e-24, 'yJ', 'yoctojoule')


@set_dimensions(mass=1, length=2, time=-3)
class Power(DerivedUnit):
    watt = (1, 'W', 'watt')
    decawatt = (10.0, 'daW', 'decawatt')
    hectowatt = (100.0, 'hW', 'hectowatt')
    kilowatt = (1000.0, 'kW', 'kilowatt')
    megawatt = (1000000.0, 'MW', 'megawatt')
    gigawatt = (1000000000.0, 'GW', 'gigawatt')
    terawatt = (1000000000000.0, 'TW', 'terawatt')
    petawatt = (1000000000000000.0, 'PW', 'petawatt')
    exawatt = (1e+18, 'EW', 'exawatt')
    zettawatt = (1e+21, 'ZW', 'zettawatt')
    yottawatt = (1e+24, 'YW', 'yottawatt')
    deciwatt = (0.1, 'dW', 'deciwatt')
    centiwatt = (0.01, 'cW', 'centiwatt')
    milliwatt = (0.001, 'mW', 'milliwatt')
    microwatt = (1e-06, 'μW', 'microwatt')
    nanowatt = (1e-09, 'nW', 'nanowatt')
    picowatt = (1e-12, 'pW', 'picowatt')
    femtowatt = (1e-15, 'fW', 'femtowatt')
    attowatt = (1e-18, 'aW', 'attowatt')
    zeptowatt = (1e-21, 'zW', 'zeptowatt')
    yoctowatt = (1e-24, 'yW', 'yoctowatt')


@set_dimensions(time=1, current=1)
class ElectricCharge(DerivedUnit):
    coulomb = (1, 'C', 'coulomb')
    decacoulomb = (10.0, 'daC', 'decacoulomb')
    hectocoulomb = (100.0, 'hC', 'hectocoulomb')
    kilocoulomb = (1000.0, 'kC', 'kilocoulomb')
    megacoulomb = (1000000.0, 'MC', 'megacoulomb')
    gigacoulomb = (1000000000.0, 'GC', 'gigacoulomb')
    teracoulomb = (1000000000000.0, 'TC', 'teracoulomb')
    petacoulomb = (1000000000000000.0, 'PC', 'petacoulomb')
    exacoulomb = (1e+18, 'EC', 'exacoulomb')
    zettacoulomb = (1e+21, 'ZC', 'zettacoulomb')
    yottacoulomb = (1e+24, 'YC', 'yottacoulomb')
    decicoulomb = (0.1, 'dC', 'decicoulomb')
    centicoulomb = (0.01, 'cC', 'centicoulomb')
    millicoulomb = (0.001, 'mC', 'millicoulomb')
    microcoulomb = (1e-06, 'μC', 'microcoulomb')
    nanocoulomb = (1e-09, 'nC', 'nanocoulomb')
    picocoulomb = (1e-12, 'pC', 'picocoulomb')
    femtocoulomb = (1e-15, 'fC', 'femtocoulomb')
    attocoulomb = (1e-18, 'aC', 'attocoulomb')
    zeptocoulomb = (1e-21, 'zC', 'zeptocoulomb')
    yoctocoulomb = (1e-24, 'yC', 'yoctocoulomb')


@set_dimensions(mass=1, length=2, time=-3, current=-1)
class Voltage(DerivedUnit):
    volt = (1, 'V', 'volt')
    decavolt = (10.0, 'daV', 'decavolt')
    hectovolt = (100.0, 'hV', 'hectovolt')
    kilovolt = (1000.0, 'kV', 'kilovolt')
    megavolt = (1000000.0, 'MV', 'megavolt')
    gigavolt = (1000000000.0, 'GV', 'gigavolt')
    teravolt = (1000000000000.0, 'TV', 'teravolt')
    petavolt = (1000000000000000.0, 'PV', 'petavolt')
    exavolt = (1e+18, 'EV', 'exavolt')
    zettavolt = (1e+21, 'ZV', 'zettavolt')
    yottavolt = (1e+24, 'YV', 'yottavolt')
    decivolt = (0.1, 'dV', 'decivolt')
    centivolt = (0.01, 'cV', 'centivolt')
    millivolt = (0.001, 'mV', 'millivolt')
    microvolt = (1e-06, 'μV', 'microvolt')
    nanovolt = (1e-09, 'nV', 'nanovolt')
    picovolt = (1e-12, 'pV', 'picovolt')
    femtovolt = (1e-15, 'fV', 'femtovolt')
    attovolt = (1e-18, 'aV', 'attovolt')
    zeptovolt = (1e-21, 'zV', 'zeptovolt')
    yoctovolt = (1e-24, 'yV', 'yoctovolt')


@set_dimensions(mass=-1, length=-2, time=4, current=2)
class ElectricCapacitance(DerivedUnit):
    farad = (1, 'F', 'farad')
    decafarad = (10.0, 'daF', 'decafarad')
    hectofarad = (100.0, 'hF', 'hectofarad')
    kilofarad = (1000.0, 'kF', 'kilofarad')
    megafarad = (1000000.0, 'MF', 'megafarad')
    gigafarad = (1000000000.0, 'GF', 'gigafarad')
    terafarad = (1000000000000.0, 'TF', 'terafarad')
    petafarad = (1000000000000000.0, 'PF', 'petafarad')
    exafarad = (1e+18, 'EF', 'exafarad')
    zettafarad = (1e+21, 'ZF', 'zettafarad')
    yottafarad = (1e+24, 'YF', 'yottafarad')
    decifarad = (0.1, 'dF', 'decifarad')
    centifarad = (0.01, 'cF', 'centifarad')
    millifarad = (0.001, 'mF', 'millifarad')
    microfarad = (1e-06, 'μF', 'microfarad')
    nanofarad = (1e-09, 'nF', 'nanofarad')
    picofarad = (1e-12, 'pF', 'picofarad')
    femtofarad = (1e-15, 'fF', 'femtofarad')
    attofarad = (1e-18, 'aF', 'attofarad')
    zeptofarad = (1e-21, 'zF', 'zeptofarad')
    yoctofarad = (1e-24, 'yF', 'yoctofarad')


@set_dimensions(mass=1, length=2, time=-3, current=-2)
class ElectricResistance(DerivedUnit):
    ohm = (1, 'Ω', 'ohm')
    decaohm = (10.0, 'daΩ', 'decaohm')
    hectoohm = (100.0, 'hΩ', 'hectoohm')
    kiloohm = (1000.0, 'kΩ', 'kiloohm')
    megaohm = (1000000.0, 'MΩ', 'megaohm')
    gigaohm = (1000000000.0, 'GΩ', 'gigaohm')
    teraohm = (1000000000000.0, 'TΩ', 'teraohm')
    petaohm = (1000000000000000.0, 'PΩ', 'petaohm')
    exaohm = (1e+18, 'EΩ', 'exaohm')
    zettaohm = (1e+21, 'ZΩ', 'zettaohm')
    yottaohm = (1e+24, 'YΩ', 'yottaohm')
    deciohm = (0.1, 'dΩ', 'deciohm')
    centiohm = (0.01, 'cΩ', 'centiohm')
    milliohm = (0.001, 'mΩ', 'milliohm')
    microohm = (1e-06, 'μΩ', 'microohm')
    nanoohm = (1e-09, 'nΩ', 'nanoohm')
    picoohm = (1e-12, 'pΩ', 'picoohm')
    femtoohm = (1e-15, 'fΩ', 'femtoohm')
    attoohm = (1e-18, 'aΩ', 'attoohm')
    zeptoohm = (1e-21, 'zΩ', 'zeptoohm')
    yoctoohm = (1e-24, 'yΩ', 'yoctoohm')


@set_dimensions(mass=-1, length=-2, time=3, current=2)
class ElectricConductance(DerivedUnit):
    siemens = (1, 'S', 'siemens', 'siemens')
    decasiemens = (10.0, 'daS', 'decasiemens', 'decasiemens')
    hectosiemens = (100.0, 'hS', 'hectosiemens', 'hectosiemens')
    kilosiemens = (1000.0, 'kS', 'kilosiemens', 'kilosiemens')
    megasiemens = (1000000.0, 'MS', 'megasiemens', 'megasiemens')
    gigasiemens = (1000000000.0, 'GS', 'gigasiemens', 'gigasiemens')
    terasiemens = (1000000000000.0, 'TS', 'terasiemens', 'terasiemens')
    petasiemens = (1000000000000000.0, 'PS', 'petasiemens', 'petasiemens')
    exasiemens = (1e+18, 'ES', 'exasiemens', 'exasiemens')
    zettasiemens = (1e+21, 'ZS', 'zettasiemens', 'zettasiemens')
    yottasiemens = (1e+24, 'YS', 'yottasiemens', 'yottasiemens')
    decisiemens = (0.1, 'dS', 'decisiemens', 'decisiemens')
    centisiemens = (0.01, 'cS', 'centisiemens', 'centisiemens')
    millisiemens = (0.001, 'mS', 'millisiemens', 'millisiemens')
    microsiemens = (1e-06, 'μS', 'microsiemens', 'microsiemens')
    nanosiemens = (1e-09, 'nS', 'nanosiemens', 'nanosiemens')
    picosiemens = (1e-12, 'pS', 'picosiemens', 'picosiemens')
    femtosiemens = (1e-15, 'fS', 'femtosiemens', 'femtosiemens')
    attosiemens = (1e-18, 'aS', 'attosiemens', 'attosiemens')
    zeptosiemens = (1e-21, 'zS', 'zeptosiemens', 'zeptosiemens')
    yoctosiemens = (1e-24, 'yS', 'yoctosiemens', 'yoctosiemens')


@set_dimensions(mass=1, length=2, time=-2, current=-1)
class MagneticFlux(DerivedUnit):
    weber = (1, 'Wb', 'weber')
    decaweber = (10.0, 'daWb', 'decaweber')
    hectoweber = (100.0, 'hWb', 'hectoweber')
    kiloweber = (1000.0, 'kWb', 'kiloweber')
    megaweber = (1000000.0, 'MWb', 'megaweber')
    gigaweber = (1000000000.0, 'GWb', 'gigaweber')
    teraweber = (1000000000000.0, 'TWb', 'teraweber')
    petaweber = (1000000000000000.0, 'PWb', 'petaweber')
    exaweber = (1e+18, 'EWb', 'exaweber')
    zettaweber = (1e+21, 'ZWb', 'zettaweber')
    yottaweber = (1e+24, 'YWb', 'yottaweber')
    deciweber = (0.1, 'dWb', 'deciweber')
    centiweber = (0.01, 'cWb', 'centiweber')
    milliweber = (0.001, 'mWb', 'milliweber')
    microweber = (1e-06, 'μWb', 'microweber')
    nanoweber = (1e-09, 'nWb', 'nanoweber')
    picoweber = (1e-12, 'pWb', 'picoweber')
    femtoweber = (1e-15, 'fWb', 'femtoweber')
    attoweber = (1e-18, 'aWb', 'attoweber')
    zeptoweber = (1e-21, 'zWb', 'zeptoweber')
    yoctoweber = (1e-24, 'yWb', 'yoctoweber')


@set_dimensions(mass=1, time=-2, current=-1)
class MagneticInduction(DerivedUnit):
    tesla = (1, 'T', 'tesla')
    decatesla = (10.0, 'daT', 'decatesla')
    hectotesla = (100.0, 'hT', 'hectotesla')
    kilotesla = (1000.0, 'kT', 'kilotesla')
    megatesla = (1000000.0, 'MT', 'megatesla')
    gigatesla = (1000000000.0, 'GT', 'gigatesla')
    teratesla = (1000000000000.0, 'TT', 'teratesla')
    petatesla = (1000000000000000.0, 'PT', 'petatesla')
    exatesla = (1e+18, 'ET', 'exatesla')
    zettatesla = (1e+21, 'ZT', 'zettatesla')
    yottatesla = (1e+24, 'YT', 'yottatesla')
    decitesla = (0.1, 'dT', 'decitesla')
    centitesla = (0.01, 'cT', 'centitesla')
    millitesla = (0.001, 'mT', 'millitesla')
    microtesla = (1e-06, 'μT', 'microtesla')
    nanotesla = (1e-09, 'nT', 'nanotesla')
    picotesla = (1e-12, 'pT', 'picotesla')
    femtotesla = (1e-15, 'fT', 'femtotesla')
    attotesla = (1e-18, 'aT', 'attotesla')
    zeptotesla = (1e-21, 'zT', 'zeptotesla')
    yoctotesla = (1e-24, 'yT', 'yoctotesla')


@set_dimensions(mass=1, length=2, time=-2, current=-2)
class MagneticInductance(DerivedUnit):
    henry = (1, 'H', 'henry', 'henries')
    decahenry = (10.0, 'daH', 'decahenry', 'decahenries')
    hectohenry = (100.0, 'hH', 'hectohenry', 'hectohenries')
    kilohenry = (1000.0, 'kH', 'kilohenry', 'kilohenries')
    megahenry = (1000000.0, 'MH', 'megahenry', 'megahenries')
    gigahenry = (1000000000.0, 'GH', 'gigahenry', 'gigahenries')
    terahenry = (1000000000000.0, 'TH', 'terahenry', 'terahenries')
    petahenry = (1000000000000000.0, 'PH', 'petahenry', 'petahenries')
    exahenry = (1e+18, 'EH', 'exahenry', 'exahenries')
    zettahenry = (1e+21, 'ZH', 'zettahenry', 'zettahenries')
    yottahenry = (1e+24, 'YH', 'yottahenry', 'yottahenries')
    decihenry = (0.1, 'dH', 'decihenry', 'decihenries')
    centihenry = (0.01, 'cH', 'centihenry', 'centihenries')
    millihenry = (0.001, 'mH', 'millihenry', 'millihenries')
    microhenry = (1e-06, 'μH', 'microhenry', 'microhenries')
    nanohenry = (1e-09, 'nH', 'nanohenry', 'nanohenries')
    picohenry = (1e-12, 'pH', 'picohenry', 'picohenries')
    femtohenry = (1e-15, 'fH', 'femtohenry', 'femtohenries')
    attohenry = (1e-18, 'aH', 'attohenry', 'attohenries')
    zeptohenry = (1e-21, 'zH', 'zeptohenry', 'zeptohenries')
    yoctohenry = (1e-24, 'yH', 'yoctohenry', 'yoctohenries')


@set_dimensions(time=-1, amount=1)
class CatalyticActivity(DerivedUnit):
    katal = (1, 'kat', 'katal')
    decakatal = (10.0, 'dakat', 'decakatal')
    hectokatal = (100.0, 'hkat', 'hectokatal')
    kilokatal = (1000.0, 'kkat', 'kilokatal')
    megakatal = (1000000.0, 'Mkat', 'megakatal')
    gigakatal = (1000000000.0, 'Gkat', 'gigakatal')
    terakatal = (1000000000000.0, 'Tkat', 'terakatal')
    petakatal = (1000000000000000.0, 'Pkat', 'petakatal')
    exakatal = (1e+18, 'Ekat', 'exakatal')
    zettakatal = (1e+21, 'Zkat', 'zettakatal')
    yottakatal = (1e+24, 'Ykat', 'yottakatal')
    decikatal = (0.1, 'dkat', 'decikatal')
    centikatal = (0.01, 'ckat', 'centikatal')
    millikatal = (0.001, 'mkat', 'millikatal')
    microkatal = (1e-06, 'μkat', 'microkatal')
    nanokatal = (1e-09, 'nkat', 'nanokatal')
    picokatal = (1e-12, 'pkat', 'picokatal')
    femtokatal = (1e-15, 'fkat', 'femtokatal')
    attokatal = (1e-18, 'akat', 'attokatal')
    zeptokatal = (1e-21, 'zkat', 'zeptokatal')
    yoctokatal = (1e-24, 'ykat', 'yoctokatal')


@set_dimensions(angle=1)
class Angle(DerivedUnit):
    radian = (1, 'rad', 'radian')
    decaradian = (10.0, 'darad', 'decaradian')
    hectoradian = (100.0, 'hrad', 'hectoradian')
    kiloradian = (1000.0, 'krad', 'kiloradian')
    megaradian = (1000000.0, 'Mrad', 'megaradian')
    gigaradian = (1000000000.0, 'Grad', 'gigaradian')
    teraradian = (1000000000000.0, 'Trad', 'teraradian')
    petaradian = (1000000000000000.0, 'Prad', 'petaradian')
    exaradian = (1e+18, 'Erad', 'exaradian')
    zettaradian = (1e+21, 'Zrad', 'zettaradian')
    yottaradian = (1e+24, 'Yrad', 'yottaradian')
    deciradian = (0.1, 'drad', 'deciradian')
    centiradian = (0.01, 'crad', 'centiradian')
    milliradian = (0.001, 'mrad', 'milliradian')
    microradian = (1e-06, 'μrad', 'microradian')
    nanoradian = (1e-09, 'nrad', 'nanoradian')
    picoradian = (1e-12, 'prad', 'picoradian')
    femtoradian = (1e-15, 'frad', 'femtoradian')
    attoradian = (1e-18, 'arad', 'attoradian')
    zeptoradian = (1e-21, 'zrad', 'zeptoradian')
    yoctoradian = (1e-24, 'yrad', 'yoctoradian')


@set_dimensions(angle=2)
class SolidAngle(DerivedUnit):
    steradian = (1, 'sr', 'steradian')
    decasteradian = (10.0, 'dasr', 'decasteradian')
    hectosteradian = (100.0, 'hsr', 'hectosteradian')
    kilosteradian = (1000.0, 'ksr', 'kilosteradian')
    megasteradian = (1000000.0, 'Msr', 'megasteradian')
    gigasteradian = (1000000000.0, 'Gsr', 'gigasteradian')
    terasteradian = (1000000000000.0, 'Tsr', 'terasteradian')
    petasteradian = (1000000000000000.0, 'Psr', 'petasteradian')
    exasteradian = (1e+18, 'Esr', 'exasteradian')
    zettasteradian = (1e+21, 'Zsr', 'zettasteradian')
    yottasteradian = (1e+24, 'Ysr', 'yottasteradian')
    decisteradian = (0.1, 'dsr', 'decisteradian')
    centisteradian = (0.01, 'csr', 'centisteradian')
    millisteradian = (0.001, 'msr', 'millisteradian')
    microsteradian = (1e-06, 'μsr', 'microsteradian')
    nanosteradian = (1e-09, 'nsr', 'nanosteradian')
    picosteradian = (1e-12, 'psr', 'picosteradian')
    femtosteradian = (1e-15, 'fsr', 'femtosteradian')
    attosteradian = (1e-18, 'asr', 'attosteradian')
    zeptosteradian = (1e-21, 'zsr', 'zeptosteradian')
    yoctosteradian = (1e-24, 'ysr', 'yoctosteradian')


@set_dimensions(luminous_intensity=1, angle=2)
class LuminousFlux(DerivedUnit):
    lumen = (1, 'lm', 'lumen')
    decalumen = (10.0, 'dalm', 'decalumen')
    hectolumen = (100.0, 'hlm', 'hectolumen')
    kilolumen = (1000.0, 'klm', 'kilolumen')
    megalumen = (1000000.0, 'Mlm', 'megalumen')
    gigalumen = (1000000000.0, 'Glm', 'gigalumen')
    teralumen = (1000000000000.0, 'Tlm', 'teralumen')
    petalumen = (1000000000000000.0, 'Plm', 'petalumen')
    exalumen = (1e+18, 'Elm', 'exalumen')
    zettalumen = (1e+21, 'Zlm', 'zettalumen')
    yottalumen = (1e+24, 'Ylm', 'yottalumen')
    decilumen = (0.1, 'dlm', 'decilumen')
    centilumen = (0.01, 'clm', 'centilumen')
    millilumen = (0.001, 'mlm', 'millilumen')
    microlumen = (1e-06, 'μlm', 'microlumen')
    nanolumen = (1e-09, 'nlm', 'nanolumen')
    picolumen = (1e-12, 'plm', 'picolumen')
    femtolumen = (1e-15, 'flm', 'femtolumen')
    attolumen = (1e-18, 'alm', 'attolumen')
    zeptolumen = (1e-21, 'zlm', 'zeptolumen')
    yoctolumen = (1e-24, 'ylm', 'yoctolumen')


@set_dimensions(luminous_intensity=1, angle=2, length=-2)
class Illuminance(DerivedUnit):
    lux = (1, 'lx', 'lux', 'lux')
    decalux = (10.0, 'dalx', 'decalux', 'decalux')
    hectolux = (100.0, 'hlx', 'hectolux', 'hectolux')
    kilolux = (1000.0, 'klx', 'kilolux', 'kilolux')
    megalux = (1000000.0, 'Mlx', 'megalux', 'megalux')
    gigalux = (1000000000.0, 'Glx', 'gigalux', 'gigalux')
    teralux = (1000000000000.0, 'Tlx', 'teralux', 'teralux')
    petalux = (1000000000000000.0, 'Plx', 'petalux', 'petalux')
    exalux = (1e+18, 'Elx', 'exalux', 'exalux')
    zettalux = (1e+21, 'Zlx', 'zettalux', 'zettalux')
    yottalux = (1e+24, 'Ylx', 'yottalux', 'yottalux')
    decilux = (0.1, 'dlx', 'decilux', 'decilux')
    centilux = (0.01, 'clx', 'centilux', 'centilux')
    millilux = (0.001, 'mlx', 'millilux', 'millilux')
    microlux = (1e-06, 'μlx', 'microlux', 'microlux')
    nanolux = (1e-09, 'nlx', 'nanolux', 'nanolux')
    picolux = (1e-12, 'plx', 'picolux', 'picolux')
    femtolux = (1e-15, 'flx', 'femtolux', 'femtolux')
    attolux = (1e-18, 'alx', 'attolux', 'attolux')
    zeptolux = (1e-21, 'zlx', 'zeptolux', 'zeptolux')
    yoctolux = (1e-24, 'ylx', 'yoctolux', 'yoctolux')


@set_dimensions(length=2, time=-2)
class AbsorbedDose(DerivedUnit):
    gray = (1, 'Gy', 'gray')
    decagray = (10.0, 'daGy', 'decagray')
    hectogray = (100.0, 'hGy', 'hectogray')
    kilogray = (1000.0, 'kGy', 'kilogray')
    megagray = (1000000.0, 'MGy', 'megagray')
    gigagray = (1000000000.0, 'GGy', 'gigagray')
    teragray = (1000000000000.0, 'TGy', 'teragray')
    petagray = (1000000000000000.0, 'PGy', 'petagray')
    exagray = (1e+18, 'EGy', 'exagray')
    zettagray = (1e+21, 'ZGy', 'zettagray')
    yottagray = (1e+24, 'YGy', 'yottagray')
    decigray = (0.1, 'dGy', 'decigray')
    centigray = (0.01, 'cGy', 'centigray')
    milligray = (0.001, 'mGy', 'milligray')
    microgray = (1e-06, 'μGy', 'microgray')
    nanogray = (1e-09, 'nGy', 'nanogray')
    picogray = (1e-12, 'pGy', 'picogray')
    femtogray = (1e-15, 'fGy', 'femtogray')
    attogray = (1e-18, 'aGy', 'attogray')
    zeptogray = (1e-21, 'zGy', 'zeptogray')
    yoctogray = (1e-24, 'yGy', 'yoctogray')