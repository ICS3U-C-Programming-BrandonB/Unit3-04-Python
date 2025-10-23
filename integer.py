#!/usr/bin/env python3

# Created By: Brandon
# Date: October 23rd, 2025
# This program asks the user for their number, determines whether its negative, positive or zero and
# displays the corresponding message


def main():

    # get the number from the user
    user_guess = int(input("Enter A Number: "))
    # determine whether or not the user guessed correctly
    if user_guess > 0:
        print("You have entered a positive number")
    # determine whether or not the user guessed correctly
    elif user_guess < 0:
        print("You have entered a negative number")
    else:
        print("Your number is zero")


# outputs the function
if __name__ == "__main__":
    main()
