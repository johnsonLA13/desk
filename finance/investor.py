# this is a estimator of growth in invetments
import math
import datetime as dt

def add_one_month(t):
    one_day = dt.timedelta(days=1)
    one_month_later = t + one_day
    while one_month_later.month == t.month:
        one_month_later += one_day
    target_month = one_month_later.month
    while one_month_later.day < t.day:
        one_month_later += one_day
        if one_month_later.month != target_month:  # gone too far
            one_month_later -= one_day
            break
    return one_month_later

def main():

    # PERSONAL INFORMATION
    print("\n" + "\033[93m" + "PERSONAL INFORMATION" + "\033[0m")
    birth_date_input = str(input("What is your birth date? (MM/DD/YYYY)  ")) # users birthdate
    birth_date_elements = birth_date_input.split("/")
    birth_year = int(birth_date_elements[2])
    birth_month = int(birth_date_elements[0])
    birth_day = int(birth_date_elements[1])
    birth_date = dt.date(birth_year, birth_month, birth_day)
    birth_date_str = birth_date.strftime("%B %d, %Y")
    print("Your Birthday: ", birth_date_str, "\n")
    
    # June 6, 2020 (2020, 6, 26) = the date two weeks before my first payday with UHG
    start_date = dt.date(2020, 6, 26)
    print("Start Date: ", start_date.strftime("%B %d, %Y"), "\n")
    
    age_in_days = abs(start_date - birth_date).days
    age_in_years = age_in_days // 365
    days = age_in_days % 365
    print ("Your Age (on start date ^): ", age_in_years, "years, ", days, "days", "\n")

    retire_age = int(input("What age do you want to retire?  ")) # number of years to save over
    retire_date = dt.date(birth_year + retire_age, birth_month, birth_day)
    print("Retire Date: ", retire_date.strftime("%B %d, %Y"), "\n")

    # FINANCIAL INFORMATION
    print("\n" + "\033[93m" + "FINANCIAL INFORMATION" + "\033[0m")
    annual_income = float(input("What is your annual income?  "))
    starting_amount = float(input("What is your current account balance?  ")) # total amount starting in the account
    contribution_rate = float(input("What percentage of your income will you be contributing?  %")) /100
    interest_y = float(input("What is your anticipated annual rate of return?  %")) /100 # monthly interest rate
    print("")

    interest_bw = math.pow(interest_y + 1,(1/26)) - 1 # bi-weekly rate of return
    bi_weekly_contribution = (annual_income * contribution_rate)/26 # amount contributed bi-weekly
    days_to_save = (retire_date - start_date).days # number of days to save over


    acc_balance = starting_amount # placeholder for monthly starting amount
    prev_acc_balance = starting_amount
    year_start = starting_amount
    pay_check_counter = 0
    for d in range(1, days_to_save + 1):
        future_date = start_date + dt.timedelta(days=d)
        if future_date.day == 1: # first of the month
            print("\033[95m" + str(future_date.strftime("%B %d, %Y")) + ": " + "\033[0m" + "${:,.2f}".format(round(acc_balance,2)) + "\033[92m" + " (+${:,.2f})".format(round(acc_balance - prev_acc_balance,2)) + "\033[0m")
            prev_acc_balance = acc_balance
        if d % 14 == 0: # pay day
            pay_check_counter += 1
            print("     Pay Day #" + str(pay_check_counter) + " - ", future_date.strftime("%B %d, %Y"))
            acc_balance = acc_balance + (acc_balance * interest_bw) + bi_weekly_contribution
        if (future_date.day == 31 and future_date.month == 12): # last day of December
                year_end = acc_balance
                print("\n" + "\033[94m" + "--------------------------------------" + "\033[0m")
                print("\033[94m" + str(future_date.strftime("%Y")) + " Year End: \n" + "\033[0m" + "    Year start: " + "${:,.2f}".format(round(year_start,2)) + "\n    Year end: " + "${:,.2f}".format(round(year_end,2)) + "\033[92m" + " (+${:,.2f})".format(round(year_end - year_start,2)) + "\033[0m")
                acc_interest_gained = (year_end - year_start) - (pay_check_counter * bi_weekly_contribution)
                print("    Annual interest rate: " + str(100 * round((acc_interest_gained/(((pay_check_counter//2)*bi_weekly_contribution) + year_start)),2)) + "%")
                print("\033[94m" + "--------------------------------------" + "\033[0m" + "\n")
                year_start = year_end
                pay_check_counter = 0


if __name__ == "__main__":
    main()