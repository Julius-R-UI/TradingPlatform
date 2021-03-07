import csv
from csv import writer
import os
import time
import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import getpass

Data = []
iterator = 0
IsitUsed = 1

with open('Data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        if iterator > 0:
            Data.append([str(i[0]), str(i[1]), i[2]])
        iterator = iterator + 1

while IsitUsed != 0:
    os.system("clear")
    Created_Username = str(raw_input("Please create a Username to sign up: "))
    for i in range(len(Data)):
        IsitUsed = 0
        UsedUsername = str(Data[i][0])
        if UsedUsername == Created_Username:
            IsitUsed = 1
            print("That username is taken, please try again")
            time.sleep(3)
        else:
            break

salt = b'\xa7p\xce\xd39 \xa0t\x1cG\xba$\x0c])F'
kdf = PBKDF2HMAC(
     algorithm=hashes.SHA256(),
     length=32,
     salt=salt,
     iterations=100000,
     backend=default_backend()
)
IsitUsed = 1
while IsitUsed != 0:
    Password = str(getpass.getpass("Choose a secure password: "))
    Verified_Password = str(getpass.getpass("Verify your password: "))
    if Password == Verified_Password:
        IsitUsed = 0
    else:
        os.system("The passwords do not match, try again")
        time.sleep(3)
    os.system("clear")

key = Fernet(base64.urlsafe_b64encode(kdf.derive(Password)))
Password = key.encrypt(Password.encode())

Userinformation = [Created_Username,Password,float(0)]
with open("Data.csv", "r") as infile:
    reader = list(csv.reader(infile))
    reader.insert(1, Userinformation)

with open("Data.csv", "w") as outfile:
    writer = csv.writer(outfile)
    for line in reader:
        writer.writerow(line)