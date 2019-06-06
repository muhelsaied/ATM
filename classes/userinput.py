from  classes.transicraption import Operation
class USER :
    def __init__(self, balance, bank_name, name):
        self.balance = balance
        self.bank_name = bank_name
        self.name = name
        self.account_change = []

    #     bank name
    def welcome_messsage(self):
        print(f'{self.bank_name}')

    #  user information
    def user_inf(self):
        print(f'welcome back {self.name}')

    # check balance
    def check_balance(self):
        print(f'your balance is {self.balance}')

    #  cash process
    def get_cash(self):
        try:
            moneyInput = input('please input amount of money : ')
            moneyInput = int(moneyInput)
        except ValueError:
            print("your input must be a number")
            self.get_cash()
        try:
            confirmInput = input("please confirm your amount operation  : ")
            confirmInput = int(confirmInput)
        except ValueError:
            print("your input must be a number")
            self.get_cash()
        if confirmInput == moneyInput:
            Operation.pullMoney(self,confirmInput)
        else:
            print('your two value must be identical')
            self.get_cash()

    #     select option
    def choice_option(self):
        try:
            option = input('select operation : ')
            option = int(option)
        except ValueError:
            print('please select only number')
            self.input_option()
        if (option == 1):
            self.check_balance()
        elif (option == 2):
            self.get_cash()
        elif (option == 3):
            Operation.show_Changes(self)
        else:
            print('please select a valid option')
            self.choice_option()

    # quit program
    def quit(self):
        try:
            otherOpition = input('would you like to preform another operation (y - n): ')
        except Exception as e:
            print(e)
        if (otherOpition == "y") or (otherOpition == "") :
            self.input_option()
        elif(otherOpition == "n"):
            print(f'thank you for your trust in {self.bank_name}')
        else:
            print('please select a valid option')
            self.quit()

    #  user option
    def input_option(self):
        print(f'please choice an operation :\n'
              f'    1-check your balance \n'
              f'    2-get some cash\n'
              f'    3-get all transcription history')
        self.choice_option()
        self.quit()




