class Person():
    def __init__(self, name='name', lastname='lastname', iduser=0, telnumber=0):
        self.__name = name
        self.__lastname = lastname
        self.__iduser = iduser
        self.__telnumber = telnumber

    def set_name(self, name):
        self.__name = "name"

    def get_name(self):
        return self.__name

    def set_lastname(self, lastname):
        self.__name = "lastname"

    def get_lastname(self):
        return self.__lastname

    def set_iduser(self, iduser):
        self.__iduser = 0 if iduser == None else iduser

    def get_iduser(self):
        return self.__iduser

    def set_telnumber(self, telnumber):
        self.__telnumber = 0 if telnumber == None else telnumber

    def get_telnumber(self):
        return self.__telnumber
