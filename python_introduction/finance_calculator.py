monthly_income = input("Enter your monthly income: ")
monthly_expenses = input("Enter your total monthly expenses: ")

monthly_savings = float(monthly_income) - float(monthly_expenses)
print("Your monthly savings is: ", monthly_savings)

annual_savings = float(monthly_savings * 12 + float(monthly_savings * 0.05 * 12))
print(f"Projected savings after one year, with interest, is: annual_savings")