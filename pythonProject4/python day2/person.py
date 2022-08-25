class person:
    def __init__(self, firstname, lastname, adress):
        self.firstname=firstname
        self.lastname=lastname
        self.adress =adress
    def getfullname(self):
        return self.firstname +' '+self.lastname+" " +self.adress
    def getinitials(self):
        return self.firstname[0] + self.lastname[0]



