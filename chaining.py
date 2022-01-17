class User:

    def __init__(self, first_name, last_name, email_address):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self # required to return self for chaining

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self # required to return self for chaining

    def display_user_balance(self):
        print(f"User: {self.first_name} {self.last_name}, Balance: {self.account_balance}")
        return self # required to return self for chaining

James = User("James", "Holden", "jamesholden@expanse.com")
Naomi = User("Naomi", "Nagata", "naominagata@expanse.com")
Camina = User("Camina", "Drummer", "caminadrummer@expanse.com")

James.make_deposit(500).make_deposit(32).make_deposit(290).make_withdrawal(100).display_user_balance()
Naomi.make_deposit(1000).make_deposit(312).make_withdrawal(200).make_withdrawal(25).display_user_balance()
Camina.make_deposit(3000).make_withdrawal(200).make_withdrawal(20).make_withdrawal(150).display_user_balance()
