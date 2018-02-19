#Q1. Create a RectangleGeometry class which takes in length and breadth as initialize parameter. Make two methods getArea
#and getPerimeter inside this class. Which when invoked returns area and perimeter of each rectangle instance.


class RectangleGeometry():

   def __int__(self,length,breadth):
      self.length = length
      self.breadth = breadth


   def getArea(self):
      self.area=self.length * self.breadth
      return self.area


   def getPerimeter(self):
      self.peri = 2*(self.length + self.breadth)
      return self.peri

R=RectangleGeometry(8,12)
print(R.getArea())
print(R.getPerimeter())




