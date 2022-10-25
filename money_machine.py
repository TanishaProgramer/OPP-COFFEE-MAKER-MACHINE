class MoneyMachine:
    
    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f'Money: {self.CURRENCY}{self.profit} ')

    def proccess_coins(self):
        print("please inser coins. ")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f'How many {coin}?: ')) 
        
        return self.money_received

    def make_payment(self, cost):
        self.proccess_coins()
        if self.money_received >= cost:
            change = round(self.money_received - cost, 2)
            print(f'Here is {self.CURRENCY}{change} in change.')
            self.profit += cost
            self.money_received = 0

        else:
            print("Sorry that's not change money. Money refunded.")
            self.money_received = 0
            return False