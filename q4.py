#Q4. Create a Temperature class. Make two methods :
     # a. convertFahrenheit - It will take Celsius and will print it into Fahrenheit.
      #b. convertCelsius - It will take Fahrenheit and will convert it into Celsius.

class Temperature():


    def __init__(self,fahrenheit,celsius):
        self.fahrenheit=fahrenheit
        self.celsius=celsius


    def convertFahrenheit(self):
        return ((self.celsius * 9) / 5)+ 32


    def convertCelsius(self):
        return ((self.fahrenheit-32) * 5) / 9

Temp=Temperature(100,36)
print(Temp.convertCelsius())
print(Temp.convertFahrenheit())