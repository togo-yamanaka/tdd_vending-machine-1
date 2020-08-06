import pytest

from vending_machine.vending_machine import vending_machine

class TestVendingMachine:
    @pytest.mark.parametrize("input, expected", [(1, 0), (5, 0), (10, 10), (50, 50), (100, 100), (500, 500), (1000, 1000)])
    def test_insert(self, input, expected) -> None:
        machine = vending_machine()
        machine.insert(input)

        assert machine.get_total_amount() == expected

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
