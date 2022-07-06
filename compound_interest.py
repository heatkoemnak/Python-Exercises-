
while True:



  #reciving the data from user
    A=float(input("Enter Amount: "))#deposit amount
    W=float(input("Enter Interest rate: ")) #interest rate
    N=int(input("Enter month: "))#each month

  
    print("\n{:<10} {:<15} {:<20} {:<25} {:<25} {:<30}".format("Month", "Deposit", "Total Deposit", "This Month's interest", "Total-Interest Earned", "Total-value to-Date"))
    print("_"*120)#print line
    Last_int = 0#last month interest

    for x in range(N):

        month = x+1 
        total_dep = (A*month)
        F = A*(pow((1+W/1200),month))
        month_int = F - A #This month's interest
        total_int = Last_int + month_int   #Total interest Earned
        Last_int += month_int
        total_value = Last_int + total_dep  #total-value to Date
        print("{:2}".format(month),
          "{:14}".format(A),
          "{:18}".format(total_dep),
          "{:23.2f}".format(month_int),
          "{:29.2f}".format(total_int),
          "{:26.2f}".format(total_value))#print(space & decimal place bettween data each posittion)
        print("_"*120)#print line

    check = input("Do you want to quit or start gain, enter Y to restart or another to end ?:")
    if check.upper() == "Y": #loop back to the start


        continue



    print("Bye..!Have a nice day")

    break #exit the program