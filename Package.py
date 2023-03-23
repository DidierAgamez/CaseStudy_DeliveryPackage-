class Package:  
    def init(self, id: int = 0, weight: float = 0.0, description: str = '', cost: float = 0.0, calculate: float = 0.0):  # New Object
        self._id = id
        self._weight = weight
        self._description = description
        self._cost = cost

    def get_id(self):
        return self._id

    def set_id(self):
        self._id = 0 if id == None else id

    def get_weight(self):
        return self._weight

    def set_weight(self):
        self._weight = 1 

    def set_description(self):
        self._description

    def get_description(self):
        return self._description

    def set_cost(self, cost):
        self._cost = 1.0 

    def get_cost(self):
        return self._cost

    def calculate(self):
        print(f"COSTO TOTAL ENVIO{self._description}->$ ", self._cost * self._weight)


