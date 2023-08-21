# Let us say your expense for every month are listed below,
# January - 2200
# February - 2350
# March - 2600
# April - 2130
# May - 2190
# Create a list to store these monthly expenses and using that find out,

# 1. In Feb, how many dollars you spent extra compare to January?
# 2. Find out your total expense in first quarter (first three months) of the year.
# 3. Find out if you spent exactly 2000 dollars in any month
# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this


expense = [2200,2350,2600,2130,2190]

# 1. In Feb, how many dollars you spent extra compare to January?

extra_spent = expense[1]-expense[0]
print(f"Extra spent in compare to January is : {extra_spent}")


# 2. Find out your total expense in first quarter (first three months) of the year.

first_quarter_expence = expense[0]+expense[1]+expense[2]
print(f"total expense in first quarter (first three months) of the year : {first_quarter_expence}")


# 3. Find out if you spent exactly 2000 dollars in any month
print("Did i spent exactly 2000 dollars in any month : ",2000 in expense)


# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expense.append(1980)
print("added june month expense in array and the array is: ",expense)

# 5. You returned an item that you bought in a month of April and got a refund of 200$. Make a correction to your monthly expense list based on this
april_expense = expense[3]-200
expense[3] = april_expense
print("Expenses after 200$ return in April: ",expense)