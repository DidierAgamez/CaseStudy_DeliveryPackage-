import Package

class OverWeightPackage(Package):

    def _init_(self, id=0, weight=1.0, description="Description", cost=1.0,overweight=1.0):
        super().__init__(id, weight, description, cost)
        self.__overweight = 1.0 if overweight == 0.0 else overweight

    def calculate(self):
        print(f"Cost of delivery with OverWeight {self._description} is $ ",
              (self.__overweight + self.__overweight) * self._cost)
