from abc import ABC, abstractmethod


class PaymentStrategy:

    @abstractmethod
    def pay(self, amount):
        pass


class CashPaymentStrategy(PaymentStrategy):

    def pay(self, amount):
        confirmation = f"Successfully paid {amount} using cash"
        print(confirmation)


class ABBankPaymentStrategy(PaymentStrategy):

    def pay(self, amount):
        confirmation = f"Successfully paid {amount} using AB Bank"
        print(confirmation)


class BkashPaymentStrategy(PaymentStrategy):

    def pay(self, amount):
        confirmation = f"Successfully paid {amount} using Bkash"
        print(confirmation)
