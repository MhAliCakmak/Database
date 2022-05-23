import sys,os
from loginData import *
from random import uniform,randint
from blockchain import *
from rapor import *
rezerv=RezervLoginService()
admin=Admin()
calisan=Calisan()



def Rezervasyon():
    rezerChoose=int(input(f"{25*' '}\n{50*' '}1)On Odemeli Rezervasyon \n{50*' '}2)60 Gün Önceden Rezervasyon\n{50*' '}3)Standart Rezervasyon\n{50*' '}4)Çıkış"))
    os.system("cls")
    if rezerChoose==1:     
        print("Ön Ödemeli Rezervasyon\n")
        rezName=input(f"{50*' '}Name:")
        rezLastName=input(f"{50*' '}Lastname:")
        rezDate=int(input(f"{50*' '}Rezervasyon Tarihi:"))
        data=rezLastName+rezName+str(rezDate)
        if rezDate>=90:
            try:
                result = int(input(30 * "-" + "|\n1)Sifreleme||\n0)Çıkış|\t"))
          
                if result == 1:
                    girdiYontem = int(input(f"{30 * ' '}+\n1)sha256\n2)md5\n3)sha1\n4)sha512\n5)sha224\n"))
                    rezNo,block,rezOzelNo=hashleme(girdiYontem,data)
                    print(f"\n{50* ' '}Block Bilgisi\n{block} \n\n{50* ' '}+Public işlem adresi\n{rezNo} \n\n\n{50* ' '}+Değişiklik icin private numaranız\n{rezOzelNo}\n\n")
                    rezerv.addRezerv(1,rezName,rezLastName,rezNo,rezOzelNo,rezDate)
                    time.sleep(uniform(2, 5))
                
                
                elif result==0:
                    quit()
            except ValueError:
                print("Karakteri yanlış") 
        else:
            print("Ön ödemeli rezervasyon tarihi 90 gün ve daha fazla olması gerekir")
    elif rezerChoose==2:
        print("60 Gün Önceden Rezervasyon\n")
        rezName=input(f"{50*' '}Name:")
        rezLastName=input(f"{50*' '}Lastname:")
        
        rezDate=int(input(f"{50*' '}Rezervasyon Tarihi:"))
        data=rezLastName+rezName+str(rezDate)
        if rezDate>=60:

            try:
                result = int(input(30 * "-" + "|\n1)Sifreleme||\n0)Çıkış|\t"))
         
                if result == 1:
                    girdiYontem = int(input(f"{30 * ' '}+\n1)sha256\n2)md5\n3)sha1\n4)sha512\n5)sha224\n"))
                    rezNo,block,rezOzelNo=hashleme(girdiYontem,data)
                    print(f"\n{50* ' '}Block Bilgisi\n{block} \n\n{50* ' '}+Public işlem adresi\n{rezNo} \n\n\n{50* ' '}+Değişiklik icin private numaranız\n{rezOzelNo}\n\n")
                    rezerv.addRezerv(2,rezName,rezLastName,rezNo,rezOzelNo,rezDate)
                    time.sleep(uniform(2,5))
                
                
                elif result==0:
                    quit()
            except ValueError:
                print("Karakteri yanlış") 
        else:
            print("60 gün Önceden Rezervasyon 60 gün ve daha fazla olması gerekir")
    
    elif rezerChoose==3:
        print("Standart Rezervasyon\n")
        rezName=input(f"{50*' '}Name:")
        rezLastName=input(f"{50*' '}Lastname:")
        
        rezDate=int(input(f"{50*' '}Rezervasyon Tarihi:"))
        data=rezLastName+rezName+str(rezDate)

        try:
            result = int(input(30 * "-" + "|\n1)Sifreleme||\n0)Çıkış|\t"))
         
            if result == 1:
                girdiYontem = int(input(f"{30 * ' '}+\n1)sha256\n2)md5\n3)sha1\n4)sha512\n5)sha224\n"))
                rezNo,block,rezOzelNo=hashleme(girdiYontem,data)
                print(f"\n{50* ' '}Block Bilgisi\n{block} \n\n{50* ' '}+Public işlem adresi\n{rezNo} \n\n\n{50* ' '}+Değişiklik icin private numaranız\n{rezOzelNo}\n\n")
                rezerv.addRezerv(3,rezName,rezLastName,rezNo,rezOzelNo,rezDate)
                time.sleep(uniform(2,5))
                
                
            elif result==0:
                quit()
        except ValueError:
            print("Karakteri yanlış") 
   

    elif rezerChoose==4:
        quit()
    else:
            print("Eksik veya hatalı giris")


def Rezervasyonlarim():
    
    rezervChoose=int(input(f"{25*' '}\n{50*' '}1)Ön ödemeli Rezervasyon \n{50*' '}2)60 gün önceden Rezervasyon \n{50*' '}3)Standart Rezervasyon\n{50*' '}4)Çıkış"))
    menuChoose=int(input(f"{25*' '}\n{50*' '}1)Rezervasyon Görüntüle \n{50*' '}2)Rezervasyon Guncelle \n{50*' '}3)Çıkış"))
    if menuChoose==1:
        pubAddress=input("Public Address:")
        
        if rezervChoose==1:
            
            rezerv.authRezerv(1,pubAddress)
        elif rezervChoose==2:
            rezerv.authRezerv(2,pubAddress)
    
        elif rezervChoose==3:
            rezerv.authRezerv(3,pubAddress)

        else:
            print("Eksik veya hatalı giris")
    elif menuChoose==2:
        
        privateAddress=input("Private Address:")
        
        if rezervChoose==1:
            rezerv.changeRezerv(1,privateAddress)
        elif rezervChoose==2:
            rezerv.changeRezerv(2,privateAddress)
        
        elif rezervChoose==3:
            rezerv.changeRezerv(3,privateAddress)
       
        else:
            print("Eksik veya hatalı giris")
    

    elif menuChoose==4:
        quit()
    else:
            print("Eksik veya hatalı giris")
    
def Rapor():
    raporType=int(input(f"\n{25*' '}1)Admin\n{25*' '}2)Calisan\n{25*' '}3)Cıkıs"))
    if raporType==1:
        adminType=int(input(f"\n{25*' '}1)Beklenen Doluluk Orani\n{25*' '}2)Beklenen Oda Geliri \n{25*' '}3)Cıkıs"))
        if adminType==1:
            admin.beklenenDolulukOran()
        elif adminType==2:
            admin.beklenenOdaGeliri()
        elif adminType==3:
            quit()


    elif raporType==2:
        calisanType=int(input(f"\n{25*' '}1)Gunluk Gelenler sayisi\n{25*' '}2)Gunluk Doluluk oranı \n{25*' '}3)Cıkıs"))
        if calisanType==1:
            calisan.gunlukGeleceKisi()
        elif calisanType==2:
            calisan.gunlukDoluluk()
        elif calisanType==3:
            quit()
        else:
            print("eksik veya hatalı tuşladiniz")

    elif raporType==3:
        quit()

while True:
    
    
    menuChoose=int(input(f"{25*' '}Ophella Oasais Otel Rezervasyon Hizmetine Hoşgeldiniz Sizlere Nasıl Yardımcı olabilirim?\n{50*' '}1)Rezervasyon Işlemleri\n{50*' '}2)Raporlar\n{50*' '}3)Cıkıs"))
    os.system("cls")
    if menuChoose==1:
        
        print(f"{30*' '}{85*'-'} ")
        UserMenu=int(input(f"{25*' '}Kullanıcı arayüzüne Hosgeldiniz\n{50*' '}1)Rezervasyon Yap\n{50*' '}2)Rezervasyonlarım\n{50*' '} 3)Cıkış"))
        if  UserMenu==1:
            Rezervasyon()
        elif UserMenu ==2:
            Rezervasyonlarim()
        
        elif UserMenu==3:
            quit()
        
        else:
            print("Eksik veya hatalı giris")
   
    elif menuChoose==2:
        Rapor()

    elif menuChoose==3:
        quit()
    
    else:
            print("Eksik veya hatalı giris")
    
