
# This code is the Module 1 Challenge Submission from Greg Richardson

# Import Libraries
import csv
from pathlib import Path

# Separator for the output
print()
print("*******" * 10)
print("Overview of Loan Portfolio")
print("*******" * 10)

# Define list variable and assign values for loan costs
loan_costs = [500, 600, 200, 1000, 450]

# Number of loans in the list
number_of_loans = len(loan_costs)
print(f"There are {number_of_loans} loans in this portfolio.")

# Sum of all loans in the list
sum_of_loans = sum(loan_costs)
print(f"The sum of loans in this portfolio is ${sum_of_loans:.2f}.")

# Average loan amount from the list
avg_of_loans = sum_of_loans / number_of_loans
print(f"The average of loans in this portfolio is ${avg_of_loans:.2f}.")

# Separator for the output
print()
print("*******" * 10)
print("Retrieved Values from a Loan")
print("*******" * 10)

# Loan Data Dictionary
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Get and print additional information for Future Value and Remaining Months from the loan dictionary variable.
future_value = loan.get("future_value")
print(f"The future value of this loan is ${future_value:.2f}")
remaining_months = loan.get("remaining_months")
print(f"The remaining months for this loan is {remaining_months}")

# Separator for the output
print()
print("*******" * 10)
print("Present Value for the Loan")
print("*******" * 10)

loan_price = loan.get("loan_price")
discount_rate = 0.20
present_value = future_value / (1 + discount_rate / 12) ** remaining_months
print(f"The present price of this loan is ${loan_price:.2f}.")
print(f"The present value of this loan is ${present_value:.2f}.")

# Separator for the output
print()
print("*******" * 10)
print("Analysis of Whether to Buy the Loan or Not")
print("*******" * 10)

# Condition to determine whether to buy loan or not
if present_value >= loan_price:
    print(f"This loan is currently worth at least the ${loan_price:.2f} price, so you should buy it!")
else:
    print(f"this loan is not worth the ${loan_price:.2f} price, so you should not buy it.")

# Separator for the output
print()
print("*******" * 10)
print("Analysis of a New Loan Using a Function")
print("*******" * 10)

# Define dictionary variable and assign new loan data
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Define function to calculate and return present value using three arguments
def calculate_present_value(future_value, remaining_months, annual_discount_rate):
    present_value = future_value / (1 + annual_discount_rate / 12) ** remaining_months
    return present_value

# Get values from new loan dictionary variable
future_value = new_loan.get("future_value")
remaining_months = new_loan.get("remaining_months")

# Set annual discount rate variable
annual_discount_rate = 0.20

# Call function to calculate present value and set return value to present_value
present_value = calculate_present_value(future_value, remaining_months, annual_discount_rate)

print(f"The present value of the new loan is ${present_value:.2f}")

# Separator for the output
print()
print("*******" * 10)
print("Conditionally Filtered List of Loans")
print("*******" * 10)

loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Create an empty list variable to hold inexpensive loans
inexpensive_loans = []

# Loop through all the loans and append any that cost $500 or less to the inexpensive loans list
for loan in loans:
    if loan["loan_price"] <= 500:
        inexpensive_loans.append(loan)

# Print the inexpensive loans list
print(inexpensive_loans)

# Separator for the output
print()
print("*******" * 10)
print("Outputting Inexpensive Loans to CSV File")
print("*******" * 10)

# Set the output header to a list variable
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path
output_path = Path("inexpensive_loans.csv")

# Write the header row and each row of loan values from the inexpensive loans list
with open(output_path, 'w', newline='') as csvfile:
    print(f"Now writing {len(inexpensive_loans)} inexpensive loan(s) to CSV file indexpensive_laons.csv.")
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())

# Separator for the output
print()
print("*******" * 10)
print("End of Program")
print("*******" * 10)
print()