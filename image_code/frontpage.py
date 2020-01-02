## add 2 numbers together
def add_two_numbers(num1, num2):
    total = num1 + num2
    print(f'Total = {total}')
    return (total)

## return the largest of 2 numbers
def largest_number(number_1, number_2):
  if number_1 < number_2:
    return(number_2)
  elif number_1 > number_2:
    return(number_1)
  else:
    return(0)

## validate that param is a number
def validate_num(test_num):
    if test_num.isdigit:
        return true
    
## setup and display main menu for terminal app
def show_menu():
    valid_options=['1','2','3','4']
    balance = 0
    while True:
        clear()
        print('1. Balance')
        print('2. Deposit')
        print('3. Withdraw')
        print('4. Exit')
        user_choice = input('\nPlease Choose an option: ')
        if user_choice in valid_options:
            if user_choice == '1':
                print(f'\nYour balance is ${balance}')
                sleep(2)
            elif user_choice == '2':
                deposit_amt=input('\nEnter the deposit amount in $')
                balance=deposit(balance,deposit_amt)
            elif user_choice == '3':
                withdraw_amt=input('\nEnter the withdraw amount in $')
                balance=withdraw(balance,withdraw_amt)
            elif user_choice == '4':
                clear()
                print('\nThankyou for using the system')
                break
        else:
            print('\nIncorrect selection - try again')
            sleep(2)

O(n)

O(log2n)

big-O

O(n^2)

O(1)

CREATE TABLE Soccer
(
    Match VARCHAR,
    HomeGoal INTEGER,
    AwayGoal INTEGER
);

INSERT INTO Soccer VALUES
('Match A', 2, 4),
('Match B', 2, 2),
('Match C', 4, 1),
('Match D', 2, 0),
('Match E', 2, 1),
('Match F', 2, 2),
('Match G', 1, 3),
('Match H', 3, 3);

SELECT MATCH, HomeGoal, AwayGoal,
CASE
    WHEN HomeGoal > AwayGoal THEN 'Home Team Won'
    WHEN HomeGoal < AwayGoal THEN 'Away Team Won'
    ELSE "It is a draw"
END AS Result
FROM Soccer;


