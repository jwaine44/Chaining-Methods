class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self                                     # For chaining need to have the functions return self

    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self                                     # For chaining need to have the functions return self

    def display_user_balance(self):
        print("User:", str(self.name + ","), "Balance:", self.account_balance)

    def transfer_money(self, other_user, amount):       # For chaining need to have the functions return self
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

# Create three instances of class

eren = User("Eren Yeager", "eren.yeager@titan.com")
mikasa = User("Mikasa Ackerman", "mikasa.ackerman@titan.com")
reiner = User("Reiner Braun", "reiner.braun@titan.com")

# First user makes 3 deposits and one withdrawal, transfers money to third user, and display the balance

eren.make_deposit(10).make_deposit(600).make_deposit(40).make_withdrawal(50).transfer_money(reiner, 200).display_user_balance()

# Second user makes 2 deposits and 2 withdrawals and display the balance

mikasa.make_deposit(100).make_deposit(200).make_withdrawal(50).make_withdrawal(10).display_user_balance()

# Third user makes 1 deposit and 3 withdrawals and display the balance

reiner.make_deposit(500).make_withdrawal(15).make_withdrawal(25).make_withdrawal(60).display_user_balance()