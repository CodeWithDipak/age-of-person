'''
Author - CodeWithDipak
Date - 7 nov 2020
purpose - Practice Purpose
'''
'''
Your age in 2090 - Get age or year of birth as an input from the user and tell them the year
when user will complete his or her 100 years. 
Also tell user about his or her age in particular year in taken input from user. 
'''
while True:
    Current_year = 2020
    user = int(input("Enter your age or year of birth date:"))

    if 00 <= user < 100:
        year_age = Current_year - user
        print(f"You will be 100 year old in year {year_age + 100}.")

    elif 1920 < user <= Current_year:
        age1 = user + 100
        print(f"Your 100 year will be completed in {age1}")

        user1 = int(input("Enter a year and we will provide how old you are:"))

        if user1 > user:
            var = user1 - user
            print(f"Your age will be {var}")
        else:
            var1 = user - user1
            print(f"Your age was {var1}")

    elif user > Current_year:
        print("You are not yet born")

    else:
        print("You seems to be one of the oldest person on the earth")

    while True:
        user2 = int(input("Press 1 for continue and 0 for exit:"))
        if user2 == 1:
            break
        elif user2 == 0:
            exit()
        else:
            print("wrong input")
            continue
