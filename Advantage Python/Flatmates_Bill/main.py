import webbrowser
from fpdf import FPDF

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

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PDFReport:
    '''
    Generate a PDF withe the name of the flatemates, the period and how much have to pay
    '''

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):

        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        #Add icon
        pdf.image(name='house.png', w=30, h=30)

        #insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmate Bill', border=0, align='C', ln=1)

        #insert period label and value
        pdf.set_font(family='Times', size=14, style='B')
        pdf.cell(w=100, h=40, txt='Period', border=0)
        pdf.cell(w=150, h=40, txt=bill.period, border=0, ln=1)

        #insert name and due amount of the first flatmate
        pdf.set_font(family='Times', size=12)
        pdf.cell(w=100, h=25, txt=flatmate1.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate1_pay, border=0, ln=1)

        #insert name and due amount of the first flatmate
        pdf.cell(w=100, h=25, txt=flatmate2.name, border=0)
        pdf.cell(w=100, h=25, txt=flatmate2_pay, border=0)

        pdf.output(self.filename)

        #Open the pdf automatically
        webbrowser.open(self.filename)


amount = float(input('Hey user, enter the bill amount: '))
period = input('What is the period?: ')
flatmate1 = input('What is the name of one flatmate?: ')
days_in_house = int(input(f'How many days did {flatmate1} stay in the house during the bill perios? '))
flatmate2 = input('What is the name of the other flatmate?: ')
days_in_house2 = int(input(f'How many days did {flatmate2} stay in the house during the bill perios? '))

a_bill = Bill(amount=amount, period=period)
mate1 = Flatmate(name=flatmate1, days_in_house=20)
mate2 = Flatmate(name=flatmate2, days_in_house=25)

print(f'{flatmate1} pays: ', mate1.pays(bill=a_bill, flatmate2=mate2))
print('Marry pays: ', mate2.pays(a_bill, mate1))

pdf_report = PDFReport(filename=f'{a_bill.period}.pdf')
pdf_report.generate(flatmate1=mate1, flatmate2=mate2, bill=a_bill)