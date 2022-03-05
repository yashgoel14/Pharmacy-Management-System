import mysql.connector
import matplotlib.pyplot as plt
import numpy as np
import time
import os
import platform
print()
print("\t\t\tPHARMACY MANAGEMENT SYSTEM")
print()

def equal():
    for i in range(79):
        print("=",end="")
        time.sleep(0.01)
equal()
print("""
 \t................................................................
 \t////////////////////////////////////////////////////////////////
 \t..............WELCOME TO THIS MEDICAL-SHOP................
 \t\t........MADE BY yash goel.........
""")
print()
mydb=mysql.connector.connect(host="localhost",user="root",passwd="123456",database="pharmacy")
cur=mydb.cursor()
cur.execute("select * from medicine")
a=[]
b=[]
c=[]
for p in cur:
    a.append(p[0])
    b.append(p[1])
    c.append(p[2])
    
def add_medicine():
    print()
    equal()
    print("\t\t\t\tENTER DETAILS OF MEDICINES")
    equal()
    try:
        n=int(input("ENTER NO. OF MEDICINES TO BE ADDED : "))
        for i in range(n):
            print()
            x=input("ENTER THE MEDICINE NAME : ")
            if x not in a:
                y=input("ENTER THE PRICE : ")
                z=input("ENTER THE QUANTITY : ")
                sql=("INSERT INTO medicine VALUES (%s,%s,%s)")
                data=(x,y,z)
                cur.execute(sql,data)
                mydb.commit()
                print()
                print("------INFORMATION ADDED-------")
            else:
                print()
                print("..THIS MEDICINE IS ALREADY IN STOCK..")
    except:
        print("!!!!!!INVALID OPERATION!!!!!!")
        
def update_record():
    try:
        print()
        equal()
        print("\t\t\t\t\tUPDATE RECORD")
        equal()
        print("1. DELETE ITEM\n2. CHANGE ITEM DATA")
        h=int(input("ENTER YOUR CHOICE : "))
        if h==1:
            print()
            print("\t\t>>>>>>>>>>>>>>>>> DELETE ITEM <<<<<<<<<<<<<<<<<")
            print()
            n=int(input("ENTER NO. OF MEDICINES TO BE DELETED : "))
            for i in range(n):
                print()
                x=input("ENTER THE MEDICINE NAME TO BE DELETED : ")
                if x in a:
                    sql=("""DELETE FROM medicine WHERE medicine_name = %s """)
                    data=(x,)
                    cur.execute(sql,data)
                    mydb.commit()
                    print()
                    print("---MEDICINE DELETED----")
                else:
                    print()
                    print("..THIS MEDICINE IS NOT IN STOCK..")
        elif h==2:
            print()
            print("\t\t>>>>>>>>>>>>>> CHANGE DATA ITEM <<<<<<<<<<<<<<<<<")
            print()
            print("1. CHANGE MEDICINE NAME\n2. CHANGE PRICE\n3. CHANGE QUANTITY")
            o=int(input("ENTER YOUR CHOICE : "))
            if o==1:
                print()
                print("\t\t\t......MEDICINE NAME.......")
                print()
                n=int(input("ENTER NO. OF MEDICINES  TO BE UPDATED : "))
                for i in range(n):
                    print()
                    x=input("ENTER OLD MEDICINE NAME : ")
                    if x in a:
                        y=input("ENTER NEW MEDICINE NAME : ")
                        sql=("UPDATE medicine SET medicine_name= %s WHERE medicine_name=%s")
                        data=(y,x)
                        cur.execute(sql,data)
                        mydb.commit()
                        print()
                        print("---STOCK UPDATED SUCCESSFULLY---")
                    else:
                        print()
                        print("..THIS MEDICINE IS NOT IN STOCK..")
            elif o==2:
                print()
                print("\t\t\t......MEDICINE PRICE.......")
                print()
                n=int(input("ENTER NO. OF MEDICINES TO BE UPDATED : "))
                for i in range(n):
                    print()
                    x=input("ENTER MEDICINE NAME : ")
                    if x in a:
                        y=input("ENTER NEW PRICE : ")
                        sql=("UPDATE medicine SET price = %s WHERE medicine_name = %s")
                        data=(y,x)
                        cur.execute(sql,data)
                        mydb.commit()
                        print()
                        print("---STOCK UPDATED SUCCESSFULLY--")
                    else:
                        print()
                        print("..THIS MEDICINE IS NOT IN STOCK..")
            elif o==3:
                print()
                print("\t\t\t......MEDICINE QUANTITY.......")
                print()
                n=int(input("ENTER NO. OF MEDICINES TO BE UPDATED : "))
                for i in range(n):
                    print()
                    x=input("ENTER MEDICINE NAME : ")
                    if x in a:
                        y=input("ENTER NEW QUANTITY: ")
                        sql=("UPDATE medicine SET quantity = %s WHERE medicine_name = %s")
                        data=(y,x)
                        cur.execute(sql,data)
                        mydb.commit()
                        print()
                        print("---STOCK UPDATED SUCCESSFULLY---")
                    else:
                        print()
                        print("..THIS MEDICINE IS NOT IN STOCK..")
    except:
        print("!!!!!!!INVALID OPERATION!!!!!!!")
        
def  sell_medicine():
    try:
        equal()
        print("\t\t\t\t\tSELL MEDICINE")
        equal()
        ans="yes"
        while ans.lower()=="yes":
            x=input("ENTER MEDICINE NAME TO BE PURCHASED : ")
            if x in a:
                y=int(input("ENTER QUANTITY OF MEDICINES : "))
                l=a.index(x)
                if (y <=c[l]):
                    print("\nMEDICINE IS IN STOCK")
                    print("\n!!!!BEFORE SELLING THE MEDICINE PLEASE CHECK THE EXPIRY DATE OF THE MEDICINE")
                    print( )
                    print("""
                                    RECEIPT
                                  ...........
                                  
                            MEDICINE NAME:""",x)

                    print("                          TOTAL PRICE:",y*b[l])
                    p=c[l]-y
                    q=c[l]
                    sql=("UPDATE medicine SET quantity = %s WHERE quantity = %s")
                    data=(p,q)
                    cur.execute(sql,data)
                    mydb.commit()
                    print("\nDO YOU WANT TO SEE THE DETAILS OF THE SOLD MEDICINE IN THE STOCK? ( YES / NO )")
                    z=str(input("\nENTER YOUR CHOICE : "))
                    if z=="yes":
                        print("\nMEDICINE NAME:",a[l])
                        print("PRICE:",b[l])
                        print("QUANTITY LEFT:",c[l]-y)
                else:
                    print("\nTHIS QUANTITY OF MEDICINE IS NOT AVAILABLE")
            else:
                print("..THIS MEDICINE IS NOT IN STOCK..")
            print()
            print("WANT TO SELL MORE MEDICINES (yes/no)")
            ans=input("ENTER YOUR CHOICE : ")
            print()
    except():
        print("!!!!!!!!INVALID OPERATION!!!!!!!!!!!")
        
def display_medicine():
    try:
        equal()
        print("\t\t\t\t\t MEDICINE DETAILS")
        equal()
        ans="yes"
        while ans.lower()=="yes":
            x=input("ENTER NAME OF THE MEDICINE TO SEE ITS DETAILS : ")
            if x not in a:
                print("..THIS MEDICINE IS NOT IN STOCK..")
            elif x in a:
                l=a.index(x)
                print("MEDICINE NAME : ",a[l])
                print("PRICE : ",b[l],"\t\tQUANTITY : ",c[l]) 
            print()
            print("WANT TO SEE MORE DETAILS (yes/no)")
            ans=input("ENTER YOUR CHOICE : ")
            print()
    except:
        print("!!!!!!!INVALID OPERATION!!!!!!!!!")
                
def stock_details():
    equal()
    print("\t\t\t\tDETAILS OF FULL STOCK ")
    equal()
    cur.execute("select * from medicine")
    for i in cur:
        print("MEDICINE : ",i[0],"\nPRICE : ",i[1],"\nQUANTITY : ",i[2])
        print()
        
def clrscreen():
    if platform.system()=="Windows":
        print(os.system("cls"))
        
def graph():
    try:
        print("1. BAR GRAPH\n2. PIE CHART")
        h=int(input("ENTER YOUR CHOICE : "))
        if h==1:
            plt.bar(np.arange(len(a)),c,color="#E19715")
            plt.xticks(np.arange(len(a)),a)
            plt.xlabel("MEDICINES")
            plt.ylabel("QUANTITY")
            plt.title("MEDICINES IN STOCK")
            plt.show()
        if h==2:
            plt.pie(c,labels=a,shadow=True,startangle=180)
            plt.title("MEDICINES IN STOCK")
            plt.show()
    except:
        print("!!!!!!!!INVALID OPERATIONR!!!!!!!!!")
        
while True:
    clrscreen()
    time.sleep(1)
    print("____________________________________MENU______________________________________")
    print()
    print("1. ADD MEDICINE\n2. UPDATE RECORD\n3. DETAILS OF FULL STOCK\n4. MEDICINE DETAIL\n5. SELL MEDICINE\n6. GRAPH\n7. EXIT")
    print()
    o=int(input("ENTER YOUR CHOICE : "))
    if o==1:
        add_medicine()
    elif o==2:
        update_record()
    elif o==3:
        stock_details()
    elif o==4:
        display_medicine()
    elif o==5:
        sell_medicine()
    elif o==6:
        graph()
    elif o==7:
        break
    else:
        print("WRONG CHOICE.....ENTER YOUR CHOICE AGAIN")
        j=input("ENTER ANY KEY TO CONTINUE : ")



        
        
