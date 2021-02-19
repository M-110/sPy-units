from base_unit_enums import Time, Length, Mass, Current, Temperature, Amount, LuminousIntensity
import unittest


def run_tests(test_class):
    suite = unittest.TestLoader().loadTestsFromTestCase(test_class)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)


class TestEnum(unittest.TestCase):
    def test_time_conversions(self):
        self.assertEqual(
            Time.hour.convert(21, Time.hour),
            21
        )
        self.assertEqual(
            Time.minute.convert(21, Time.second),
            60 * 21
        )
        self.assertEqual(
            Time.hour.convert(21, Time.minute),
            60 * 21
        )
        self.assertEqual(
            Time.day.convert(6, Time.hour),
            24 * 6
            
        )
        self.assertEqual(
            Time.week.convert(6, Time.day),
            6 * 7
        )
        # TODO: Add day/week/year conversion tests
        
    def test_length_conversions(self):
        self.assertEqual(
            Length.meter.convert(6, Length.kilometer))
    
    def test_length_conversions(self):
        pass
        
        
    # def test_enum_creation(self):
    #     insufficient_supplies = AppStatus.InsufficientSupplies
    #     timeout = AppStatus.Timeout
    #     protected = AppStatus.Protected
    #     not_an_integer = AppStatus.NotAnInteger
    # 
    # def test_lookup_by_name(self):
    #     self.assertEqual(AppStatus.InsufficientSupplies, AppStatus['InsufficientSupplies'])
    #     self.assertEqual(AppStatus.Timeout, AppStatus['Timeout'])
    #     self.assertEqual(AppStatus.Protected, AppStatus['Protected'])
    #     self.assertEqual(AppStatus.NotAnInteger, AppStatus['NotAnInteger'])
    # 
    # def test_throws(self):
    #     with self.assertRaises(InsufficientSuppliesException):
    #         AppStatus.InsufficientSupplies.throw()
    # 
    #     with self.assertRaises(Timeout):
    #         AppStatus.Timeout.throw()
    # 
    #     with self.assertRaises(ProtectedException):
    #         AppStatus.Protected.throw()
    # 
    #     with self.assertRaises(ValueError):



run_tests(TestEnum)
