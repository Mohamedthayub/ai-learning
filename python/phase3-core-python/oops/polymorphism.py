class  UPI:
    def pay(self,amount):
        print(f"Paid {amount} using Credit Card")

class PayPal:
    def pay(self,amount):
        print(f"Paid {amount}  using Paypal UPI")


class Bank:
    def pay(self,amount):
        print(f"Paid {amount} using Challen Method")


upi = UPI()
paypal = PayPal()
bank = Bank()

upi.pay(2000)
paypal.pay(10000)
bank.pay(5000)