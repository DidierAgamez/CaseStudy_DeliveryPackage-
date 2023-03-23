class Address():

    def __init__(self, house_number=0, kind_street="kind of street", street_name="street name", address=0, postal_code=0):
        self.__house_number = 0 if house_number == None else house_number
        self.__kind_street = "kind of street" if kind_street == None else kind_street
        self.__street_name = "street name " if street_name == None else street_name
        self.__address = 0 if address == None else address
        self.__postal_code = 0 if postal_code == None else postal_code

    def set_house_number(self, house_number):
        self.__house_number = "number" if house_number == None else house_number

    def get_house_number(self):
        return self.__house_number

    def set_kind_street(self, kind_street):
        self.__kind_street = "kind of street" if kind_street == None else kind_street

    def get_kind_street(self):
        return self.__kind_street

    def set_street_name(self, street_name):
        self.__street_name = "street name " if street_name == None else street_name

    def get_street_name(self):
        return self.__street_name

    def set_address(self, address):
        self.__address = 0 if address == None else address

    def get_address(self):
        return self.__address

    def set_postal_code(self, postal_code):
        self.__postal_code = 0 if postal_code == None else postal_code

    def get_postal_code(self):
        return self.__postal_code
