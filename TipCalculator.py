#!/usr/bin/env python3

#creating a tip calator that allows us to choose what percentage tip we would like to give
print("Welcome to the tip calculator 😄")
total_bill = float(input("What is the total bill? £"))
tip=int(input("What percentage bill would you like to give: 10, 12, or 15? "))
people= int(input("How many people to split the bill? "))
total_bill_float= round(float(total_bill),2)

bill_with_tip= round((tip /100 * total_bill + total_bill),2)
bill_per_person = (bill_with_tip / people)
final_bill="{:.2f}".format(bill_per_person)
print(f"Your bill before tip is £{total_bill_float}, your bill with tip is £{bill_with_tip}, Your bill divided by {people} people is £{final_bill}")


