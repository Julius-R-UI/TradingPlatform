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
IsthepasswrdCorrect = 0
f = 0
key = []

def ReadingCsv(iterator):
    with open('Data.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        for i in reader:
            if iterator > 0:
                Data.append([str(i[0]), str(i[1]), i[2]])
            iterator = iterator + 1

def password_checker(Inputted_Password,Password,key):
    '''
    try:
        key = base64.urlsafe_b64encode(kdf.derive(Inputted_Password))
        key = Fernet(key)
        Password = key.decrypt(str(Password))
    except:
        if Inputted_Password == str(Password):
            IsthepasswrdCorrect = 1
            return IsthepasswrdCorrect
        elif Inputted_Password != str(Password):
            os.system('clear')
            print("Wrong password, please try again")
            time.sleep(3)
            os.system('clear')
    else:
        IsthepasswrdCorrect = 1
        return IsthepasswrdCorrect
    '''
    try:
        Password = key.decrypt(str(Password))
    except:
        if Inputted_Password == str(Password):
            IsthepasswrdCorrect = 1
            return IsthepasswrdCorrect
        elif Inputted_Password != str(Password):
            os.system('clear')
            print("Wrong password, please try again")
            time.sleep(3)
            os.system('clear')
        return 0
    else:
        if Inputted_Password == str(Password):
            return 1

def UsernameInput(DoestheUsernameExist, iterator):
    while DoestheUsernameExist == 0:
        Username = str(raw_input("Your username: "))
        for i in range(len(Data)):
            if Username == str(Data[i][0]):
                Encrypted_Password = str(Data[i][1])
                DoestheUsernameExist = 1
                return i
        os.system('clear')
        print("Your username does not exist, would you like to sign up")
        answer = str(raw_input("[y]es [n]o: "))
        if answer =='y':
            os.system('clear')
            import Signup
            #Signup
            ReadingCsv(0)
            UsernameInput
            
        elif answer == 'n':
            None
        else:
            print("Input not supported")
            UsernameInput


ReadingCsv(0)
i = UsernameInput(0,0)



salt = b'\xa7p\xce\xd39 \xa0t\x1cG\xba$\x0c])F'


while IsthepasswrdCorrect != 1:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
     )
    Password = Data[i][1]
    Inputted_Password = str(getpass.getpass("Enter your password: "))
    key.append(base64.urlsafe_b64encode(kdf.derive(Inputted_Password)))
    used_key = Fernet(key[f])
    IsthepasswrdCorrect = password_checker(Inputted_Password,Password,used_key)
    f = f + 1
os.system('clear')
print("Login Successful")
AllUsers = [row[0] for row in Data]
Userloggedin = AllUsers[i]
with open('usercurrentlyloggedin.txt', 'w') as f:
    f.write('\n')
    f.write(Userloggedin)
