# (Credit Limit Calculator) Develop a python application that determines whether any of
# several department-store customers has exceeded the credit limit on a charge account. For each customer,the
# following facts are available: (a)  account number (b) balance at the beginning of the month (c)total of all
# items charged by the customer this month (d) total of all credits applied to the customer’s account this
# month (e)   allowed credit limit.The program should input all these facts as integers, calculate the new balance
# (= beginning balance+ charges – credits), display the new balance and determine whether the new balance exceeds
# the customer’s credit limit. For those customers whose credit limit is exceeded, the program should dis-play the
# message "Credit limit exceeded".

def creditLimitCalculator():
    acctNumber = int(input("Enter account number: "))
    balance = int(input("Enter balance at the beginning of the month :"))
    totalItemsCharged = int(input("total of all items charged by the customer this month: "))
    creditApplied = int(input("total of all credits applied to the customer’s account this month: "))
    allowedCredit = int(input("allowed credit limit: "))

    newBalance = balance + totalItemsCharged - allowedCredit

    if newBalance > allowedCredit:
        print(f'new balance is {newBalance}')

    else:
        print('Credit limit has been Exceeded')


creditLimitCalculator()
