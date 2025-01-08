from cryptography.fernet import Fernet

class Account():
    def __init__(self, username, password, website, note):
        self.username = username
        self.password = password
        self.website = website
        self.note = note

    def setUsername(self, username):
        self.username = username
    
    def setPassword(self, password):
        self.password = password
    
    def setWebsite(self, website):
        self.website = website
    
    def setNote(self, note):
        self.note = note

    def getUsername(self):
        return self.username
    
    def getPassword(self):
        return self.password
    
    def getWebsite(self):
        return self.website
    
    def getNote(self):
        return self.note
    
