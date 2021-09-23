class Banking:

   

  
       @property
       def depositor(self):
           
               print("Deposite:")
               Name = input("What is your name?")
               Account_Number = input("Enter the Account Number:")
               Account_Number = int(Account_Number)
               Ifsc_code = input("Enter the ifsc code:")
               Amount = input("Enter the amount:")
               Amount = int(Amount)
               print("Application Form:")
               print(f"The Entered name is {Name}")
               print(f"The Entered Account Number is {Account_Number}")
               print(f"The Entered IFSC Code is {Ifsc_code}")
               print(f"The Entered Amount is {Amount}")
               print("Confirmation message:")
               print(f"Amount is successfully debited in Account  number:{Account_Number}")
    
   
       @property 
       def transaction(self):
           print("/n/n")
           print("The transaction:")
           print("Enter the card")
           user = input("choose the account type")
           type = ['savings account' , 'current account']
           if user in type :
               language1 = input("choose language :")
               language = ['English' , 'German' , 'French']
               if language1 in language :
                    print(f"{language1} is accessible , continue")
                    Pin_no = input("Enter pin no:")
                    Pin_no = int(Pin_no)
                    Money = input("enter the amount:")
                    Money = int(Money)
                    print("The transaction in processing....")
                    print("collect your cash")
                    print(f"The amount of {Money} has been successfully credited" )




      


Saving_money = Banking()
Saving_money.depositor
Saving_money.transaction


