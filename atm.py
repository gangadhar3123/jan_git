#simple atm progrm
#atm programme using conditional statements
#feb batch
a='''
1 deposit
2 withdraw
3 balance enquiry
'''
name="reddy"
password="312312"
print("welcome to  SBI bank ATM")
user_name=input("enter the user name:")
pass_word=input("enter the password:")
balance=1000
if name==user_name and password==pass_word:
  while True:  
    print(a)  
    option=int(input("enter tour option:"))
    if option==1:
      credit_amount=float(input("enter the amount:"))
      if credit_amount<=0:
          print("please enter a positive amount:")
      else:
          balance+=credit_amount
          print("deposit seccessfully,your new balance is:",balance)
    elif option==2:
      debit_amount=float(input("enter the amount:"))
      if debit_amount<=balance:
       balance-=debit_amount
       print("withdrawl successfully,your new balance is:",balance)
      else:
          print("insufficeint funds")
    elif option==3:
      print("your current balance is:",balance)
    elif option==4:
        print("exit")
        break
    else:
      print("invalid transaction type")
      break
else:
    print("invalid details")   
