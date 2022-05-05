SALES_TAX = .07
TIP_PERCENTAGE = .18

cost_of_food = float(input ("Please enter the charge for the food: "))

subtotal = cost_of_food
servers_tip = (cost_of_food * TIP_PERCENTAGE)
sales_tax = (cost_of_food * SALES_TAX)
total = cost_of_food + servers_tip + sales_tax

print("\nSubtotal:\t$", format(subtotal, "7,.2f"))
print("Tax(7.00%):\t$", format(sales_tax, "7,.2f"))
print("Tip(18.00%):\t$", format(servers_tip, "7,.2f"))
print("============    =========")
print("Total:\t\t$", format(total, "7,.2f"))
