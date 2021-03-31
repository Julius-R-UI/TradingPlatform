import os
import csv
from tabulate import tabulate
import time
import random

Products = []
Data = []
BuyorSellCorrect = 0
productIDvalid = 0
iterator = 0

os.system('clear')
with open('product.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        Products.append([str(i[0]), i[1], i[2],str(i[3]), str(i[4])])

with open('Data.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    for i in reader:
        if iterator == 0:
            Data.append([str(i[0]), str(i[1]), str(i[2])])
        if iterator > 0:
            Data.append([str(i[0]), str(i[1]), i[2]])
        iterator = iterator + 1

def SellingProduct(user, checker):
    while checker != 1:
        os.system('clear')
        Product = str(raw_input("What product are you selling: "))
        try:
            Price = float(raw_input("What is the price you are selling the product for: "))
        except:
            Price = ''
        
        try:
            Stock = int(raw_input("How many of those items are in your stock: "))
        except:
            Stock = ''

        ContactEmail = str(raw_input("What is the email buyers should use to contact you: "))
        ProductInfo = [Product, Price, Stock, user, ContactEmail]
        if Product == ''  or ContactEmail == '' or Price == '' or Stock == '':
            os.system('clear')
            print("You have not entered valid values, please try again")
            time.sleep(3)
            checker = 0
        elif Product != '' or Price != '' or ContactEmail != '' or Stock == '':
            checker = 1

    with open("product.csv", "r") as infile:
        reader = list(csv.reader(infile))
        reader.insert(1, ProductInfo)

    with open("product.csv", "w") as outfile:
        writer = csv.writer(outfile)
        for line in reader:
            writer.writerow(line)

def buyingProducts(user,Product, Data):
    productIDvalid = 0
    while productIDvalid != 1:
        try:
            productID = (int(raw_input("Enter the product ID, of the prodct you wish to purchase: "))+1)
        except:
            os.system('clear')
            print("The inputed product ID did not fit the requested format, please try again")
            time.sleep(3)
            os.system('clear')
            print(tabulate(Products,headers="firstrow", showindex = "always",tablefmt="presto"))
            productIDvalid = 0
        else:
            productIDvalid = 1
    print("Is this the chosen product: ")
    ChosenProduct = Product[productID]
    answer = str(raw_input("[y]es [n]o: "))
    if answer =='y':
        os.system('clear')
        print("Contact the seller at " + str(ChosenProduct[4]))
        transaction_continue = str(raw_input("Do you agree to continue with the transaction ([y]es, [n]o): "))
        if transaction_continue == "y":
            os.system('clear')
            Seller = Product[productID][3]
            iterator = 0
            for i in Data:
                if Data[iterator] == str(Seller):
                    SellerPosition = iterator
                    print(SellerPosition)
                    break
                iterator = iterator + 1
            
            '''
            Data[SellerPosition][0] = float(Data[SellerPosition][2]) + float(ChosenProduct[1])
            writer.writerows(Data)
            writer = csv.writer(open('Data.csv', 'w'))
            writer.writerows(Data)
            '''

            print("Transaction complete")
    elif answer == 'n':
        os.system('clear')
        buyingProducts(0, Product, Data)
    else:
        print("Input not supported")
        time.sleep(3)
        os.system('clear')
        print(tabulate(Products,headers="firstrow", showindex = "always",tablefmt="presto"))
        buyingProducts(0, Product)
    
    
        
    

def showingProducts(BuyorSellCorrect):
    print(tabulate(Products,headers="firstrow", showindex = "always",tablefmt="presto"))
    i = 0
    while BuyorSellCorrect != 1:
        if i == 0:
            print("")
        BuyOrSell = str(raw_input("Would you like to [b]uy or [s]ell a product: "))
        if BuyOrSell == "b" or BuyOrSell == "s":
            BuyorSellCorrect = 1
            return BuyOrSell
        elif BuyOrSell != "b" or BuyOrSell != "s":
            BuyorSellCorrect = 0
            os.system('clear')
            print("Your input does not fit the required structure, please try again")
            time.sleep(3)
            os.system('clear')
        i=i+1


BuyOrSell = showingProducts(BuyorSellCorrect)

if BuyOrSell == "s":
    user = "Root"
    SellingProduct(user, 0)
if BuyOrSell == "b":
    user = "Root"
    buyingProducts(user,Products, Data)
    
