def convertKelvinToCelsius(kval):
    kval = float(kval)
    Celsius = kval - 273.15
    return (round(Celsius, 2))


def convertKelvinToFahrenheit(kval):
    kval = float(kval)
    Fahrenheit = kval * 9/5 - 459.67
    return (round(Fahrenheit, 2))


def convertFahrenheitToKelvin(fvalb):
    Kelvin = ((float(fvalb)) + 459.67) * (5/9)
    return (round(Kelvin, 2))


def convertFahrenheitToCelsius(fval):
    fval = float(fval)
    Celsius = (fval - 32) / 1.8
    return float(round(Celsius, 2))


def convertCelsiusToFahrenheit(cval):
    cval = float(cval)
    Fahrenheit = cval * 1.8 + 32
    return Fahrenheit


def convertCelsiusToKelvin(cval):
    Kelvin = (float(cval)) + 273.15
    return Kelvin
    
    
def convert(fromUnit, toUnit, value):
    if fromUnit == 'Celsius' and toUnit == 'Kelvin':
        convertCelsiusToKelvin(value)
    elif fromUnit == 'Celsius' and toUnit == 'Fahrenheit':
        convertCelsiusToFahrenheit(value)
    elif fromUnit == 'Fahrenheit' and toUnit == 'Celsius':
        convertFahrenheitToCelsius(value)
    elif fromUnit == 'Fahrenheit' and toUnit == 'Kelvin':
        convertFahrenheitToKelvin(value)
    elif fromUnit == 'Kelvin' and toUnit == 'Fahrenheit':
        convertKelvinToFahrenheit(value)
    elif fromUnit == 'Kelvin' and toUnit == 'Celsius':
        convertKelvinToCelsius(value)
