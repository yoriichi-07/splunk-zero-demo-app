import logging
import logging.config
import os

# Load logging configuration
logging.config.fileConfig('logging.conf')

logger = logging.getLogger('payment')

class PaymentService:
    """Handles payment processing for the platform."""

    def process_payment(self, user_id: str, amount: float, currency: str = "USD"):
        logger.debug(f"Starting payment processing for user {user_id}")
        logger.debug(f"Payment details: amount={amount}, currency={currency}")
        logger.debug(f"Validating payment parameters...")

        if amount <= 0:
            logger.error(f"Invalid payment amount: {amount}")
            raise ValueError("Payment amount must be positive")

        logger.debug(f"Connecting to payment gateway...")
        logger.debug(f"Gateway connection established")
        logger.debug(f"Sending payment request: user={user_id}, amount={amount} {currency}")

        # Simulate payment processing
        transaction_id = f"TXN-{user_id}-{int(amount * 100)}"

        logger.debug(f"Payment gateway responded with transaction_id={transaction_id}")
        logger.debug(f"Verifying transaction status...")
        logger.debug(f"Transaction verified successfully")
        logger.info(f"Payment processed: {transaction_id} for ${amount}")

        return transaction_id

    def refund_payment(self, transaction_id: str):
        logger.debug(f"Starting refund for transaction {transaction_id}")
        logger.debug(f"Looking up original transaction...")
        logger.debug(f"Original transaction found, initiating refund...")
        logger.info(f"Refund processed for {transaction_id}")
        return True


if __name__ == "__main__":
    service = PaymentService()
    service.process_payment("user-123", 49.99)
    service.process_payment("user-456", 199.00)
    service.refund_payment("TXN-user-123-4999")
