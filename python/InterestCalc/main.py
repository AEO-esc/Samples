class loanCalculator():
    def __init__(self) -> None:
        principal = 0.0
        apr = 0.0
        years = 0
        monthlyPayment = 0.0
        propTax = 0.0
        taxes = 0.0

    def loanCalcHelper(self):
        self.principal = float(input("Input the loan amount: "))
        self.apr = float(input("Input the annual interest rate: "))
        self.years = int(input("Input amount of years: "))
        self.propTax = float(input("Input your county's property tax: "))

    def calcInterest(self):
        monthlyInterestRate = self.apr / 1200
        amountOfMonths = self.years * 12
        self.monthlyPayment = self.principal * monthlyInterestRate / (1 - (1 + monthlyInterestRate) ** (-amountOfMonths))
        return self.monthlyPayment;
    
    def calcTotalLoanWithInterest(self):
        return self.monthlyPayment * (self.years * 12)
    def calcTotalofInterest(self):
        return abs(self.principal - self.calcTotalLoanWithInterest())

    def calcPropertyTax(self):
        self.taxes = self.principal * (self.propTax / 100)
        return self.taxes
    def totalMonthlyPayment(self):
        return self.monthlyPayment + (self.taxes / 12)




def main() -> None:
    # get user data
    myLoan = loanCalculator()
    myLoan.loanCalcHelper()
    print("The monthly loan payment is : $%.2f " % myLoan.calcInterest())
    print("The total amount paid for the life of the loan is : $%.2f " % myLoan.calcTotalLoanWithInterest())
    print("The total amount paid to interest alone is : $%.2f " % myLoan.calcTotalofInterest() )
    print("Your yearly taxes will be : $%.2f " % myLoan.calcPropertyTax())
    print("Your total monthly payment with taxes is : $%.2f " % myLoan.totalMonthlyPayment())

if __name__ == "__main__":
    main()