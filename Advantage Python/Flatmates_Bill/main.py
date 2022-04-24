class Bill:
    '''
    Object that contains data about a bill, such as total amout and period of the bill
    '''

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    '''
    Create a flatmate person who lives in the flat and pays a share of the bill.
    '''

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill):
        return bill.amount/2

class PDFReport:
    '''
    Generate a PDF withe the name of the flatemates, the period and how much have to pay
    '''

    def __init__(self, filename):
        self.filename = filename

    def generate(self):
        pass

a_bill = Bill(amount=200, period='March 2020')
john = Flatmate(name='John', days_in_house=20)
marry = Flatmate(name='Marry', days_in_house=25)

print(john.pays(bill=a_bill))
