from datetime import datetime

class TIME(object):
    def Years(self):
        self.now = datetime.now()
        self.years = str(self.now.day) + '/' + str(self.now.month) + '/' +  str(self.now.year)
        
        return self.years

    def Hors(self):
        self.now = datetime.now()
        self.hors = str(self.now.hour) + '-' + str(self.now.minute)
        
        return self.hors
