import pypyodbc,csv
from pay import *
from abc import ABC,abstractmethod
import pandas as pd
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-F95I3O2\SQLEXPRESS;'
    'Database=rezervasyon;'
    'Trusted_Connection=True;'  
)


imlec = db.cursor()

class Admin:
    @staticmethod
    def beklenenDolulukOran():
        onOdeme=imlec.execute('SELECT name,surname,rezarvasyonTarihi,odendi FROM OnOdemeli WHERE rezarvasyonTarihi<30')
        res=imlec.fetchall()
        
        with open("beklenenDoluluk.csv","w")as file:
            for row in res:
                csv.writer(file).writerow(row)
            
            
            
    @staticmethod
    def beklenenOdaGeliri():
        imlec.execute('SELECT rezervasyonUcreti FROM OnOdemeli ')
        res=imlec.fetchall()
        with open("beklenenOdaGeliri.csv","w")as file:
            toplam=0
            for row in res:
                
                csv.writer(file).writerow(row)
                


class Calisan:
    @staticmethod
    def gunlukGeleceKisi():
        imlec.execute('SELECT name FROM OnOdemeli WHERE rezarvasyonTarihi<1')
        res=imlec.fetchall()
        with open("gunlukGeleckKisi.csv","w")as file:
            for row in res:
                csv.writer(file).writerow(row)
    
    @staticmethod
    def gunlukDoluluk():
        imlec.execute('SELECT rezarvasyonTarihi FROM OnOdemeli WHERE inOtel=1')
        res=imlec.fetchall()
        with open("gunlukDoluluk.csv","w")as file:
            for row in res:
                csv.writer(file).writerow(row)
        



        



        
                    