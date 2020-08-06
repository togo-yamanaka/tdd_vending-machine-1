from vending_machine.vending_machine import vending_machine

class TestVendingMachine:
    def test_insert(self) -> None:
        input = 100

        machine = vending_machine()
        machine.insert(input)

        assert machine.get_total_amount() == input

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
