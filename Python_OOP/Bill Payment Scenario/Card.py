from Bill import Bill
class Card(Bill):

    def pay_bill(self):
        print(f"The bill of Rs. {self.bill} has been paid through card payment. ")