from pathlib import Path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = PROJECT_ROOT / "data"
import mysql.connector as ms
mydb=ms.connect(host='localhost',user='root',password='12345')
mc=mydb.cursor()

mc.execute("create database if not exists bank_management")
mc.execute("use bank_management")
mc.execute("create table if not exists checking_acc(NAME varchar(30),DOB date,ADDRESS varchar(30),BALANCE int,PASSWORD varchar(8),id int primary key,EMIRATESID varchar(15))")
mc.execute("create table if not exists saving_acc(NAME varchar(30),DOB date,ADDRESS varchar(30),BALANCE int,PASSWORD varchar(8),id int primary key,EMIRATESID varchar(15))")
mc.execute("create table if not exists pending(NAME varchar(30),DOB date,ADDRESS varchar(30),BALANCE int,EMIRATESID varchar(20),TYPE varchar(15),STATUS varchar(8),TEM_PAS int)")

def apply():
    print()
    print("What type of account are you applying for : 1. Checking     2. Saving\n")
    SELECT=input("Enter what type of Account do you want to apply for (Checking/Saving) : ")
    Z=SELECT.lower()
    if Z == "checking":
        print()
        print("\t\t===Please Enter the Follwoing Details===\n")
        a=input("Enter your Full Name here: ")
        print("_"*30)
        M=len(a)
        if M > 30:
            print("Please enter a valid Name")
            return()
        b=input("\nPlease enter your DOB( YYYY-MM-DD) : ")
        print("_"*30)
        c=input("\nAddress: ")
        print("_"*30)
        C=c.upper()
        if C not in open(DATA_DIR / 'EMIRATES.txt').read():
            print()
            print("="*60)
            print("Please enter a valid emirate")
            return()
        d=int(input("Enter your Emirates id:"))
        print("_"*30)
        if d == 15:
            pass

    elif Z == "saving":
        print()
        print("\t\t===Please Enter the Follwoing Details===\n")
        a=input("Enter your Full Name here: ")
        print("_"*30)
        M=len(a)
        if M > 30:
            print("Please enter a valid Name")
            return()
        b=input("\nPlease enter your DOB( YYYY-MM-DD) : ")
        print("_"*30)
        c=input("\nAddress: ")
        print("_"*30)
        C=c.upper()
        if C not in open(DATA_DIR / 'EMIRATES.txt').read():
            print()
            print("="*60)
            print("Please enter a valid emirate")
            return()
        d=input("Enter your Emirates id:")
        print("_"*30)
    else:
        print("="*40)
        print("\nPlease enter a viable option")
        print("="*40)
        return
        
    
    AF=int(input("\nDeposit an initial starting amount to create your account(Should be more than 500):"))
    print("-"*60)
    print("Please wait as your amount is being processed...")
    print("-"*60)
    time.sleep(1)
    print()
    if AF >= 500 and AF<= 99999:
        time.sleep(2)
        print("\nSuccessfully Deposited")
        print("="*30)
    else:
        print('+'*64)
        print('please deposit an amount greater that 500 and below 99,999 to finish with the joining process to proceed further')
        print()
        return()
    A=a.upper()
    G=("PENDING")
    AA=random.randint(10000,99999)

    try:
        mc.execute("insert into pending values('{}','{}','{}',{},'{}','{}','{}',{})".format(A,b,C,AF,d,Z,G,AA))
        print("Your Temporary 1 time password is : ",AA)
        with open(DATA_DIR / 'TEMPASS.txt','a+') as f:
            TY=str(AA)
            f.write('\n')
            f.write(TY)
        print("="*20)
        print("Application successfully saved\n")
        print("+"*20)
        print("Welcome to Bank")
        print()
        print("\nThe Manager will check the appication and create your account respectively")
        print("="*20)
        mydb.commit()
    except:
        mydb.rollback()
        print("="*20)
        print("===Application not successful=== \n ===Please try again===")
        print("="*20) 
        
        
#========================

def USER_passcre():
    print("===Please enter the following to check your account status===\n")
    USER=input("Please Enter your name here : ")
    print("_"*30)
    USERB=input("Enter your Emirates-ID : ")
    print("_"*30)
    USERC=int(input("Enter the temporary password provided to you : "))
    AG=str(USERC)
    print("_"*30)
    TYPE=input("Enter the account type you applied for (CHECKING/SAVING) : ")
    TYPE2=TYPE.upper()
    print("\n============== Processing ==============\n")
    try:
        mc.execute("select * from pending where TEM_PAS = '{}' and TYPE = '{}'".format(USERC,TYPE2))
        data=mc.fetchall()
        if mc.rowcount == 1:
            print("="*60)
            print("Account Status : Pending ")
        else:
            with open(DATA_DIR / 'TEMPASS.txt','r') as f:
                data=f.read().splitlines()
                found = False
                for i in data:
                    if i == AG:
                        found = True
                        if TYPE2=='CHECKING':
                            try:
                                mc.execute("select password from checking_acc where name = '{}' and emiratesid = '{}'".format(USER,USERB))
                                data=mc.fetchone()
                                DATA=data[0]
                                if DATA == 'PCODESET':
                                    pass
                                else:
                                    print("="*60)
                                    print("\t\t ====  Account already active  ====")
                                    print("="*60)
                                    return()
                            except:
                                print('Someting went wrong')
                                return()
                        print("Account Status : Accepted ")
                        print()
                        print("="*60)
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
                            print("-"*60)
                        if TYPE2 =='CHECKING':
                            try:
                                mc.execute("update checking_acc set PASSWORD = '{}' where EMIRATESID ='{}' and NAME ='{}'".format(e,USERB,USER))
                                mydb.commit()
                            except:
                                mydb.rollback()
                                print("_"*60)
                                print('Unsuccessful in Saving the data')
                                        
                            try:
                                mc.execute("select * from checking_acc where NAME = '{}' and PASSWORD = '{}'".format(USER,e))
                                data=mc.fetchall()
                                if mc.rowcount>0:
                                    print("="*140)
                                    print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%45s'%'IDNO','%45s'%'EMIRATES-ID')
                                    print("="*140)
                                    for i in data:
                                        print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%40s'%i[5],'%40s'%i[6])
                                        print("_"*152)
                                        print("="*20)
                                        print("\n Account succesfully activated")
                                        print("_"*152)
                                        print("Your IDNO is : ",i[5])
                                        print("="*20)
                                        print()
                                        mydb.commit()
                                else:
                                    print("========")
                                    print("No data exists")
                                    print("========\n")
                            except:
                                mydb.rollback()
                                print("_"*60)
                                print('Unsuccessful in Loading the data\n \t\t======= Please Try Again ========')
                                    
                        elif TYPE2 =='SAVING':
                            try:
                                mc.execute("update saving_acc set PASSWORD = '{}' where EMIRATESID ='{}' and NAME ='{}'".format(e,USERB,USER))
                                mydb.commit()
                            except:
                                mydb.rollback()
                                print("_"*60)
                                print('Unsuccessful in Saving the data')
                                        
                            try:
                                mc.execute("select * from saving_acc where NAME = '{}' and PASSWORD = '{}'".format(USER,e))
                                data=mc.fetchall()
                                if mc.rowcount>0:
                                    print("="*140)
                                    print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%45s'%'IDNO','%45s'%'EMIRATES-ID')
                                    print("="*140)
                                    for i in data:
                                        print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%40s'%i[5],'%40s'%i[6])
                                        print("_"*152)
                                        print("="*20)
                                        print("\n Account succesfully activated")
                                        print("_"*152)
                                        print("Your IDNO is : ",i[5])
                                        print("="*20)
                                        print()
                                        mydb.commit()

                            except:
                                mydb.rollback()
                                print("_"*60)
                                print('Unsuccessful in Loading the data\n \t\t======= Please Try Again ========')
                if found == False:
                    print('Please Try again')
    except:
        print("_"*60)
        print('Error occured while procedure')
        print("_"*60)
        mydb.rollback()
                        
                                   
#========================

def interest(NAME):
    try:
        mc.execute("select balance from saving_acc where name = '{}'".format(NAME[0]))
        data=mc.fetchone()
        DATA=data[0]
        if DATA <= 1000:
            interest =0.06
        elif DATA <= 5000:
            interest =0.5
        elif DATA <=10000:
            interest =2.6
        elif DATA <=20000:
            interest=3.1
        else:
            interest =4.2
        return(interest)
    except:
        print("ERROR")
        return()
    
    print("_"*60)

#========================
def interest_rate():
    print()
    print("_"*60)
    A=int(input("Enter the Password to continue further :"))
    print("_"*60)
    if A == 123456:
        ACCEPT=input("Start Process (YES/NO) : ")
        if ACCEPT.upper() :
            try:
                mc.execute("select name from saving_acc")
                data=mc.fetchall()
                for i in data:
                    INTEREST=interest(i)
                    try:
                        mc.execute("update saving_acc set balance = balance + (balance * {}/100)where name = '{}'".format(INTEREST,i[0]))
                        print("_"*80)
                        mydb.commit()
                    except:
                        print("Some error has occured")
                        mydb.rollback()
                        return()
                print("\t\t ================ Interest Succesfully Credited ================")
                print(' \t\t ================ SUCCESSFULLY SAVED ================')
                print("_"*80)
                
            except:
                print("\t\t============= Something Went wrong   ============")
                mydb.rollback
                    
                        
#========================

def acc_info():
    print("-"*60)
    print("===Account-Information===\n")
    print("-"*60)
    A=int(input("Enter your IDNO:"))
    print("_"*30)
    B=input("Enter your account Password:")
    print("_"*30)
    C=int(input("Enter account type(1. Checking/ 2. Saving ) : "))
    print("_"*30)
    if C == 1:
        try:
            print("-"*60)   
            mc.execute("select * from checking_acc where id={} and password ='{}' ".format(A,B))
            data=mc.fetchall()
            if mc.rowcount>0:
                print("="*120)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'IDNO','%40s'%'EMIRATES-ID')
                print("="*120)
                for i in data:
                    print(i[0],'%33s'%i[1],'%37s'%i[2],'%37s'%i[3],'%40s'%i[5],'%40s'%i[6])
                    mydb.commit()
                    print('+'*123)
            else:
                time.sleep(1)
                print("-"*60)
                print('\n===Entered idno or password was wrong, Please try again=== \n',"_"*50,"\n ===Please visit the bank for more enquiry===")
                print("-"*60) 
        except:
            mydb.rollback()
    if C == 2:
        try:
            print("-"*60)   
            mc.execute("select * from saving_acc where id={} and password ='{}' ".format(A,B))
            data=mc.fetchall()
            if mc.rowcount>0:
                print("="*120)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'IDNO','%40s'%'EMIRATES-ID')
                print("="*120)
                for i in data:
                    print(i[0],'%33s'%i[1],'%37s'%i[2],'%37s'%i[3],'%40s'%i[5],'%40s'%i[6])
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
    TYPE=input("Enter the account type  (CHECKING/SAVING) : ")
    TYPE2=TYPE.upper()
    print("_"*30)
    print("+"*40)
    
    print()
    if TYPE2 == 'CHECKING':
        try:
            mc.execute("select id,name,balance from checking_acc where id = {} and password='{}' ".format(Z,X))
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
                print("===The entered account number or password is incorrect=== \n \t\t===Please try again===")
                print("="*60)
                return
        except:
            mydb.rollback()
            print("Sorry the entered id or password is incorrect")
            return()
        A=int(input("Enter the amount to be deposited:"))
        if A >= 500 and A <= 20000:
            try:
                mc.execute("update checking_acc set balance = balance + {} where id = {}".format(A,Z))
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
            mc.execute("select id,name,balance from checking_acc where id = {} and password='{}' ".format(Z,X))
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
            
    elif TYPE2 == 'SAVING':
        try:
            mc.execute("select id,name,balance  from saving_acc where id = {} and password='{}' ".format(Z,X))
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
                print("===The entered account number or password is incorrect=== \n \t\t===Please try again===")
                print("="*60)
                return
        except:
            mydb.rollback()
            print("Sorry the entered id or password is incorrect")
            return()
        A=int(input("Enter the amount to be deposited:"))
        if A >= 500 and A <= 10000:
            try:
                mc.execute("update saving_acc set balance = balance + {} where id = {}".format(A,Z))
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
            mc.execute("select id,name,balance from checking_acc where id = {} and password='{}' ".format(Z,X))
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
    TYPE=input("Enter the account type you applied for (CHECKING/SAVING) : ")
    TYPE2=TYPE.upper()
    print("_"*30)
    print("+"*40)
    print()
    if TYPE2 =='CHECKING':
        try:
            print("-"*60)
            mc.execute("select id,name,balance from checking_acc where id = {} and password='{}' ".format(Z,X))
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
            return
            
        A=int(input("Enter the amount to be withdrawed:"))
        print("_"*30)
        if A >= 500 and A <= 15000:
            try:
                if TYPE2=='CHECKING':
                    mc.execute("select balance from checking_acc where id = {}".format(Z))
                    data=mc.fetchone()
                    AD=(data,)
                    print(AD)
                    if A <= AD[0] [0] [0]:
                        pass
                    else:
                        print("Entered amount is exceding the Bank balance")
            except:
                mydb.rollback
                print("ERROR")
            try:
                mc.execute("update checking_acc set balance = balance - {} where id = {}".format(A,Z))
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

        try:
            mc.execute("select id,name,balance from checking_acc where id = {} and password='{}' ".format(Z,X))
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
            return
            
    elif TYPE2 =='SAVING':
        try:
            print("-"*60)
            mc.execute("select id,name,balance from saving_acc where id = {} and password='{}' ".format(Z,X))
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
            return
            
        A=int(input("Enter the amount to be withdrawed:"))
        print("_"*30)
        if A >= 500 and A <= 10000:
            try:
                mc.execute("update saving_acc set balance = balance - {} where id = {}".format(A,Z))
                mydb.commit()
                print()
                print('Transaction in process...')
                time.sleep(1)
                print("===Successfully withdrawed===")
                print("Please collect the bill before leaving\n Thankyou for choosing Bank")
            except:
                mydb.rollback()
                return
        else:
            print("="*60)
            print("\nYour are only authorized to withdraw an amount according to the limiit set by the bank,For further queries please visit  any nearby of our branches")
            print("+"*80)
            return()
        try:
            mc.execute("select id,name,balance from saving_acc where id = {} and password='{}' ".format(Z,X))
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
            return

#=====================

def Transfer():
    print("-"*60)
    print("===Account balance transfering service===")
    print("-"*60)
    Z=int(input("Enter your  Account IDNO:"))
    print("_"*30)
    X=input("Enter your password:")
    print("_"*30)
    TYPE=input("Enter the account type you applied for (CHECKING/SAVING) : ")
    TYPE2=TYPE.upper()
    print("_"*30)
    print("+"*40)
    print()
    if TYPE2 == 'CHECKING':
        try:
            print("=== Current Account details  ===")
            mc.execute("select * from checking_acc where id = {} and password= '{}' ".format(Z,X))
            data=mc.fetchall()
            D=(data,)
            A=D
            if mc.rowcount>0:
                print("\n")
                print("="*140)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'IDNO','%45s'%'EMIRATES-ID')
                print("="*140)
                for i in data:
                    print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%37s'%i[5],'%40s'%i[6])
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
            return()
            
    elif TYPE2 == 'SAVING':
        try:
            print("=== Current Account details  ===")
            mc.execute("select * from saving_acc where id = {} and password= '{}' ".format(Z,X))
            data=mc.fetchall()
            D=(data,)
            A=D
            print(A)
            if mc.rowcount>0:
                print("\n")
                print("="*140)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'IDNO','%45s'%'EMIRATES-ID')
                print("="*140)
                for i in data:
                    print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%37s'%i[5],'%40s'%i[6])
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
            return()
    else:
        print('-'*60)
        print("\t\t ===== No such option available =====")
        print('-'*60)
        return()
    NAME=input("Enter the name of the Client: ")
    N=NAME.upper()
    M=len(N)
    if M > 25:
        print("Please enter a valid Name")
        return()
    print("_"*60)
    TRAN=int(input("Enter the account IDNO to which you would like to transfer the amount:"))
    if TRAN == Z :
        print()
        print("\t\t ============= Something went wrong =================")
        print()
    print("_"*30)
    TYPE=input("Enter the account type to which you are transfering the amount (CHECKING/SAVING) : ")
    TYPE3=TYPE.upper()
    print("_"*30)
    print()
    print("===Please be attentive and careful while doing the transactions===")
        
    AMOUNT=int(input("Enter the amount you would like to transfer:"))
    if AMOUNT > A[0] [0] [3]:
        print("_"*60)
        print("The amount is greater than the the amount available in your account,Please check and try again")
        print("_"*60)
        return()
    if TYPE2 =='CHECKING':
        if TYPE3 == 'CHECKING':
            try:
                mc.execute("select NAME,id from checking_acc where id = {} and NAME = '{}' ".format(TRAN,NAME))
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
                return()
        elif TYPE3 == 'SAVING':
            try:
                mc.execute("select NAME,id from saving_acc where id = {} and NAME = '{}' ".format(TRAN,NAME))
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
                return()
    elif TYPE2 =='SAVING':
        if TYPE3 == 'CHECKING':
            try:
                mc.execute("select NAME,id from checking_acc where id = {} and NAME = '{}' ".format(TRAN,NAME))
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
                return()
        elif TYPE3 == 'SAVING':
            try:
                mc.execute("select NAME,id from saving_acc where id = {} and NAME = '{}' ".format(TRAN,NAME))
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
                return()
       
    sure=input("Are you sure this is the correct account (YES/NO):")
    S=sure.upper()
    if S == "YES":
        print()
        print("Transfering the amount",AMOUNT,"to account IDNO :",TRAN," from IDNO:",Z)
        print()
        print("-"*60)
        if TYPE2 =='CHECKING':
            if TYPE3 == 'CHECKING':
                try:
                    mc.execute("update checking_acc set balance =balance - {} where id = {} ".format(AMOUNT,Z))
                    mc.execute("update checking_acc set balance =balance + {} where id = {} ".format(AMOUNT,TRAN))
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
                try:
                    print("=== Current Account details  ===")
                    mc.execute("select * from checking_acc where id = {} and password= '{}' ".format(Z,X))
                    data=mc.fetchall()
                    if mc.rowcount>0:
                        print("="*140)
                        print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'IDNO','%45s'%'EMIRATES-ID')
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
                        
            elif TYPE3 == 'SAVING':
                try:
                    mc.execute("update checking_acc set balance =balance - {} where id = {} ".format(AMOUNT,Z))
                    mc.execute("update saving_acc set balance =balance + {} where id = {} ".format(AMOUNT,TRAN))
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
                try:
                    print("=== Current Account details  ===")
                    mc.execute("select * from checking_acc where id = {} and password= '{}' ".format(Z,X))
                    data=mc.fetchall()
                    if mc.rowcount>0:
                        print("="*140)
                        print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'IDNO','%45s'%'EMIRATES-ID')
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
        elif TYPE2 == 'SAVING':
            if TYPE3 == 'CHECKING':
                try:
                    mc.execute("update saving_acc set balance =balance - {} where id = {} ".format(AMOUNT,Z))
                    mc.execute("update checking_acc set balance =balance + {} where id = {} ".format(AMOUNT,TRAN))
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
                try:
                    print("=== Current Account details  ===")
                    mc.execute("select * from saving_acc where id = {} and password= '{}' ".format(Z,X))
                    data=mc.fetchall()
                    if mc.rowcount>0:
                        print("="*140)
                        print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'IDNO','%45s'%'EMIRATES-ID')
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
                        
            elif TYPE3 == 'SAVING':
                try:
                    mc.execute("update saving_acc set balance =balance - {} where id = {} ".format(AMOUNT,Z))
                    mc.execute("update saving_acc set balance =balance + {} where id = {} ".format(AMOUNT,TRAN))
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
                try:
                    print("=== Current Account details  ===")
                    mc.execute("select * from saving_acc where id = {} and password= '{}' ".format(Z,X))
                    data=mc.fetchall()
                    if mc.rowcount>0:
                        print("="*140)
                        print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'IDNO','%45s'%'EMIRATES-ID')
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
    print("_"*30)
    X=input("Enter your password:")
    print("_"*30)
    Y=int(input("Enter account type(1. Checking/ 2. Saving ) : "))
    print("_"*30)
    print("+"*40)
    print()
    if Y == 1:
        try:
            print("=== Current Account details  ===")
            mc.execute("select * from checking_acc where id = {} and password='{}' ".format(Z,X))
            data=mc.fetchall()
            if mc.rowcount>0:
                print("="*140)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'PASSWORD','%45s'%'IDNO')
                print("="*140)
                for i in data:
                    print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%37s'%i[5],'%40s'%i[6])
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
            Nb=input("Enter your change of address: ")
            print("_"*30)
            Nc=input("Enter your new passcode  here: ")
            print("_"*30)
            try:
                mc.execute("update checking_acc set ADDRESS = '{}' , PASSWORD = '{}' where id = {} ".format(Nb,Nc,Z))
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
    elif Y ==2:
        try:
            print("=== Current Account details  ===")
            mc.execute("select * from saving_acc where id = {} and password='{}' ".format(Z,X))
            data=mc.fetchall()
            if mc.rowcount>0:
                print("="*140)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%40s'%'PASSWORD','%45s'%'IDNO')
                print("="*140)
                for i in data:
                    print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%37s'%i[5],'%40s'%i[6])
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
            Nb=input("Enter your change of address: ")
            print("_"*30)
            Nc=input("Enter your new passcode  here: ")
            print("_"*30)
            try:
                mc.execute("update saving_acc set ADDRESS = '{}' , PASSWORD = '{}' where id = {} ".format(Nb,Nc,Z))
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
    else:
        print("INVALID CHOICE")
        
#=====================

            
#============================================((ADMIN))================================================
        
def list_display():
    print('''========================================================
1) All user  application

2) Checking Account Details

3)Saving Account Details
========================================================\n''')
    A=int(input("Enter your option : "))
    if A == 1:
        try:
            mc.execute("select * from pending")
            data=mc.fetchall()
            if mc.rowcount>0:
                print("="*140)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%45s'%'Emirates-ID','%45s'%'Type','%45s'%'status','%45s'%'TEMP-PASS')
                print("="*150)
                for i in data:
                    print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%40s'%i[4],'%40s'%i[5],'%40s'%i[6],'%40s'%i[7])
                    print("_"*152)
            else:
                print("========")
                print("No data exists")
                print("========\n")
        except:
            mydb.rollback()
            print("_"*60)
            print('There no data available to be displayed')
    elif A == 2:
        try:
            mc.execute("select * from checking_acc")
            data=mc.fetchall()
            if mc.rowcount>0:
                print("="*140)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%45s'%'IDNO','%45s'%'EMIRATES-ID')
                print("="*140)
                for i in data:
                    print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%40s'%i[5],'%40s'%i[6])
                    print("_"*152)
            else:
                print("========")
                print("No data exists")
                print("========\n")
        except:
            mydb.rollback()
            print("_"*60)
            print('There no data available to be displayed')
    elif A == 3:
        try:
            mc.execute("select * from saving_acc")
            data=mc.fetchall()
            if mc.rowcount>0:
                print("="*140)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%45s'%'IDNO','%45s'%'EMIRATES-ID')
                print("="*140)
                for i in data:
                    print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%40s'%i[5],'%40s'%i[6])
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
    TYPE=input("Enter the account type (CHECKING/SAVING ) : ")
    TYPE.upper()
    print("+"*40)
    print()
    if TYPE == "CHECKING":
        try:
            print("=== Current Account details  ===")
            mc.execute("select * from checking_acc where id = {}".format(Z))
            data=mc.fetchall()
            if mc.rowcount>0:
                print("="*140)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%45s'%'IDNO')
                print("="*140)
                for i in data:
                    print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%45s'%i[5])
                    print("_"*150)
                    print()
        except:
            return()
    elif TYPE == "SAVING":
        try:
            print("=== Current Account details  ===")
            mc.execute("select * from saving_acc where id = {}".format(Z))
            data=mc.fetchall()
            if mc.rowcount>0:
                print("="*140)
                print('NAME','%40s'%'DOB','%40s'%'ADDRESS','%40s'%'AMOUNT','%45s'%'IDNO')
                print("="*140)
                for i in data:
                    print(i[0],'%37s'%i[1],'%37s'%i[2],'%37s'%i[3],'%45s'%i[5])
                    print("_"*150)
                    print()
        except:
            return()
        
    c=input("Do you want  to change any of the  account details? (YES/NO) : ")
    C=c.upper()
    if C =="YES":
        print()
        print("Performance of there acts are only authenticated to official personal, \any violating behaviour will result in sever charges\n")
        print("_"*60)
        Na=input("Enter customer new name : ")
        print("_"*30)
        Nb=input("Enter customer DOB  (YYYY/MM/DD: ")
        print("_"*30)
        Nc=input("Enter customer address here: ")
        print("_"*30)
        Nd=int(input("Enter customer balance here: "))
        if Nd >=500 and Nd <=99999:
            pass
        else:
            print("_"*30)
            print("Invalid ")
            print("_"*30)
        if TYPE == 'CHECKING':
            try:
                mc.execute("update checking_acc set NAME = '{}' , DOB = '{}',  ADDRESS = '{}' , BALANCE = {}  where id = {} ".format(Na,Nb,Nc,Nd,Z))
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
                print("_"*30)
                
        elif TYPE == 'SAVING':
            try:
                mc.execute("update saving_acc set NAME = '{}' , DOB = '{}',  ADDRESS = '{}' , BALANCE = {}  where id = {} ".format(Na,Nb,Nc,Nd,Z))
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
    
#+++++++++++++++++++++++++++++++
            
def new_acc():
    print()
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
    SELECT=input("Enter what type of Account  (Checking/Saving) : ")
    Z=SELECT.lower()
    if Z == "checking":
        print()
        print("\t\t===Please Enter the Follwoing Details===\n")
        a=input("Enter Full Name here: ")
        print("_"*30)
        M=len(a)
        if M > 30:
            print("Please enter a valid Name")
            return()
        b=input("\nPlease enter  DOB: ")
        print("_"*30)
        c=input("\nAddress: ")
        print("_"*30)
        C=c.upper()
        if C not in open(DATA_DIR / 'EMIRATES.txt').read():
            print()
            print("="*60)
            print("Please enter a valid emirate")
            return()
        d=int(input("Enter Emirates id:"))
        print("_"*30)
        if d == 15:
            pass

    elif Z == "saving":
        print("="*20)
        print()
        print("="*20)
        print()
        print("\t\t===Please Enter the Follwoing Details===\n")
        a=input("Enter Full Name here: ")
        print("_"*30)
        M=len(a)
        if M > 30:
            print("Please enter a valid Name")
            return()
        b=input("\nPlease enter DOB: ")
        print("_"*30)
        c=input("\nAddress: ")
        print("_"*30)
        C=c.upper()
        if C not in open(DATA_DIR / 'EMIRATES.txt').read():
            print()
            print("="*60)
            print("Please enter a valid emirate")
            return()
        d=input("Enter  Emirates id:")
        print("_"*30)
        if d == 15:
            pass
    else:
        print("="*40)
        print("\nPlease enter a viable option")
        print("="*40)
        return
        
    
    AF=int(input("\nEnter the amount of customer account(Should be more than 500) : "))
    print("-"*60)
    print("Please wait as your amount is being processed...")
    print("-"*60)
    time.sleep(1)
    print()
    if AF >= 500 and AF<= 99999:
        time.sleep(2)
        print("\nSuccessfully Saved")
        print("="*30)
    else:
        print('+'*64)
        print('please deposit an amount greater that 500 and below 99,999 to finish with the joining process to proceed further')
        print()
        return()
    A=a.upper()
    P="PCODESET"
    if Z == "checking" :
        try:
            mc.execute("insert into checking_acc values('{}','{}','{}',{},'{}',{},'{}')".format(A,b,C,AF,P,f,d))
            mc.execute("delete from pending where Name= '{}' ".format(A))
            print("="*20)
            print("+"*20)
            print("Account Created")
            mydb.commit()
        except:
            mydb.rollback()
            print("="*20)
            print("===Account creation not successful=== \n ===Please try again===")
            print("="*20)
            
    elif Z == "saving" :
        try:
            mc.execute("insert into saving_acc values('{}','{}','{}',{},'{}',{},'{}')".format(A,b,C,AF,P,f,d))
            mc.execute("delete from pending where Name= '{}' ".format(A))
            print("="*20)
            print("Application successfully saved\n")
            print("+"*20)
            print("Account Created")
            mydb.commit()
            
        except:
            mydb.rollback()
            print("="*20)
            print("===Account creation not successful=== \n ===Please try again===")
            print("="*20)
        
      
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
        apply()
    elif user == 2 :
        USER_passcre()
    elif user == 3 :
        print()
        acc_info()
    elif user == 4 :
        print()
        depo()
    elif user==5:
        print()
        withdrw()
    elif user==6:
        print()
        editor()
    elif user==7:
        print()
        Transfer()
    elif user==8:
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
                        interest_rate()
                        print("\nExiting admin prompt...")
                        print("="*40)
                        time.sleep(3)
                        break
                    elif admin == 5 :
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
