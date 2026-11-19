from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
import mysql.connector as ms
mydb=ms.connect(host='localhost',user='root',password='12345')
mc=mydb.cursor()

mc.execute("create database if not exists bank_management")
mc.execute("use bank_management")
mc.execute("create table if not exists client_info(NAME varchar(30),DOB date,ADDRESS varchar(30),BALANCE int,PASSWORD varchar(8),id int primary key)")

def new_acc():
    print()
    a=input("Enter your Full Name here: ")
    print("_"*30)
    M=len(a)
    if M > 30:
        print("Please enter a valid Name")
        return()
    b=input("\nPlease enter your DOB: ")
    print("_"*30)
    c=input("\nAddress: ")
    print("_"*30)
    C=c.upper()
    if C not in open(DATA_DIR / 'EMIRATES.txt').read():
        print()
        print("="*60)
        print("Please enter a valid emirate")
        return()
    d=int(input("\nDeposit an initial starting amount to create your account(Should be more than 500):"))
    print("-"*60)
    print("Please wait as your amount is being processed...")
    print("-"*60)
    time.sleep(1)
    print()
    if d >= 500 and d<= 99999:
        time.sleep(2)
        print("\nSuccessfully Deposited")
        print("="*30)
        while True:
            e=input("\nCreate your password (Should be 8 characters):")
            Q=input("Are you sure of the password (YES/NO :")
            W=Q.lower()
            if W == 'yes':
                break
        z=len(e)
        print("-"*60)
        print("Processing all information...")
        time.sleep(2)
        if z != 8:
            print('\npassword not viable')
            return()
    else:
        print('+'*64)
        print('please deposit an amount greater that 500 and below 99,999 to finish with the joining process to proceed further')
        print()
    A=a.upper()
    C=c.upper()
    while True:
        f=random.randint(10000,99999)
        m=str(f)
        with open(DATA_DIR / "IDNO.txt",'r') as R:
            U=R.read()
            if f != U:
                break
            
    with open(DATA_DIR / "IDNO.txt",'a') as Q:
        Q.write(m)
        Q.write("\n")
        print("="*20)
        
    try:
        mc.execute("insert into client_info values('{}','{}','{}',{},'{}',{})".format(A,b,C,d,e,f))
        print("="*20)
        print("Account successfully created\n")
        print("+"*20)
        print("Welcome to Bank")
        print()
        print("\nYour personal IDNO is:",f)
        print("="*20)
        mydb.commit()
    except:
        mydb.rollback()
        print("="*20)
        print("===Account creation was not successful=== l\n ===Please try again===")
        print("="*20)  

#========================

def acc_info():
    print("-"*60)
    print("===Account-Information===\n")
    print("-"*60)
    A=int(input("Enter your IDNO:"))
    print("_"*30)
    B=input("Enter your account Password:")
    print("_"*30)
    try:
        print("-"*60)
        mc.execute("select * from client_info where id={} and password ='{}' ".format(A,B))
        data=mc.fetchall()
        if mc.rowcount>0:
            print("="*120)
            print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'PASSWORD','%40s'%'IDNO')
            print("="*120)
            for i in data:
                print(i[0],'%33s'%i[1],'%37s'%i[2],'%37s'%i[3],'%54s'%i[4],'%40s'%i[5])
                mydb.commit()
                print('+'*123)
        else:
            time.sleep(1)
            print("-"*60)
            print('\n===Entered idno or password was wrong, Please try again=== \n',"_"*50,"\n ===Please visit the bank for more enquiry===")
            print("-"*60) 
    except:
        mydb.rollback()

#========================

def depo():
    print("-"*60)
    print("===Deposit===\n")
    print("-"*60)
    Z=int(input("Enter your  Account IDNO:"))
    print("_"*30)
    X=input("Enter your password:")
    print("_"*30)
    print("+"*40)
    
    print()
    try:
        mc.execute("select id,name,balance from client_info where id = {} and password='{}' ".format(Z,X))
        data=mc.fetchall()
        if mc.rowcount>0:
            print("=== Current bank balance ===")
            print("="*60)
            print('IDNO','%40s'%'NAME','%40s'%'BALANCE')
            print("="*60)
            for i in data:
                print(i[0],'%40s'%i[1],'%40s'%i[2])
                print()
                print('+'*64)
        else:
            print("="*60)
            print("===The entered account number or password is incorrect=== \n ===Please try again===")
            print("="*60)
            return
    except:
        mydb.rollback()
        print("Sorry the entered id or password is incorrect")
        return()
    A=int(input("Enter the amount to be deposited:"))
    if A >= 500 and A <= 10000:
        try:
            mc.execute("update client_info set balance = balance + {} where id = {}".format(A,Z))
            print("="*80)
            time.sleep(1)
            print("+++Successfully Deposited+++")
            print("_"*60)
            print()
            mydb.commit()
        except:
            mydb.rollback()
    else:
        print("="*60)
        print("The depositing amount is greater than the limit provided,Please deposit in turns.")
        print("="*60)
        return()

    try:
        mc.execute("select id,name,balance from client_info where id = {} and password='{}' ".format(Z,X))
        data=mc.fetchall()
        if mc.rowcount>0:
            print("="*60)
            print('IDNO','%40s'%'NAME','%40s'%'BALANCE')
            print("="*60)
            for i in data:
                print(i[0],'%40s'%i[1],'%40s'%i[2])
                print()
                print('+'*64)
    except:
        mydb.rollback()

#========================

def withdrw():
    print("===Withdraw===\n")
    Z=int(input("Enter your  Account IDNO:"))
    print("_"*30)
    X=input("Enter your password:")
    print("_"*30)
    print("+"*40)
    print()
    try:
        print("-"*60)
        mc.execute("select id,name,balance from client_info where id = {} and password='{}' ".format(Z,X))
        data=mc.fetchall()
        if mc.rowcount>0:
            print("=== Current bank balance ===")
            print("="*60)
            print('IDNO','%40s'%'NAME','%40s'%'BALANCE')
            print("="*60)
            for i in data:
                print(i[0],'%40s'%i[1],'%40s'%i[2])
                print()
                print('+'*64)
        else:
            print("="*60)
            print("===The entered account number or password is incorrect=== \n ===Please try again===")
            print("="*60)
            return
        
    except:
        print("Sorry the entered id or password is incorrect")
        mydb.rollback()
        
    A=int(input("Enter the amount to be withdrawed:"))
    print("_"*30)
    if A >= 500 and A <= 10000:
        try:
            mc.execute("update client_info set balance = balance - {} where id = {}".format(A,Z))
            mydb.commit()
            print()
            print('Transaction in process...')
            time.sleep(1)
            print("===Successfully withdrawed===")
            print("Please collect the bill before leaving\n Thankyou for choosing Bank")
        except:
            mydb.rollback()
    else:
        print("="*60)
        print("\nYour are only authorized to withdraw an amount according to the limiit set by the bank,For further queries please visit  any nearby of our branches")
        print("+"*80)
        return()

#=====================

def Transfer():
    print("-"*60)
    print("===Account balance transfering service===")
    print("-"*60)
    Z=int(input("Enter your  Account IDNO:"))
    print("_"*30)
    X=input("Enter your password:")
    print("_"*30)
    print("+"*40)
    print()
    try:
        print("=== Current Account details  ===")
        mc.execute("select * from client_info where id = {} and password= '{}' ".format(Z,X))
        data=mc.fetchall()
        D=(data,)
        A=D
        if mc.rowcount>0:
            print("\n")
            print("="*140)
            print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'PASSWORD','%45s'%'IDNO')
            print("="*140)
            for i in data:
                print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%37s'%i[4],'%40s'%i[5])
                print("_"*150)
                print()
        else:
            print("+"*70)
            print("\n Sorry either the entered Idno or Password is wrong , Please try again .\n")
            print("+"*70)
            return()
    except:
        mydb.rollback()
        print("_"*60)
        print("There no data available to be displayed")
        print("_"*60)

    NAME=input("Enter the name of the Client: ")
    N=NAME.upper()
    M=len(N)
    if M > 25:
        print("Please enter a valid Name")
        return()
    print("_"*60)
    TRAN=int(input("Enter the account IDNO to which you would like to transfer the amount:"))
    print()
    print("===Please be attentive and careful while doing the transactions===")
    print()
    
    AMOUNT=int(input("Enter the amount you would like to transfer:"))
    if AMOUNT > A[0] [0] [3]:
        print("_"*60)
        print("The amount is greater than the the amount available in your account,Please check and try again")
        print("_"*60)
        return()
    
    try:
        mc.execute("select NAME,id from client_info where id = {} and NAME = '{}' ".format(TRAN,NAME))
        data=mc.fetchall()
        if mc.rowcount>0:
            print("="*60)
            print('NAME','%45s'%'IDNO')
            print("="*60)
            for i in data:
                print(i[0],'%37s'%i[1])
                print("_"*80)
                print()
        else:
            print("+"*70)
            print("\n Sorry either the entered Idno or Name is wrong , Please try again .\n")
            print("+"*70)
            return()
    except:
        mydb.rollback()
        print("_"*60)
        print("There no data available to be displayed")
        print("_"*60)
    sure=input("Are you sure this is the correct account (YES/NO):")
    S=sure.upper()
    if S == "YES":
        print()
        print("Transfering the amount",AMOUNT,"to account IDNO :",TRAN," from IDNO:",Z)
        print()
        print("-"*60)

        try:
            mc.execute("update client_info set balance =balance - {} where id = {} ".format(AMOUNT,Z))
            mc.execute("update client_info set balance =balance + {} where id = {} ".format(AMOUNT,TRAN))
            print("_"*60)
            print("Please waint a few minutes,Thankyou......")
            time.sleep(2)
            print("-"*60)
            print("===Successfully Credited===")
            print("-")
            print("Thankyou for choosing Bank")
            print('='*60)
            mydb.commit()

        except:
            mydb.rollback()
            print("+"*60)
            print("Sorry something went wrong")
            print("+"*60)
            return()
    else:
        return()
    
    try:
        print("=== Current Account details  ===")
        mc.execute("select * from client_info where id = {} and password= '{}' ".format(Z,X))
        data=mc.fetchall()
        if mc.rowcount>0:
            print("="*140)
            print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'PASSWORD','%45s'%'IDNO')
            print("="*140)
            for i in data:
                print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%37s'%i[4],'%40s'%i[5])
                print("_"*150)
                print()
        else:
            print("+"*70)
            print("\n Sorry either the entered Idno or Password is wrong , Please try again .\n")
            print("+"*70)
            return()
    except:
        mydb.rollback()
        print("_"*60)
        print("There no data available to be displayed")
        print("_"*60)

#========================

def editor():
    print("-"*60)
    print("===Account editing===")
    print("-"*60)
    Z=int(input("Enter your  Account IDNO:"))
    X=input("Enter your password:")
    print("+"*40)
    print()
    try:
        print("=== Current Account details  ===")
        mc.execute("select * from client_info where id = {} and password='{}' ".format(Z,X))
        data=mc.fetchall()
        if mc.rowcount>0:
            print("="*140)
            print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'PASSWORD','%45s'%'IDNO')
            print("="*140)
            for i in data:
                print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%37s'%i[4],'%40s'%i[5])
                print("_"*150)
                print()
        else:
            print("+"*70)
            print("\n Sorry either the entered Idno or Password is wrong , Please try again .\n")
            print("+"*70)
            return()
    except:
        mydb.rollback()
        print("_"*60)
        print("There no data available to be displayed")
        print("_"*60)
    
    c=input("Do you wish to change any of your account details? (YES/NO) : ")
    C=c.upper()
    if C =="YES":
        Na=input("Enter your change of name : ")
        print("_"*30)
        Nb=input("Enter your change of address: ")
        print("_"*30)
        Nc=input("Enter your new passcode  here: ")
        print("_"*30)
        try:
            mc.execute("update client_info set NAME = '{}' , ADDRESS = '{}' , PASSWORD = '{}' where id = {} ".format(Na,Nb,Nc,Z))
            mydb.commit()
            print()
            print("\nProcessing the information to our bank server,Please wait a few minutes...")
            print()
            time.sleep(2)
            print("+"*30)
            print("Change successful,the following  change will be reported to the bank Managers for the security of your account")
            print("+"*30)
        except:
            mydb.rollback()
            print("There seems to be some error,Please try again")
    else:
        print("\n===Returning to Menu===")
        print("_"*30)
        time.sleep(1)
        return()
    
#=====================

            
#============================================((ADMIN))================================================
        
def list_display():
    try:
        mc.execute("select * from client_info")
        data=mc.fetchall()
        if mc.rowcount>0:
            print("="*140)
            print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'PASSWORD','%45s'%'IDNO')
            print("="*140)
            for i in data:
                print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%37s'%i[4],'%40s'%i[5])
                print("_"*152)
        else:
            print("========")
            print("No data exists")
            print("========\n")
    except:
        mydb.rollback()
        print("_"*60)
        print('There no data available to be displayed')

#+++++++++++++++++++++++++++++++

def pro_editor():
    print("-"*60)
    print("===Account editing===")
    Z=int(input("Enter customer  Account IDNO:"))
    X=input("Enter customer password:")
    print("+"*40)
    print()
    try:
        print("=== Current Account details  ===")
        mc.execute("select * from client_info where id = {} and password='{}' ".format(Z,X))
        data=mc.fetchall()
        if mc.rowcount>0:
            print("="*140)
            print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'PASSWORD','%45s'%'IDNO')
            print("="*140)
            for i in data:
                print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%40s'%i[4],'%45s'%i[5])
                print("_"*150)
                print()
        else:
            print("+"*70)
            print("\n Sorry either the entered Idno or Password is wrong , Please try again .\n")
            print("+"*70)
            return()
    except:
        mydb.rollback()
    
    c=input("Do you want  to change any of the  account details? (YES/NO) : ")
    C=c.upper()
    if C =="YES":
        print()
        print("Performance of there acts are only authenticated to official personal, \nany violating behaviour will result in sever charges\n")
        print("_"*60)
        Na=input("Enter customer new name : ")
        print("_"*30)
        Nb=input("Enter customer DOB: ")
        print("_"*30)
        Nc=input("Enter customer address here: ")
        print("_"*30)
        Nd=input("Enter customer balance here: ")
        print("_"*30)
        Ne=input("Enter customer new passcode here: ")
        print("_"*30)

    else:
        print("-"*60)
        print("===Returning to menu===")
        print("-"*60)
        print()
        time.sleep(1)
        return()
    
        try:
            mc.execute("update client_info set NAME = '{}' , DOB = '{}',  ADDRESS = '{}' , BALANCE = {} , PASSWORD = '{}' where id = {} ".format(Na,Nb,Nc,Nd,Ne,Z))
            mydb.commit()
            print("Processing the information to bank server,Please wait a few minutes...")
            time.sleep(2)
            print("+"*30)
            print("Change successful,")
            print("+"*30)
        except:
            mydb.rollback()
            print("There seems to be some error,Please try again")
            print("_"*60)

    
import time
import random
#--------------------------------------------------------------------


while True:
    time.sleep(1)
    print()
    with open(DATA_DIR / 'START-MENU.txt','r') as f:
        x=f.read()
        print(x)
    user=int(input("\nEnter your choice:"))
    if user == 1 :
        new_acc()
    elif user == 2 :
        print()
        acc_info()
    elif user == 3 :
        print()
        depo()
    elif user==4:
        print()
        withdrw()
    elif user==5:
        print()
        editor()
    elif user==6:
        print()
        Transfer()
    elif user==7:
        print()
        print("Exiting....")
        time.sleep(2)
        quit() 

#--------------------------------------------------------------------
        
#ADMIN
        
    elif user==1024:
        print("=====ADMIN-LOG=====\n")
        a=input("For further access please enter the admin password : ")
        if a == "MANAGEMENT_1024" :
            print('\n=================')
            print('Access Granted')
            print('=================')
            while True:
                with open(DATA_DIR / "ADMIN-OPTIONS.txt",'r') as f:
                    x=f.read()
                    print(x)

                    admin=int(input("Enter the choice : "))

                    if admin == 1:
                        print("\n")
                        list_display()

                    elif admin == 2 :
                        print()
                        new_acc()

                    elif admin == 3:
                        print()
                        pro_editor()
                            
                    elif admin== 4 :
                        print()
                        print("\nExiting admin prompt...")
                        print("="*40)
                        time.sleep(3)
                        break
        else:
            print("="*40)
            print("\npasscode entered is incorrect, more incorrect trials willl result in notifying the security team.")
            print("="*40)

    else:
          print("===Sorry unrecognized option===")
