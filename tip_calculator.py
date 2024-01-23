print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
tip_percent = int(input("What percentage tip would you like to give? 10, 20, or 15? "))
tip_calculation = (total_bill*tip_percent)/100
total_bill_pay = total_bill+tip_calculation
split_bill = int(input("How many people to split the bill? "))
each_bill_pay = total_bill_pay/split_bill
final_amount = round(each_bill_pay, 2)
print(f"Each person should pay: ${final_amount}")