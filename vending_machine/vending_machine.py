class vending_machine:

    def __init__(self) -> None:
        self.money = 0

    def insert(self, add_money) -> None:
        self.money += add_money

    def get_total_amount(self) -> int:
        return self.money

    def refund(self) -> int:
        change = self.money
        self.money = 0
        return change
