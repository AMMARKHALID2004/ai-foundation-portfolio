class Phone:
    def __init__(self, name, model,year):
        print("Executing parent constructor")
        self.name = name
        self.mode = model
        self.year=2026
    def print_year(self):
        print(self.year)