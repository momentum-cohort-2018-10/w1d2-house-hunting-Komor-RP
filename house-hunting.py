annual_salary = input("Enter your annual salary: ")
portion_saved = input("Enter the percent of your salary to save, as a decimal: ")
rate_of_return = input("Enter the expected annual rate of return [0.04]: ")
total_cost = input("Enter the cost of your dream home: ")
portion_down_payment = input("Enter the percent of your home's cost to save as a down payment [0.25]: ")

annual_salary = float(annual_salary)
portion_saved = float(portion_saved)

if (rate_of_return):
    rate_of_return = float(rate_of_return)

total_cost = float(total_cost)
if (portion_down_payment):
    portion_down_payment = float(portion_down_payment)


def number_of_months(annual_salary, portion_saved, total_cost, portion_down_payment=.25, rate_of_return=.04):
    
    months = 0
    current_savings = 0
    
    while (current_savings < (total_cost * portion_down_payment)):
        
        current_savings = current_savings + (current_savings * (rate_of_return / 12))
        current_savings = current_savings + (portion_saved * annual_salary / 12)
        months += 1
        
    print("Number of months: " + str(months))


number_of_months(annual_salary, portion_saved, total_cost)