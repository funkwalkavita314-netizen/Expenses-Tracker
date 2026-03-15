import os

filename="expenses.txt"

expenses=[]

if os.path.exists(filename):
    with open(filename, "r") as file:
        for line in file:
            ctr,amt= line.strip().split(",")
            expenses.append([ctr,float(amt)])
   

while True:
    print("/n===== Expense Tracker =====")
    print('''1.Add Expenses
2.View All Expenses
3.Show total Expenses
4.Show Category-wise total
5.Exit''')

    cho=input("enter your choice.")


    if cho=="1":
        ctr=input("enter category")
        amt=float(input("enter amount"))
        expenses.append([ctr,amt])

        file=open(filename,"a")
        file.write(ctr + "," + str(amt) + "\n")
        file.close()

        print("expenses added and saved")


    elif cho=="2":
        if len(expenses)==0:
            print("no expenses found")
        else:
            print("/n   All Expenses   ")
            for i in range(len(expenses)):
                print(i+1, ",", expenses[i][0], "-", expenses[i][1])

    elif cho=="3":
        total=0
        for item in expenses:
            total += item[1]
            print("Total Expenses=",total)

    elif cho=="4":
        ctr_totals={}

        for ctr,amt in expenses:
            if ctr in ctr_totals:
                ctr_totals[ctr] += amt
            else:
                ctr_totals[ctr]=amt
                print("/n   category wise total   ")

                for cat in ctr_totals:
                    print(cat , "=",ctr_totals[cat])


    elif cho=="5":
        print("goodbye")
        break

    else:
        print("invalid choice")
            
