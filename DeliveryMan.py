class DeliveryMan(Person):

    def __init__(self, name='name', lastname='lastname', dni=0, phone=0, id=0, date='00/00/00', time='00:00', sender=Person(), receiver=Person(), sender_add=Address, receiver_add=Address(), contact=Person(), items=[Package()]):
        super().__init__(name, lastname, dni, phone)
        self.__id = 0 if id == None else id

        self.__date = "00/00/00" if date == None else date
        self.__time = "00:00" if time == None else time
        self.__sender = Person() if sender == None else sender
        self.__receiver = Person() if receiver == None else receiver

        self.__sender_add = Address() if sender_add == None else sender_add
        self.__receiver_add = Address() if receiver_add == None else receiver_add
        self.__contact = Person() if contact == None else contact
        self.__items = [Package()] if items == None else items

    def set_id(self, id):
        self.__id = 0 if id == None else id

    def get_id(self):
        return self.__id

    def set_date(self, date):
        self.__date = "00/00/00" if date == None else date

    def get_date(self):
        return self.__date

    def set_time(self, time):
        self.__time = "00:00" if time == None else time

    def get_time(self):
        return self.__time

    def set_sender(self, sender):
        self.__sender = Person( ) if sender == None else sender

    def get_sender(self):
        return self.__sender

    def set_receiver(self, receiver):
        self.__receiver = Person() if receiver == None else receiver

    def get_receiver(self):
        return self.__receiver

    def set_sender_add(self, sender_add):
        self.__sender_add = Address if sender_add == None else sender_add

    def get_sender_add(self):
        return self.__sender_add

    def set_receiver_add(self, receiver_add):
        self.__receiver_add = Address if receiver_add == None else receiver_add

    def get_receiver_add(self):
        return self.__receiver_add

    def set_contact(self, contact):
        self.__contact = Person if contact == None else contact

    def get_contact(self):
        return self.__contact

    def set_items(self, items):
        self.__items = [Package] if items == None else items

    def get_items(self):
        return self.__items
