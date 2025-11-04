from db import connect

def create_account():
    name=input("Enter your First name = ")
    email=input("Enter your email address = ")
    mobile=input("Enter your mobile number")
    balance=float(input("Enter your opening balance = "))
    db=connect()
    cursor=db.cursor()
    sql="INSERT INTO accounts (name,email,mobile,balance) VALUES (%s,%s,%s,%s)"
    values=(name,email,mobile,balance)
    cursor.execute(sql,values)
    db.commit()
    print("Account Created successfully!")
    db.close()


def view_accounts():
    db=connect()
    cursor=db.cursor()
    cursor.execute("SELECT * FROM accounts")
    accounts=cursor.fetchall()
    print("All Accounts")
    for acc in accounts:
        print(f"Acc_No: {acc[0]}, Name: {acc[1]}, Email: {acc[2]},Mobile:{acc[3]}, Balance: {acc[4]}")
    db.close()


def deposit_money():
    acc_id=int(input("Enter Account Number: "))
    amount=float(input("Enter deposit amount: "))
    db=connect()
    cursor=db.cursor()
    cursor.execute("UPDATE accounts SET balance = balance + %s WHERE id=%s", (amount,acc_id))
    db.commit()
    print("Money Deposited successfully")
    db.close()


def withdraw_money():
    acc_id=int(input("Enter Account Number: "))
    amount=float(input("Enter amount to withdraw: "))
    db=connect()
    cursor=db.cursor()
    cursor.execute("SELECT balance FROM accounts WHERE id=%s", (acc_id,))
    result=cursor.fetchone()
    if result and result[0]>=amount:
        cursor.execute("UPDATE accounts SET balance = balance - %s WHERE id=%s", (amount,acc_id))
        db.commit()
        print("Withdrawal successfully")
    else:
        print("Insufficient balance")

    db.close()        
   

def check_balance():
     acc_id=int(input("Enter Account Number: "))
     db=connect()
     cursor=db.cursor()
     cursor.execute("SELECT name,balance FROM accounts WHERE id=%s",(acc_id,))
     result=cursor.fetchone()
     if result:
         print(f"Account Holder : {result[0]}, Blance : {result[1]}")
     else:
         print("Account not found")
     db.close()        


    
while True:
        print("\n Bank Management System")
        print("1.  Create Account")
        print("2.  View Accounts")
        print("3.  Deposit Money")
        print("4.  Withdraw Money")
        print("5.  Check Balance")
        print("6.  Exit")

        choice=input("Enter Your Choice: ")

        if choice=="1":
            create_account()
        elif choice=="2":
            view_accounts()
        elif choice=="3":
            deposit_money()
        elif choice=="4":
            withdraw_money()
        elif choice=="5":
            check_balance()
        elif choice=="6":
            print("Exiting System. Thank you!")
            break
        else:
            print("Invalid Choice. Please try again.")        