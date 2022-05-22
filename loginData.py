import pypyodbc
from abc import ABC,abstractmethod
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-F95I3O2\SQLEXPRESS;'
    'Database=rezervasyon;'
    'Trusted_Connection=True;'  
)

imlec = db.cursor()





class UserLoginService:
    

    def AddUser(self,name,lastname,email,phone,password):
       
        commands = 'INSERT INTO People VALUES(?,?,?,?,?)'
        data = (name,lastname,email,phone,password)

        imlec.execute(commands,data)
        imlec.commit()
    
    def authUser(self,em,password):
        
        imlec.execute('SELECT email,password,name,id FROM People')
        user=imlec.fetchall()
        for i in user:
            if i[0]==em and i[1]==password:
                print(f"\n{50*' '}Hosgeldiniz {i[2]}")
                return id
        return False

        
            

         
     
        
        
        

        