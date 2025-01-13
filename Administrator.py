from Account import Account
from os import mkdir, getcwd
from os.path import exists
from json import dumps

class Administrator():
    def __init__(self):
        self.accounts = []

    def createAccount(self, username, password, website, note):
        account = Account(username, password, website, note)
        self.accounts.append(account)
    
    def getAccounts(self):
        return self.accounts
    
    def searchUsername(self, username):
        for account in self.accounts:
            if account.getUsername() == username:
                return account
        return False
    
    def saveAccounts(self):
        source = getcwd()
        ddbb = "/DDBB"
        path = source + ddbb
        file = '/claves.json'
        
        
        if not exists(path):
            mkdir(path)
            print("Folder created")
        
        dictAccounts = [account.__dict__ for account in self.accounts]
        
        with open(path+file, 'w', encoding='utf-8') as jsonfile:
            
            jsonData = dumps(dictAccounts)
            jsonfile.write(jsonData)
        jsonfile.close()

    def importAccounts(self):
        pass