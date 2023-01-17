class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return True
        else:
            return False

    def get_balance(self):
        return self.__balance

# Membuat objek dari class BankAccount
my_account = BankAccount(1000)

# Menyetor uang ke rekening
my_account.deposit(500)

# Menarik uang dari rekening
if my_account.withdraw(200):
    print("Tarik uang berhasil")
else:
    print("Saldo tidak cukup")

# Cek saldo
print(my_account.get_balance())
