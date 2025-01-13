from os import system
from Administrator import Administrator
class App():
    
    def __init__(self):
        self.administrator = Administrator()
        self.valid = True

    def lobby(self):
        while True:
            system('clear')
            print("==== PassManager ====")
            print("0. Salir")
            print("1. Crear cuenta")
            print("2. Listar cuentas")
            print("3. Ingresar en cuenta")
            response = str(input("\nElige una opción: "))

            if response == '0':
                self.administrator.saveAccounts()
                self.valid = False
                break
            elif response == '1':
                self.createAccount()
            
            elif response == '2':
                self.listAccounts()

            elif response == '3':
                self.showAccount()

    
    def createAccount(self):
        while True:
            system('clear')
            print("==== PassManager ====")
            print("==== Crear Cuenta ====")
            username = str(input("Nombre de usuario: "))
            password = str(input("Password: "))
            website = str(input("Sitio web: "))
            note = str(input("Notas: "))

            if len(username) != 0 or len(password) != 0 or len(website) != 0:
                self.administrator.createAccount(username, password, website, note)
                break
    
    def listAccounts(self):
        while True:
            system('clear')
            print("==== PassManager ====")
            print("==== Lista de Cuentas ====")
            for index, account in enumerate(self.administrator.getAccounts()):
                print("Id  Username   Website")
                print(f'{index}. {account.getUsername()} {account.getWebsite()}')
            
            
            response = str(input("\nEnter para salir "))
            if len(response) == 0:
                break
    
    def showAccount(self):
        while True:
            system('clear')
            print("==== PassManager ====")
            print("==== Cuenta ====")
            request = str(input("Nombre de usuario: "))
            account = self.administrator.searchUsername(request)

            if account:
                print(f"Username: {account.getUsername()}")
                print(f"Password: {account.getPassword()}")
                print(f"Web site: {account.getWebsite()}")
                print(f"Notas:    {account.getNote()}")

                response = str(input("\n¿Desea modificar algún campo? (y/n): "))
                if response == 'y':
                    account.setUsername(str(input("Username: ") or account.getUsername()))
                    account.setPassword(str(input("Password: ") or account.getPassword()))
                    account.setWebsite(str(input("Web site: ") or account.getWebsite()))
                    account.setNote(str(input("Nota: ") or account.getNote()))
                    pass

                input("\nEnter para salir ")

                break
                
            print("\nUsuario no encontrado")
            response = str(input("Enter para continuar\n0. Para salir\n"))
            if response == '0':
                break



    def getValid(self):
        return self.valid