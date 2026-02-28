"""Strategy Pattern Example: Payment Methods"""

from abc import ABC, abstractmethod
# Strategy Interface
class PaymentStrategy(ABC):
	@abstractmethod
	def pay(self, amount: float) -> None:
		pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def __init__(self, card_number: str, card_holder: str, cvv: str, expiry_date: str):
        
        self.card_number = card_number
        self.card_holder = card_holder
        self.cvv = cvv
        self.expiry_date = expiry_date

    def pay(self, amount: float) -> None:
        print(f"Paid ${amount:.2f} using Credit Card ({self.card_number[-4:]})")

class PayPalPayment(PaymentStrategy):
	def __init__(self, email: str):
		self.email = email

	def pay(self, amount: float) -> None:
	    print(f"Paid ${amount:.2f} using PayPal account {self.email}")

class BitcoinPayment(PaymentStrategy):
	def __init__(self, wallet_address: str):
		self.wallet_address = wallet_address

	def pay(self, amount: float) -> None:
	    print(f"Paid ${amount:.2f} using Bitcoin wallet {self.wallet_address[:6]}...{self.wallet_address[-4:]}")

# Context
class PaymentContext:
	def __init__(self, strategy: PaymentStrategy):
		self._strategy = strategy

	def set_strategy(self, strategy: PaymentStrategy) -> None:
		self._strategy = strategy

	def pay(self, amount: float) -> None:
	    self._strategy.pay(amount)


# Example usage
if __name__ == "__main__":
    
    print("Strategy Pattern Example: Payment Methods\n")
	# Choose payment strategies
    credit_card = CreditCardPayment(
		card_number="1234567890123456",
        card_holder="John Doe",
        cvv="123",
        expiry_date="12/28"
	)
    print("Created Initial payment method: Credit Card")
    paypal = PayPalPayment(email="john.doe@example.com")
    bitcoin = BitcoinPayment(wallet_address="1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
	# Context with initial strategy
    context = PaymentContext(credit_card)
    context.pay(100.0)

	# Switch to PayPal
    context.set_strategy(paypal)
    context.pay(250.0)

    # Switch to Bitcoin
    context.set_strategy(bitcoin)
    context.pay(500.0)