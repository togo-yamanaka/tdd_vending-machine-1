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
        assert machine.insert(50) == 0
        assert machine.get_total_amount() == 50

        machine2 = VendingMachine()
        assert machine2.insert(320) == 320
        assert machine2.get_total_amount() == 0

    def test_get_total_amount(self) -> None:
        machine = VendingMachine()
        machine.insert(10)
        machine.insert(50)
        machine.insert(100)
        machine.insert(500)
        machine.insert(1000)

        assert machine.get_total_amount() == 1660

    def test_refund(self) -> None:
        machine = VendingMachine()
        machine.insert(10)
        machine.insert(50)
        machine.insert(100)
        machine.insert(500)
        machine.insert(1000)

        assert machine.refund() == 1660
        assert machine.get_total_amount() == 0

    def test_juice(self):
        machine = VendingMachine()

        assert machine.check_stock("コーラ") == 5
        assert machine.check_price("コーラ") == 120
