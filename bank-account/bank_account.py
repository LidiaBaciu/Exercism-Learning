import threading

class BankAccount:
    lock = threading.Lock()

    def __init__(self):
        self.isOpen = False
        self.balance = 0.0

    def get_balance(self):
        if not self.isOpen:
            raise ValueError("Account is closed.")
        
        with self.lock:
            return round(self.balance, 2)

    def open(self):
        if self.isOpen:
            raise ValueError("Account is already open.")

        with self.lock:
            self.isOpen = True

    def deposit(self, amount):
        if self.isOpen == False:
            raise ValueError("Account is closed.")
        if amount < 0.0:
            raise ValueError("Amount cannot be negative")

        with self.lock:
            self.balance += amount

    def withdraw(self, amount):
        if self.isOpen == False:
            raise ValueError("Account is closed.")
        if amount < 0.0:
            raise ValueError("Amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient balance.")
            
        with self.lock:
            self.balance -= amount

    def close(self):
        if self.isOpen == False:
            raise ValueError("Account is already closed.")

        with self.lock:
            self.isOpen = False
            self.balance = 0.0
