from random import randint
import sys,os
from loginData import *




class Pay:

    

    
    def pay(cls,tutar):
        bakiye=randint(980,10000)
        cardNo=input("Hesap No:")
        lastdate=input("Son kullanma tarihi:")
        cvc=input("Cvc:")

        bakiye=bakiye-tutar
        if bakiye >tutar:
            return bakiye
        elif bakiye<tutar:
            print("Yetersiz Bakiye")
        
        
        
   
    def addMoney(self,tutar):
        self.bakiye+=tutar
        return self.bakiye



