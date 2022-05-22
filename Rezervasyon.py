from abc import ABC, abstractmethod
import pypyodbc

class LogDatabase(ABC):
    db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-F95I3O2\SQLEXPRESS;'
    'Database=rezervasyon;'
    'Trusted_Connection=True;'  
)
  


class AbstractRezervasyonClass(ABC):
    
    def __init__(self,date):
       
        self.date=date
        
 
        
        
        
    @abstractmethod
    def makeRezervasyon(self):
        pass
   
 

class OnOdemeliRezervasyonService(AbstractRezervasyonClass):
    def __init__(self, date):
        super().__init__(date)
        self.price=200
    def makeRezervasyon(self):
         commands = 'INSERT INTO  VALUES(?,?,?,?,?)'

