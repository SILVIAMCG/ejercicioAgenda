from claseContacto import Contacto
import os

#definir el menu dentro de la clase
class Agenda:
    OPC_AÑADIR_CONTACTO = 1
    OPC_LISTA_DE_CONTACTOS = 2
    OPC_BUSCAR_CONTACTO = 3
    OPC_EDITAR_CONTACTO = 4
    OPC_CERRAR_AGENDA = 0

    #inicializar lista de contactos que ira dentro de la agenda
    def __init__ (self):
        self.contactos=[]

    #metodo para imprimir cada atributo
    def __str__(self):
        c= f"                     Contactos: \n"
        for contacto in self.contactos:
            c += f"{nombre}\n"
            c += f"{telefono}\n"
            c += f"{email}\n"
        return c
    
    #property se usa como un getter
    @property
    def nombre(self):
        return self._nombre
    #setter asigna un valor al parametro
    @nombre.setter
    def nombre(self,valor):
        self._nombre=valor
    #deleter borra el atributo en caso de ser necesario
    @nombre.deleter
    def nombre(self):
        del self._nombre

    #los mismos metodos aplican para cada atributo

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

    #metodo para imprimir opciones del menu
    def menu(self):
        #inicializar para volver al menu 
        continuar=True
        while continuar:
            #esto limpia la pantalla, por alguna razon no funciona
            os.system('cls')
      #se imprime el menu definido al principio de la clase
            print (f'''
     {self.OPC_AÑADIR_CONTACTO} Añadir contacto
     {self.OPC_LISTA_DE_CONTACTOS} Lista de contactos
     {self.OPC_BUSCAR_CONTACTO} Buscar contacto
     {self.OPC_EDITAR_CONTACTO} Editar contacto
     {self.OPC_CERRAR_AGENDA} Cerrar agenda
     ''')
            #se piden los datos de las opciones a seleccionar, y depende de lo
            #seleccionado se ejecuta cada metodo
            opc=int(input("Selecciona una opcion: "))
            if opc== self.OPC_AÑADIR_CONTACTO:
                self.agnadirContacto()
            elif opc==self.OPC_LISTA_DE_CONTACTOS:
                self.listaContactos()
            elif opc==self.OPC_BUSCAR_CONTACTO:
                self.buscarContacto()
            elif opc==self.OPC_EDITAR_CONTACTO:
                self.editarContacto()
            elif opc==self.OPC_CERRAR_AGENDA:
                #si cierra la agenda se termina el ciclo
                continuar=False
                print("Nos vemos")
                break
               

            else:
                print("Opcion no valida")
            #esto es para volver al menu
            input("Presiona enter para continuar")

    #    print("Nos vemos")

    #funcion que añade los contactos

    def agnadirContacto(self):
        continuar=True
        while continuar:
            os.system('cls')
            #se piden los datos
            nombre= input("Nombre: ")
            telefono=int(input("Telefono: "))
            email=input("Email: ")
            #se llama al objeto de la clase contacto, y se almacena dentro de una lista
            contacto=Contacto(nombre,telefono,email)
            #se añade la lista a la lista de contactos
            self.contactos.append(contacto)
            #opcion para agregar mas contactos, si la respuesta es distinta de si, se deja
            #de ejecutar el ciclo
            respuesta=input("¿Desea agregar otro contacto? (s/n)")
            if respuesta != "s" and respuesta!= "S":
                continuar=False

    #metodo para mostrar la lista de contactos, hay un error

    def listaContactos(self):
        os.system("cls")
        print("                         Contactos")
        if len(self.contactos)==0:
            print("No hay contactos registrados")
        else:
            for i in self.contactos:
                print(f"{i}")

    #metodo para buscar contacto
    def buscarContacto(self):
        continuar=True
        while continuar:
            os.system('cls')
            nombre=input("Ingrese nombre: ")
            #cont es cada contacto de la lista
            for cont in self.contactos:
                if cont.nombre == nombre:
                    print(cont)
            respuesta=input("¿Desea buscar otro contacto? (s/n)")
            if respuesta != "s" and respuesta!= "S":
                continuar=False

    def editarContacto(self):
        continuar=True
        while continuar:
            os.system('cls')
            nombre=input("Ingrese nombre del contacto a editar: ")
            #cont es cada contacto de la lista
            for cont in self.contactos:
                if cont.nombre == nombre:
                   cont.nombre=input("Ingrese nuevo nombre: ")
                   cont.telefono=int(input("Ingrese nuevo telefono: "))
                   cont.email=input("Ingrese nuevo email: ")                                           
            respuesta=input("¿Desea editar otro contacto? (s/n)")
            if respuesta != "s" and respuesta!= "S":
                continuar=False

    
