import pytest

from vending_machine.vending_machine import vending_machine

class TestVendingMachine:
    @pytest.mark.parametrize("input, total_amount, return_money",
    [(1, 0, 1), (5, 0, 5), (10, 10, None), (50, 50, None), (100, 100, None), (500, 500, None), (1000, 1000, None)])
    def test_insert(self, input, total_amount, return_money) -> None:
        machine = vending_machine()
        change = machine.insert(input)

        assert machine.get_total_amount() == total_amount
        assert change == return_money

    def test_get_total_amount(self) -> None:
        machine = vending_machine()
        machine.insert(10)
        machine.insert(50)
        machine.insert(100)
        machine.insert(500)
        machine.insert(1000)

        assert machine.get_total_amount() == 1660

    def test_refund(self) -> None:
        machine = vending_machine()
        machine.insert(10)
        machine.insert(50)
        machine.insert(100)
        machine.insert(500)
        machine.insert(1000)

        assert machine.refund() == 1660
        assert machine.get_total_amount() == 0
