from fpdf import FPDF

class Bill:
    """
    Object that contains data about a bill, such as total amount
    and period of the bill
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains data about a flatmate, such as name, days in the house
    the flatmate pays a share of the bill
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight
        return to_pay

class PdfReport:
    """
    Creates a PDF files that contains data about the flatmates such as
    their names, their due amount and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))

        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()

        # Add Icon
        pdf.image("house.png", w=30, h=30)

        # Insert Title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt="Flatmates Bill", border=1, align="C", ln=1)

        # Insert Period label and value
        pdf.cell(w=100, h=40, txt="Period:", border=1)
        pdf.cell(w=200, h=40, txt=bill.period, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate1.name, border=1)
        pdf.cell(w=200, h=40, txt=flatmate1_pay, border=1, ln=1)

        # Insert name and due amount of the first flatmate
        pdf.cell(w=100, h=40, txt=flatmate2.name, border=1)
        pdf.cell(w=200, h=40, txt=flatmate2_pay, border=1, ln=1)

        pdf.output(self.filename)


the_bill = Bill(amount=120, period="February 2021")
Tom = Flatmate(name="Tom", days_in_house=20)
Sean = Flatmate(name="Sean", days_in_house=25)

print("Tom pays: ", Tom.pays(the_bill, Sean))
print("Sean pays: ", Sean.pays(the_bill, Tom))

pdf_report = PdfReport(filename="Report1.pdf")
pdf_report.generate(flatmate1=Tom, flatmate2=Sean, bill=the_bill)
