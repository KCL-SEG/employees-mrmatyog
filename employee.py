"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contract, commission):
        self.name = name
        self.contract = contract
        self.commission = commission

    def get_pay(self):
        return self.contract.get_pay() + self.commission.get_pay()

    def __str__(self):
        return f"{self.name} works on a {self.contract}{self.commission}. Their total pay is {self.get_pay()}."

class Contract:
    def __init__(self, type, wage):
        self.type = type
        self.wage = wage

    def get_pay(self):
        if self.type == "monthly":
            return self.wage["pay"]
        elif self.type == "hourly":
            return self.wage["hours"] * self.wage["rate"]

    def __str__(self):
        if self.type == "monthly":
            return f"{self.type} salary of {self.wage['pay']}"
        elif self.type == "hourly":
            return f"contract of {self.wage['hours']} hours at {self.wage['rate']}/hour"

class Commission:
    def __init__(self, type, earnings = 0):
        self.type = type
        self.earnings = earnings

    def get_pay(self):
        if self.type == "none":
            return 0
        elif self.type == "contract":
            return self.earnings["number"] * self.earnings["rate"]
        elif self.type == "bonus":
            return self.earnings["pay"]

    def __str__(self):
        if self.type == "none":
            return f""
        elif self.type == "contract":
            return f" and receives a commission for {self.earnings['number']} contract(s) at {self.earnings['rate']}/contract"
        elif self.type == "bonus":
            return f" and receives a {self.type} commission of {self.earnings['pay']}"

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie =    Employee('Billie', 
            Contract("monthly", {"pay" : 4000}), 
            Commission("none"))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie =   Employee('Charlie', 
            Contract("hourly", {"hours" : 100, "rate" : 25}), 
            Commission("none"))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee =     Employee('Renee', 
            Contract("monthly", {"pay" : 3000}), 
            Commission("contract", {"number" : 4, "rate" : 200}))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan =       Employee('Jan', 
            Contract("hourly", {"hours" : 150, "rate" : 25}), 
            Commission("contract", {"number" : 3, "rate" : 220}))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie =    Employee('Robbie', 
            Contract("monthly", {"pay" : 2000}), 
            Commission("bonus", {"pay" : 1500}))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel =     Employee('Ariel', 
            Contract("hourly", {"hours" : 120, "rate" : 30}), 
            Commission("bonus", {"pay" : 600}))
