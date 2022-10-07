from .models import Transaction
from .service import pay_transaction, cancel_transaction
from clickuz import ClickUz
from decimal import Decimal


class CheckClickTransaction(ClickUz):
    def check_order(self, order_id: str, amount: str):
        try:
            transaction = Transaction.objects.get(id=int(order_id))
            if transaction.total_price != Decimal(amount):
                return self.INVALID_AMOUNT
            transaction.verify()
        except Transaction.DoesNotExist:
            return
        return self.ORDER_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        try:
            transaction = Transaction.objects.get(id=int(order_id))
            transaction.make_payment()
        except Transaction.DoesNotExist:
            return
