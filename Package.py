class Package(object):

    def __init__(self, id=0, weight=1.0, description="Description", cost=1.0):
        self._id = 0 if id == None else id
        self._weight = 1 if weight == 0 else weight
        self._description = 'description' if 'description' == None else description
        self._cost = 1.0 if cost == 0.0 else cost

    def get_id(self):
        return self._id

    def set_id(self, id):
        self._id = 0 if id == None else id

    def get_weight(self, weight):
        return self._weight

    def set_weight(self, weight):
        self._weight = 1 if weight == 0 else weight

    def set_description(self, description):
        self._description = 'description' if 'description' == None else description

    def get_description(self):
        return self._description

    def set_cost(self, cost):
        self._cost = 1.0 if cost == 0.0 else cost

    def get_cost(self):
        return self._cost

    def calculate(self):
        print(f"Cost of delivery {self._description} is $ ",
              self._cost * self._weight)
