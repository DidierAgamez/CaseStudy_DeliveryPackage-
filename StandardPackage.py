import Package

class StandardPackage(Package):

    def __init__(self, id=0, weight=1.0, description="Description", cost=1.0, overweight=1.0, fixedfee=1.0):
        super().__init__(id, weight, description, cost)
        self.__fixedfee = 1.0 if fixedfee == 0.0 else fixedfee

    def calculate(self):
        print(f"Cost of delivery {self._description} is $ ",
              (self.__fixedfee + self._cost) * self._weight)
