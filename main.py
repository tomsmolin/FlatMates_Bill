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

    def pays(self, bill):
        pass


class PdfReport:
    """
    Creates a PDF files that contains data about the flatmates such as
    their names, their due amount and the period of the bill
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pass



