from random import uniform,randint
from sifreleme import *
import time

class blockchain:
    def __init__(self):
        self.chain = []
        self.chain.append(sifrelemeYontemleri("sign of Eflatun",'0x000000000000000000000000000000000').md5())

    def addBlock(self, data, secim):
        previous_hash =self.chain[-1]
        hashle=sifrelemeYontemleri(data, previous_hash)
        if secim == 1:
            node = hashle.sha256()
        elif secim == 2:
            node = hashle.md5()
        elif secim == 3:
            node = hashle.sha1()
        elif secim == 4:
            node = hashle.sha224()
        elif secim == 5:
            node = hashle.sha512()

        else:
            return "Eksik veya hatalı tuşladınız"
        self.chain.append(node)

        nonce = randint(1000, 45678)

        return f"\t   |\/\/\/\/\/|\t|/\/\/\/\/\|\nnonce:\t{nonce}\ndata:\t{data}\nhash:\t{node}\nprevious hash:\t{self.chain[-2]}\n\t   |\/\/\/\/\/|\t|/\/\/\/\/\|\n"


def sifreleme(girdiYontem):


    if girdiYontem<7:
        result2 = input("data giriniz :\t")


        saveBlock = int(input(30 * "-" + "\nBlock u kaydetmek istiyor musun ? \n1)YES\n2)no:\t"))
        if saveBlock == 1:
            try:

                print("Block Oluştruluyor ....")
                time.sleep(uniform(2, 5))
                değer = block1.addBlock(result2, girdiYontem)
                

                    

                print(değer)
                
            except r:
                print("Kaydedilmedi lütfen yönetici ile iletişime geçin")
        else:
            print(block1.addBlock(result2, girdiYontem))
            print("block kaydedilmedi")
    else:
        print("Eksik veya hatali tusladınız.\n")
block1 = blockchain()


while True:
        try:
            result = int(input(30 * "-" + "|\n1)Sifreleme||\n0)Çıkış|\t"))
         
            if result == 1:
                girdiYontem = int(input(30 * "-" + "\n1)sha256\n2)md5\n3)sha1\n4)sha512\n5)sha224\n"))
                sifreleme(girdiYontem)
           
            elif result==0:
                break
        except ValueError:
            print("Karakteri yanlış")