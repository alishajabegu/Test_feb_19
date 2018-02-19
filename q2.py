#Q2. Create a class Circle which has a class variable PI with the value=22/7.
# Make two methods getArea and getCircumference inside this Circle class.
# Which when invoked returns area and circumference of each circle instances.


class Circle:
    pi=22/7

    def __init__(self,radius):
       self.radius=radius


    def getArea(self):
        self.area=Circle.pi*self.radius
        return self.area

    def getCircumference(self):
        self.circumference=2*Circle.pi*self.radius
        return self.circumference

C=Circle(10)
print(C.getArea())
print(C.getCircumference())
