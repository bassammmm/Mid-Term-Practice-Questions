amount_bor = float(input("Please enter the Amount borrowed in Dollars:"))
interest_r = float(input("Please enter the Interest rate percentage  :"))
time_loan  = int(input("Please enter the Time of the Loan in Years :"))




tot_interest_paid = (interest_r/100)*amount_bor
remaining_bal = tot_interest_paid+amount_bor

tot_months = time_loan*12
payments = remaining_bal/tot_months
payments=float("{0:.2f}".format(payments))
remaining_bal=float("{0:.2f}".format(remaining_bal))

print("\nAmount Borrowed   :$",amount_bor)
print("Total Interst Paid:%",tot_interest_paid)



print("\n\n")
print("_"*66)
print("|{0:^20}|{1:^20}|{2:^20}|".format("#Payments","Amt. Paid","Rem. Bal."))
bill=0
while remaining_bal!=0:
    if bill==0:
        print("|{2:^20}|{0:^20}|{1:^20}|".format("$0","$"+str(remaining_bal),bill))
        bill+=1
    else:
        remaining_bal=float("{0:.2f}".format(remaining_bal))
        payments=float("{0:.2f}".format(payments))
        print("|{2:^20}|{0:^20}|{1:^20}|".format("$"+str(payments),"$"+str(remaining_bal),bill))
        if payments>remaining_bal:
            payments=remaining_bal
            remaining_bal-=payments
        else:
            remaining_bal-=payments
       
        bill+=1
remaining_bal=float("{0:.2f}".format(remaining_bal))
payments=float("{0:.2f}".format(payments))
print("|{2:^20}|{0:^20}|{1:^20}|".format("$"+str(payments),"$"+str(remaining_bal),bill))

