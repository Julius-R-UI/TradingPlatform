import os
import time

c = 0
while c == 0:
    loginorsignup = str(raw_input("Would you like to [l]ogin or [s]ignup: "))
    if loginorsignup == 'l':
        os.system('python Login.py')
        c = 1
    elif loginorsignup == 's':
        os.system('python Signup.py')
os.system('python ProductPage.py')