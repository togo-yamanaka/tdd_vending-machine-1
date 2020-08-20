class Coin(object):
    def __init__(self, amount) -> None:
        self.amount = amount


class Juice(object):
    price_dict = {"コーラ": 120}

    def __init__(self, name):
        self.name = name
        self.price = self.price_dict["コーラ"]


class VendingMachine:
    def __init__(self) -> None:
        self.coin_list = []
        self.available_amount = [10, 50, 100, 500, 1000]
        self.juice_dict = {"コーラ": {"juice": Juice("コーラ"), "stock": 5}}

    def insert(self, money: int) -> int:

        if money in self.available_amount:
            self.coin_list.append(Coin(money))
            return 0
        else:
            return money

    def get_total_amount(self) -> int:
        if self.coin_list:
            result = sum([coin.amount for coin in self.coin_list])
        else:
            result = 0
        return result

    def refund(self) -> int:
        result = self.get_total_amount()
        self.coin_list = []
        return result

    def check_stock(self, name: str) -> int:
        return self.juice_dict[name]["stock"]

    def check_price(self, name: str) -> int:
        juice = self.juice_dict[name]["juice"]
        return juice.price
