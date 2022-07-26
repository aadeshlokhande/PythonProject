#candidate=input("Enter your Name = ")
#if(candidate=="X"):
#    print("Hello X .Your Education is M.B.B.S .Contact number = 8247591837")
#elif(candidate=="Y"):
#elif(candidate=="Z"):
#   print("Hello Z . Your Education is B.Arch . Contact number = 8782398569")
#else:
#    print("no match ")

#Payment Authorization. The first stage of any credit card transaction is payment. ...
#Payment Authentication. The issuing bank receives the payment request and verifies
#whether the cardholder has the available balance to make the purchase. ...
#Clearing.


"""Log on to Axis Bank Internet Banking.
Go to Credit Card section.
Select the Credit Card for which payment needs to be done.
Click on “Pay Now”
Select the Account to be debited.
Enter Amount you wish to pay."""


print("************************Credit Card Processing Works*********************************")
credit_card=input("Want to pay using card \CVV = ")
if (credit_card in ["YES", "yes", "ha" , "haa"]):
    print("Payment authentification process ")
    process=input("Click pay now yes or no = ")
    if (process=="yes"):
        print("Select account ")
        account=input("Enter your account = ")
        if(account in ["ICICI Bank", "Axis Bank" ,"HDFC Bank"]):
            amount=int(input("Amount you wish to pay = "))
            if(amount<100000):
                print("The issuing bank receives the payment request and verifies whether the cardholder has the available balance to make the purchase.")
            else:
              print("Insufficient Balance ")
        else:
            print("Enter valid account name ")
    else:
        print("please enter yes ")
else:
    print("Go to home")
