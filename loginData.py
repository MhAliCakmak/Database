import pypyodbc


from pay import *
from abc import ABC,abstractmethod
import pandas as pd
db = pypyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-F95I3O2\SQLEXPRESS;'
    'Database=rezervasyon;'
    'Trusted_Connection=True;'  
)



mailMetni="""Lutfen 15 gun icinde rezervasyon odemesi gerceklestirin..."""
mailKonu="Rezervasyon Islemleri"



imlec = db.cursor()
card=Pay()

rezervasyonUcreti=1000
class RezervLoginService:
    

    def addRezerv(self,secim,name,lastname,publicAddress,privateAddress,rezervasyonDate):
            
        
        if secim==1:
            rezerUcret=rezervasyonUcreti*0.75
            commands = 'INSERT INTO OnOdemeli VALUES(?,?,?,?,?,?,?,?)'
            
            print(f"Rezervasyon ucreti {rezerUcret} ")
            bakiye=card.pay(rezerUcret)
            
            data = (publicAddress,privateAddress,name,lastname,rezervasyonDate,rezerUcret,1,0)
            

        elif secim==2:
            eposta=input(f"{50*' '}E-mail:")
            rezerUcret=rezervasyonUcreti*0.85
            commands = 'INSERT INTO altmisGunRezervasyon VALUES(?,?,?,?,?,?,?,?,?)'
            data = (publicAddress,privateAddress,name,lastname,eposta,rezerUcret,rezervasyonDate,0,0)
        
        elif secim==3:
            commands = 'INSERT INTO Standart VALUES(?,?,?,?,?,?,?,?)'
            data = (publicAddress,privateAddress,name,lastname,rezervasyonDate,rezervasyonUcreti,0,0)
            bakiye=card.pay(0)


        imlec.execute(commands,data)
        imlec.commit()
    
    def authRezerv(self,typeRezerv,pubAddress):
        if typeRezerv==1:

            imlec.execute('SELECT * FROM OnOdemeli ')
            rezervs=imlec.fetchall()
            for rezerv in rezervs:
                if rezerv[1]==pubAddress:
                    print(f"\n{50*' '}Public Address:{rezerv[1]}\n{50*' '}Name : {rezerv[3]}\n{50*' '}Lastname: {rezerv[4]}\n{50*' '}Rezervasyon KalanGun:{rezerv[5]}\n{50*' '}Rezervasyon Ucreti:{rezerv[6]}\n{50*' '}Odenme Durumu{rezerv[7]}\n")
                    
        
        elif typeRezerv==2:
            imlec.execute('SELECT * FROM altmisGunRezervasyon ')
            rezervs=imlec.fetchall()
            for rezerv in rezervs:
                if rezerv[1]==pubAddress:
                    print(f"\n{50*' '}Public Address:{rezerv[1]}\n{50*' '}Name : {rezerv[3]}\n{50*' '}Lastname: {rezerv[4]}\n{50*' '}Eposta:{rezerv[5]}\n{50*' '}Rezervasyon Ucreti :{rezerv[6]}\n{50*' '}Rezervasyon KalanGun:{rezerv[7]}\n")
                    if rezerv[7]<=45 and rezerv[7]>=30:
                        
                        print("Email inizi kontrol edin ")
                        cancel=int(input(f"\n{50*' '}1)Ode \n{50*' '}2)Iptal Et\n{50*' '}3)Cıkıs"))
                        if cancel==1:
                            privAdd=input("Private Address:")
                            bakiye=card.pay(0)
                            commands=('UPDATE altmisGunRezervasyon  SET odendi = ? WHERE privateAddress = ?')
                            data=(1,privAdd)
                            imlec.execute(commands,data)
                            db.commit()

                        elif cancel==2:
                            privAdd=input("Private Address:")
                            commands=('DELETE FROM altmisGunRezervasyon WHERE privateAddress = ?')
                            data=(privAdd,)
                            imlec.execute(commands,data)
                            db.commit()
                        elif cancel==3:
                            quit()
                        else:
                            print("eksik veya hatalı girsim")

                    elif rezerv[7]<30:
                        
                        commands=('DELETE FROM altmisGunRezervasyon WHERE privateAddress = ?')
                        data=(rezerv[2],)
                        imlec.execute(commands,data)
                        db.commit()
                        print("Verilen sure zarfi sure icinde rezervasyon ucreti odenmedigi icin silinmistir")
                        
                        
                        



                   
        elif typeRezerv==3:
            imlec.execute('SELECT * FROM Standart ')
            rezervs=imlec.fetchall()
            for rezerv in rezervs:
                if rezerv[1]==pubAddress:
                    print(f"\n{50*' '}Public Address:{rezerv[1]}\n{50*' '}Name : {rezerv[3]}\n{50*' '}Lastname: {rezerv[4]}\n{50*' '}Rezervasyon Kalan Gun :{rezerv[5]}\n{50*' '}Rezervasyon Ucreti:{rezerv[6]}\n")
                    if rezerv[6]<3:
                        privAdd=input("Private Address:")
                        

                    
    def changeRezerv(self,typeRezerv,privateAddress):
        
        if typeRezerv==1:
            iptal=int(input(f"\n{50*' '}1)Rezervasyon Guncelle\n{50*' '}2)Iptal et\n{50*' '}3)Cıkıs "))
            if iptal==1:
                guncelDate=int(input("Gunclenecek tarih:"))
                commands = 'UPDATE OnOdemeli SET rezervasyonUcreti = ?,rezarvasyonTarihi=? WHERE privateAddress = ?'
                yeniUcret=rezervasyonUcreti*1.10-rezervasyonUcreti*0.75
                bakiye=card.pay(yeniUcret)
                yeniUcret+=rezervasyonUcreti
                data=(yeniUcret,guncelDate,privateAddress)
            
            elif iptal==2:
                sure=int(input("Iptal ettiginiz taktirde para iadesi olmayacaktır.Devam etmek için 1 e tıklayın geri cıkmak icin 2 tıklayın"))
                if sure==1:
                    commands=('DELETE FROM OnOdemeli WHERE privateAddress = ?')
                    data=(privateAddress,)
                elif sure==2:
                    quit()
                else:
                    print("eksik veya hatalı tuşladınız")
            
            elif iptal==3:
                quit()
            
            else:
                print("Eksik veya hatali tusladiniz")

            imlec.execute(commands,data)
            db.commit()
        
        elif typeRezerv==2:
            guncelDate=int(input("Gunclenecek tarih:"))
            commands ='UPDATE altmisGunRezervasyon SET rezervasyonUcreti = ?,rezervasyonDate=?  WHERE privateAddress = ?'
            yeniUcret=rezervasyonUcreti*1.10-rezervasyonUcreti*0.85
            data=(yeniUcret,guncelDate,privateAddress)
            imlec.execute(commands,data)
            db.commit()

        elif typeRezerv==3:
            guncelDate=int(input("Gunclenecek tarih:"))
            command1=''
            command2 = 'UPDATE Standart SET rezarvasyonTarihi=? WHERE privateAddress = ?'
            
            data=(guncelDate,privateAddress)
            imlec.execute(command2,data)
            db.commit()

    
    
        




       
        

        
            

         
     
        
        
        

        