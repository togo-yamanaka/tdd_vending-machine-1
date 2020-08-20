import pytest

from vending_machine.vending_machine import VendingMachine, Coin


class TestVendingMachine:
    # @pytest.mark.parametrize(
    #     "input, total_amount, return_money",
    #     [
    #         (1, 0, 1),
    #         (5, 0, 5),
    #         (10, 10, None),
    #         (50, 50, None),
    #         (100, 100, None),
    #         (500, 500, None),
    #         (1000, 1000, None),
    #     ],
    # )
    def test_insert(self):  # , input, total_amount, return_money) -> None:
        machine = VendingMachine()
        coin = Coin(50)

        machine.insert(coin)

        assert machine.get_total_amount() == coin.amount

    def test_get_total_amount(self) -> None:
        machine = VendingMachine()
        machine.insert(Coin(10))
        machine.insert(Coin(50))
        machine.insert(Coin(100))
        machine.insert(Coin(500))
        machine.insert(Coin(1000))

        assert machine.get_total_amount() == 1660

    def test_refund(self) -> None:
        machine = VendingMachine()
        machine.insert(Coin(10))
        machine.insert(Coin(50))
        machine.insert(Coin(100))
        machine.insert(Coin(500))
        machine.insert(Coin(1000))

        assert machine.refund() == 1660
        assert machine.get_total_amount() == 0

    def test_invalid_coin_generate(self):

        try:
            Coin(320)
        except Exception as e:
            assert e.message == "正常なコインではありません"
