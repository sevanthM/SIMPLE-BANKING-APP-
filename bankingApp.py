# properties and behavoirs(methods)
class Bank:
    
    balance = 1000    

    def __init__(self):       
            self.username = input('Enter name:')
            
            self.bankName = input('Enter bank branch:')
        
            self.accNum = int(input('Enter last 4 digits in Acc no:'))
            
            
            
    def addAmount(self):
            self.addAmt = int(input('Enter Amt to deposit:'))
        
            self.balance=self.balance+self.addAmt    
        
            print(f'current balance:{self.balance}')        


            
    def withdrawAmt(self):        
            self.withdrwAmt = int(input('Enter Amt to withdraw:'))
        
            if (self.withdrwAmt > self.balance):
                print('insufficient balance! ')
            else:
                self.balance=self.balance-self.withdrwAmt
            print(f'current balance:{self.balance}')        


        
    def showBalance(self):
            print(f"current balance:{self.balance}")
    
    

user = Bank()

print(f"hello! {user.username}")
while True:
    print('''
         >>. To Add Amt press 1:
         >>. To Withdraw Amt press 2:
         >>. To view balance press 3:
         >>. press 0! to exit 
         ''')
    pickOption = int(input('Enter Action:'))

    if pickOption==1:
            user.addAmount()

    elif pickOption==2:
            user.withdrawAmt()

    elif pickOption==3:
            user.showBalance()
    
    elif pickOption==0:
            print('done!')
            break
        
