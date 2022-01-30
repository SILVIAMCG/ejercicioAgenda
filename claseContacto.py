class Contacto:
    def __init__(self,nombre="",telefono=None,email=""):
        #estos argumentos se asignan a los atributos
        self._nombre=nombre
        self._telefono=telefono
        self._email=email
    #estos metodos estan explicados en la clase agenda
    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self,valor):
        self._nombre=valor

    @nombre.deleter
    def nombre(self):
        del self._nombre

    @property
    def telefono(self):
        return self._telefono

    @telefono.setter
    def telefono(self,valor):
        self._telefono=valor

    @telefono.deleter
    def telefono(self):
        del self._telefono

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self,valor):
        self._email=valor

    @email.deleter
    def email(self):
        del self._email


    #metodo para imprimir la informacion
    def __str__(self):
        return f'''Nombre: {self.nombre} Telefono: {self.telefono} Email: {self.email}'''












        
