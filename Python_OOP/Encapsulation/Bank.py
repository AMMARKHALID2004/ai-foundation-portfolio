class Bank:
    def __init__(self):
        self.__name=""
        self.__account_number=""
        self.__pin=0
        self.__balance=0

    def get_name(self):
        return self.__name
    def set_name(self, name):
        if isinstance(name,str):
         self.__name=name
        else:
           raise ValueError("Write Valid Name: ")

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        if isinstance(account_number,str):
         self.__account_number = account_number
        else:
            print("Enter a valid account number: ")

    def get_pin(self):
        return self.__pin

    def set_pin(self,pin):

        if isinstance(pin,int):
         self.__pin = pin
        else:
            print("Enter valid pin: ")
    def get_balance(self):
        return self.__balance

    def set_balance(self, balance):
        if isinstance(balance,int):
         self.__balance = balance
        else:
            print("Enter valid balance: ")

