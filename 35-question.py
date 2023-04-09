loan_amount = float(input("Enter loan amount: "))
num_years = int(input("Enter number of years: "))

print("{:<20} {:<20} {}".format("Interest rate", "Monthly payment", "Total payment"))

for i in range(500, 826, 5):
    interest_rate = i / 10000
    num_months = num_years * 12
    monthly_rate = interest_rate / 12
    monthly_payment = (loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -num_months)*10
    total_payment = monthly_payment * num_months
    
    print("{:<20.3f} {:<20.2f} {:.2f}".format(interest_rate * 100, monthly_payment, total_payment))
