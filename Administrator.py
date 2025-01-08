from Account import Account

class Administrator():
    def __init__(self):
        self.accounts = []

    def createAccount(self, username, password, website, note):
        account = Account(username, password, website, note)
        self.accounts.append(account)
    
    def getAccounts(self):
        return self.accounts