from Account import Account

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