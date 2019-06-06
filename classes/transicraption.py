import datetime

time = datetime.datetime.now()
date_time = time.strftime("%m/%d/%Y, %H:%M:%S")
class Operation:
    def __init__(self,balance):
        self.balance = balance
        self.account_change = []
    # main function to deal with credit
    def pullMoney( self, request):
        cash = 0
        papers = [100,50,20,10,5]
        if request <= self.balance :
            if request > 0 :
                for paper in papers:
                    while request >= paper :
                        request -= paper
                        cash += paper
                        self.balance -= paper
            if request < 10 :
                print(f'your request : {request}  \n'
                     f'you must provide more at least 10 $ to preform operation\n')
                cash_request = {
                    "cash":cash,
                    "time":date_time,
                    "balance":self.balance
                }
                self.account_change.append(cash_request)
                print(f'cash : {cash} \nbalance : {self.balance} ')
            else:
                print('can not preform request,pls input at least 10 $')
        else:
            print('sorry u dont have enough credits in you account')
    def show_Changes(self):
        print('your transcripation  details :')
        for operation in self.account_change :
            print(f'your withdraw {operation["cash"]} $ from your account at {operation["time"]}'
                  f' your balance : {operation["balance"]} $')
