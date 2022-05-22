import sys,os
from loginData import *
user=UserLoginService()

def OnOdemeli(people):
    print(f"{25*' '}\n{50*' '}Ön Ödeme Rezervasyonuna hosgeldiniz")
    onOdemeRezervasyonTarihi=int(input("kac gün sonra:"))
    
    
    




while True:
    
    
    menuChoose=int(input(f"{25*' '}Ophella Oasais Otel Rezervasyon Hizmetine Hoşgeldiniz Sizlere Nasıl Yardımcı olabilirim?\n{50*' '}1)Kayıt ve Giris Islemleri\n{50*' '}2)Cıkıs"))
    os.system("cls")
    if menuChoose==1:
        authUser=False
        print(f"{30*' '}{85*'-'} ")
        loginStatus=int(input(f"{25*' '}\n{50*' '}1)Kullanıcı Kaydı\n{50*' '}2)Kullanıcı Girisi\n{50*' '}3)Admin Kaydı\n{50*' '}4)Admin Girisi\n{50*' '}6)Ust Menuye Dön"))
        if loginStatus==1:
            loginName=input("İsim:")
            loginLastname=input("Soyisim:")
            loginEmail=input("Email:")
            loginPhone=input("Phone:")
            loginPassword=input("Password:")
            try:
                user.AddUser(loginName,loginLastname,loginEmail,loginPhone,loginPassword)
            except:
                print("hata")
            finally:
                print("işlem başarılı")

        elif loginStatus==2:
            authEmail=input("Email:")
            authPassword=input("Password:")
            os.system("cls")
            if authUser !=user.authUser(authEmail,authPassword):
                UserMenu=int(input(f"{25*' '}Kullanıcı arayüzüne Hosgeldiniz\n{50*' '}1)Rezervasyon Yap\n{50*' '}2)Rezervasyonlarım\n{50*' '} 3)Cıkış"))
                if UserMenu==1:
                    rezervasyonMenu=int(input(f"{25*' '}\n{50*' '}1)On Odemeli Rezervasyon \n{50*' '}2)60 gun onceden Rezarvasyon \n{50*' '}3)Standart Rezervasyon\n{50*' '}$)Tesvik Rezervasyon\n{50*' '}5)Çıkış"))
                    if rezervasyonMenu==1:
                        OnOdemeli(user.authUser(authEmail,authPassword))
                    elif rezervasyonMenu==2:
                        pass
                    elif rezervasyonMenu==3:
                        pass
                    elif rezervasyonMenu==4:
                        pass
                    elif rezervasyonMenu==5:
                        pass
                elif UserMenu==2:
                    pass
                elif UserMenu==3:
                    quit()

            else:
                print("hata")
                
            
        
            
        


    elif menuChoose==2:
        quit()