class Account:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"{self.name} {self.phone_number} {self.email}"

a1 = Account("Todd,", "(432)908-9560",", todd.tran@snhu.edu")
a2 = Account("Selena,", "(602)853-3325", ", selena.gomez@snhu.edu")

class Flag:
    def __init__(self, name, date, priority, open, description):
        self.name = name
        self.date = date
        self.priority = priority
        self.open = open
        self.description = description

    def __str__(self):
        return f"{self.name}{self.date}{self.priority}{self.open}{self.description}"

f1 = Flag("Michelle,", "12/4/24", "Priority 5,", "open flag", "Computer is not turning on.")
f2 = Flag("Ethan,", "12/3/24", "Priority 2,", "closed flag", "Could not connect to Wi-Fi.")

class OxfordCorpEmployee:
    pass

class Tech:
    pass

class Manager:
    pass

print(a1)
print(a2)
print(f1)
print(f2)






