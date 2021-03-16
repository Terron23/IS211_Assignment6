import sys
#sys.path.append("")
import unittest
import conversions

class Testconversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        test = {"40C":"313.15K", "-50C":"223.15K", "0C":"273.15K" }
        for key in test:
            self.assertEqual(conversions.convertCelsiusToKelvin(key), test[key])
            print("Test is Successful! {0} = {1}".format(key, test[key]))

        
    def test_convertCelsiusToFahrenheit(self):
        test = {"0C":"32F", "-50C":"-58F", "200C":"392F" }
        for key in test:
            self.assertEqual(conversions.convertCelsiusToKelvin(key), test[key])
            print("Test is Successful! {0} = {1}".format(key, test[key]))

        
    def test_convertFahrenheitToCelsius(self):
        self.assertEqual(conversions.convertFahrenheitToCelsius(0), -17.78)
        print("Test is Successful! 0F = -17.78C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(50), 10)
        print("Test is Successful! 50F = 10C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(212), 100)
        print("Test is Successful! 212F = 100C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(130), 54.44)
        print("Test is Successful! 130F = 54.44C")
        self.assertEqual(conversions.convertFahrenheitToCelsius(-40), -40)
        print("Test is Successful! -40F = -40C")
        
    def test_convertFahrenheitToKelvin(self):
        self.assertEqual(conversions.convertFahrenheitToKelvin(110), 316.48)
        print("Test is Successful! 30F = 272.04K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(-20), 244.26)
        print("Test is Successful! -20F = 244.26K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(1000), 810.93)
        print("Test is Successful! 1000F = 810.93K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(-459.67), 0)
        print("Test is Successful! -459.67F = 0K")
        self.assertEqual(conversions.convertFahrenheitToKelvin(100), 310.93)
        print("Test is Successful! 100F = 310.93K")
        
    def test_convertKelvinToFahrenheit(self):
        self.assertEqual(conversions.convertKelvinToFahrenheit(200), -99.67)
        print("Test is Successful! 200K = -99.67F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(50), -369.67)
        print("Test is Successful! 10K = -441.67F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(1000), 1340.33)
        print("Test is Successful! 1000K = 1340.33F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(500), 440.33)
        print("Test is Successful! 500K = 440.33F")
        self.assertEqual(conversions.convertKelvinToFahrenheit(260), 8.33)
        print("Test is Successful! 260K = 8.33F")
        
    def test_convertKelvinToCelsius(self):
        self.assertEqual(conversions.convertKelvinToCelsius(150), -123.15)
        print("Test is Successful! 150K = -123.15C")
        self.assertEqual(conversions.convertKelvinToCelsius(270), -3.15)
        print("Test is Successful! 270K = -3.15C")
        self.assertEqual(conversions.convertKelvinToCelsius(400), 126.85)
        print("Test is Successful! 400K = 126.85C")
        self.assertEqual(conversions.convertKelvinToCelsius(600), 326.85)
        print("Test is Successful! 600K = 326.85C")
        self.assertEqual(conversions.convertKelvinToCelsius(90), -183.15)
        print("Test is Successful! 90K = -183.15C")

        
if __name__ == "__main__":
    unittest.main()
