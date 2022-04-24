from flat import Bill, Flatmate, PDFReport

amount = float(input('Hey user, enter the bill amount: '))
period = input('What is the period?: ')

name1 = input('What is the name of one flatmate?: ')
days_in_house = int(input(f'How many days did {name1} stay in the house during the bill perios? '))

name2 = input('What is the name of the other flatmate?: ')
days_in_house2 = int(input(f'How many days did {name2} stay in the house during the bill perios? '))

a_bill = Bill(amount=amount, period=period)
mate1 = Flatmate(name=name1, days_in_house=days_in_house)
mate2 = Flatmate(name=name2, days_in_house=days_in_house2)

print(f'{name1} pays: ', mate1.pays(bill=a_bill, flatmate2=mate2))
print('Marry pays: ', mate2.pays(a_bill, mate1))

pdf_report = PDFReport(filename=f'{a_bill.period}.pdf')
pdf_report.generate(flatmate1=mate1, flatmate2=mate2, bill=a_bill)