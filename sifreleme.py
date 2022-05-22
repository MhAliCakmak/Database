import hashlib
import datetime



class sifrelemeYontemleri:

    def __init__(self, data, previousHash="", timeStamp=datetime.datetime.now().day):

        self.data = data
        self.previousHash = previousHash
        self.timeStamp = timeStamp
        self.kuvvet = 0

    def md5(self):

        while True:
            self.kuvvet += 1
            transaction = hashlib.md5(
                (str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if transaction[0:2] == "00":
                break
        return transaction

    def sha256(self):
        while True:
            self.kuvvet += 1
            transaction = hashlib.sha256(
                (str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if transaction[0:2] == "00":
                break
        return transaction

    def sha1(self):
        while True:
            self.kuvvet += 1
            transaction = hashlib.sha1(
                (str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if transaction[0:2] == "00":
                break
        return transaction

    def sha224(self):
        while True:
            self.kuvvet += 1
            result = hashlib.sha224(
                (str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if result[0:2] == "00":
                break
        return result

    def sha512(self):
        while True:
            self.kuvvet += 1
            result = hashlib.sha512(
                (str(self.timeStamp) + str(self.data) + str(self.previousHash) + str(self.kuvvet)).encode()).hexdigest()
            if result[0:2] == "00":
                break
        return result
