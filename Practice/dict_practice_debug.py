

def main():
    '''
     this is a bank account management program. User enters the initial
     amount in their account then the program asks the user to enter
     what they spent money on and how much they spent.

     The program is to then subtract that amount from the account then
     display a summary at the end.
     
    '''
    account = float (input("Enter account starting amount $"))

    # create dictionary

    expenses = dict()

    # create accululator variable

    total = account

    # start loop

    another = "y"

    
    while another.lower() == "y":
    
        expense = input("Enter expense name: ")
        amount = float(input("Enter expense amount: "))
        
        # update dictionary
        
        expenses.update({expense:amount})
        
        # subract from account
        
        total = total - amount
        
        another = input("Would you like to enter another expense? (y/n) ")

    account_sum(expenses, account, total)
def account_sum(expenses_dict, start_amount ,end_amount):

    ''' Required parameters
         - a dictionary containing expenses,
         - inital amount in account
         - ending amount

         the function displays the following
         starting amount , list of expenses (name and amount) and remaining
         amount in accout '''

    print("\nStarting Amount $",start_amount,sep="")
    print()
    print (f'{"Expense Calculator":^30}')

    print("-----------------------------------")
    print(f'{"Expense":<20}{"Amount":<7}')
    print("-----------------------------------")

    for key, value in expenses_dict.items():
        
        print(f'{key:<20}{value:<7}')


    print("-----------------------------------")
    print("Closing Amount $", end_amount,sep="") 




if __name__ == "__main__":

    main()
