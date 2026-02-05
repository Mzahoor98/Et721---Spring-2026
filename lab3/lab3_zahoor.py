"""
Muhammad Zahoor
Feb 3, 2026
Lab 3, conditional statement and loop is python
"""
print("\n----- example 1: set-up of conditional statment -----")
# conditional statement states the flow of the program
age = 11
if(age >=21):
    print("You are an adult")
elif(age<21 and age>=100):
    print("you are a teen")
elif(age<12 and age>0):
    print("You are a kid")
else: 
    print("Unable to read age")

print("\n----- Example 2: for loop -----")
# for loop as a counter to print from 9 to 1, step 1
for n in range(9,0, -1):
    print(n)

    # for loop in a list
    print ("\n----- example 3: for loop in a list -----")
    numbers =[3,6,1,-8,9,-5]
    count_negative = 0
    for m in numbers:
        if m<0:
            count_negative +=1
else:
    print(f"There is/are {count_negative} negative numbers")
# for-else, the else statement will run only after the complete of all iterations in the for loop

print('\nEND OF PROGRAM!')

print("\n----- example 4: while loop as a counter -----")
# while loop to print from-3 to 5, inclusive, step of 2, outpuit --> -3 -1 1 3 5
x = -3
while x<=5:
    print(x)
    x +=2

print("\n----- Example 5: while loop to validate an input -----")
# program collects a number from the user and print if the number is even or odd
# after it, the program will ask the user if another number will be tested
# if the user types 'y' or 'Y' then the prgram will run again
# if the user types any other chracter that is not 'y' or 'Y' the program will stop

decision_user = 'y'
user_number = 0

while True:
    user_number = int(input("Enter a number: "))
    if user_number % 2 == 0 and user_number != 0:
        print(f"{user_number} is EVEN")
    elif user_number == 0:
        print("The number is zero")
    else:
        print(f"{user_number} is ODD")

    decision_user = input("Do you want another run? y or Y for yes: ")
    if decision_user != 'y' and decision_user != 'Y':
        break

print("\n----- EXERCISE 1: validate a number between 1 and 9 -----")
user_number = int(input("Enter a number between 1 and 9: "))

while user_number < 1 or user_number > 9:
    print("Invalid input. Please try again.")
    user_number = int(input("Enter a number between 1 and 9: "))

print("Valid number entered:", user_number)

print("\n----- EXERCISE 2 : Guess a number with 3 attempts -----")
secret_number = 5
attempts = 0

while attempts < 3:
    guess = int(input("Guess the number (1–9): "))
    attempts += 1

    if guess == secret_number:
        print("Correct! You guessed the number.")
        break
    else:
        print("Wrong guess.")

if attempts == 3 and guess != secret_number:
    print("Sorry, you’ve used all three attempts.")


