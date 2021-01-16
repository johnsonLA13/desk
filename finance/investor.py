# this is a estimator of growth in invetments
import math


def main():
    # variables TODO: make this user imput from the console
    # TODO: create a value: month map 

    # personal questions
    age = int(input("What is your age?  "))
    retire_age = int(input("What age do you want to retire?  ")) # number of years to save over
    print("")

    # financial questions
    annual_income = float(input("What is your annual income?  "))
    starting_amount = float(input("What is your current account balance?  ")) # total amount starting in the account
    contribution_rate = float(input("What percentage of your income will you be contributing?  %")) /100
    interest_y = float(input("What is your anticipated annual rate of return?  %")) /100 # monthly interest rate
  
    interest_m = math.pow(interest_y + 1,(1/12)) - 1
    monthly_contribution = (annual_income * contribution_rate)/12 # total amount contributed to the account per month
    months = (retire_age - age) * 12 # number of monthly to save over

    acc_balance = starting_amount #placeholder for monthly starting amount
    year_start = starting_amount
    for m in range(1,months+1):
        acc_balance = acc_balance + (acc_balance * interest_m) + monthly_contribution
        print("Month" + str(m) + ": $" + str(round(acc_balance,2)))
        if (m != 0 and (m % 12 == 0)):
            year_end = acc_balance
            print("Year " + str(m/12) +" total: \n" + "    year start: " + "${:,.2f}".format(round(year_start,2)) + "\n    year end: " + "${:,.2f}".format(round(year_end,2)))
            acc_interest_gained = (year_end - year_start) - 12 * monthly_contribution
            print("    annual interest rate: " + str(100 * round((acc_interest_gained/((6*monthly_contribution) + year_start)),2)) + "%")
            year_start = year_end

if __name__ == "__main__":
    main()