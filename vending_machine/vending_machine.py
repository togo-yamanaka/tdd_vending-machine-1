class Coin(object):
    def __init__(self, amount) -> None:
        self.available_amount = [10, 50, 100, 500, 1000]

        if amount in self.available_amount:
            self.amount = amount
        else:
            raise Exception("正常なコインではありません")


class VendingMachine:
    def __init__(self) -> None:
        self.coin_list = []

    def insert(self, coin: Coin) -> None:
        self.coin_list.append(coin)

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

