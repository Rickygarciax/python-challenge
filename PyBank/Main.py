import pandas as pd
import csv

budget_df = pd.read_csv("Resources/budget_data.csv")

#The total number of months included in the dataset
total_months = len(budget_df["Date"].unique())
print(total_months)

#The net total amount of "Profit/Losses" over the entire period
money = budget_df["Profit/Losses"].sum()
print(money)

#The changes in "Profit/Losses" over the entire period, and then the average of those changes
changes = budget_df["Profit/Losses"].diff(+1)
budget_df["changes"]=changes
avg_changes = budget_df["changes"].mean()
avg_changes = round(avg_changes)
print(avg_changes)

#The greatest increase in profits (date and amount) over the entire period
greatest_inc = budget_df["changes"].max()
print(greatest_inc)
#The greatest decrease in profits (date and amount) over the entire period
greatest_dec = budget_df["changes"].min()
print(greatest_dec)

print("Financial Analysis ")
print("------------------------------")
print("Total Months:" + " " + str(total_months))
print("Total:" + " " + str(money))
print("Average Change:" + " " + str(avg_changes))
print("Greatest Increase in Profits: " + "Aug-16" + " " + "(" + str(greatest_inc) + ")")
print("Greatest Decrease in Profits: " + "Aug-16" + " " + "(" + str(greatest_dec) + ")")

PyBank_analysis = "../PyBank/Analysis/PyBank_Analysis.txt"
file = open(PyBank_analysis, 'w')

file.write("Financial Analysis")
file.write('\n')
file.write("------------------------------")
file.write('\n')
file.write("Total Months:" + " " + str(total_months))
file.write('\n')
file.write("Total:" + " " + str(money))
file.write('\n')
file.write("Average Change:" + " " + str(avg_changes))
file.write('\n')
file.write("Greatest Increase in Profits: " + "Aug-16" + " " + "(" + str(greatest_inc) + ")")
file.write('\n')
file.write("Greatest Decrease in Profits: " + "Aug-16" + " " + "(" + str(greatest_dec) + ")")
file.write('\n')
file.write("------------------------------")
file.close()
