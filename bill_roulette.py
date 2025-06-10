# import random

# names_string = input("Give me everyones name but separate them with a comma.\n").split(", ")
# pay_chois = input("in wich way would you like to pay one person or by spliting(one person/spliting).\n")
# print("EVERYONE IS PAYING FOR THE MEALLLL")

# def pay_calc():
#      pay_amount= names_string.__len__() /num_pep
#      print(f"{pay_amount}")


# if pay_chois == "spliting":
#     num_pep=int(input("how many people are willinf to pay?\n"))
#     if num_pep == 0 or num_pep > len(names_string):
#         print("There are not enough people in the group to split the bill  is ther any who is willing to tip you (y/n).")
#         tip = input("Are you willing to tip? (y/n)\n")
#         if tip.lower() == "y":
#             pay_calc()
#         else:
#             print("No one is paying for the meal")
    
#         exit()
#     elif num_pep==names_string.__len__():
#         print("EVERYONE IS PAYING FOR THE MEALLLL")
#         pay_calc()

#     names_string = names_string * int(input("how many people are there in the group?\n"))
# elif pay_chois == "one person":
#     print(f"one person IS PAYING FOR THE MEALLL{random.choice(names_string)}")
#     pay_calc()
# else:
#     print("Please choose one of the options: spliting or one person")

#     exit()




# # names = names_string
# x = len(names_string).randint(0, names_string.__len__() - 1)
# # x = random.randint(0, len(names_string) - 1)
# # n = random
# print(f"TODAY {names_string[x]} IS PAYING FOR THE MEALLLL")


# import random

# def get_names():
#     names_string = input("Give me everyone's names, separated by a comma:\n").strip()
#     return [name.strip() for name in names_string.split(",") if name]
# prosuct_bill=int(input("What is the total bill amount?\n"))
# def get_payment_choice():
#     return input("In which way would you like to pay? (one person/splitting)\n").strip().lower()

# def calculate_split(names, num_pep):
#     if num_pep > 0 and num_pep <= len(names):
#         pay_amount = prosuct_bill / num_pep  # Assuming a total bill of 100 for demonstration
#         print(f"Each person pays: ${pay_amount:.2f}")
#     else:
#         print("Invalid number of people for splitting.")

# def main():
#     names = get_names()
#     if not names:
#         print("No names provided. Exiting.")
#         return

#     pay_choice = get_payment_choice()

#     if pay_choice == "splitting":
#         num_pep = int(input("How many people are willing to pay?\n"))
#         if num_pep == 0:
#             tip = input("There are not enough people in the group to split the bill. Is there anyone willing to tip? (y/n)\n").strip().lower()
#             if tip == "y":
#                 print("Calculating tip...")
#                 # Add tip calculation logic here if needed
#             else:
#                 print("No one is paying for the meal.")
#         else:
#             calculate_split(names, num_pep)

#     elif pay_choice == "one person":
#         selected_person = random.choice(names)
#         print(f"{selected_person} is paying for the meal!")
#     else:
#         print("Please choose one of the options: splitting or one person.")

# if __name__ == "__main__":
#     main()



import random

def get_names():
    names_string = input("Give me everyone's names, separated by a comma:\n").strip()
    return [name.strip() for name in names_string.split(",") if name]

def get_payment_choice():
    return input("In which way would you like to pay? (one person/splitting)\n").strip().lower()

def calculate_split(names, num_pep, total_bill):
    if num_pep > 0 and num_pep <= len(names):
        pay_amount = total_bill / num_pep
        print(f"Each person pays: ${pay_amount:.2f}")
    else:
        print("Invalid number of people for splitting.")

def main():
    names = get_names()
    if not names:
        print("No names provided. Exiting.")
        return

    try:
        total_bill = float(input("What is the total bill amount?\n"))
    except ValueError:
        print("Please enter a valid number for the bill amount.")
        return

    pay_choice = get_payment_choice()

    if pay_choice == "splitting":
        try:
            num_pep = int(input("How many people are willing to pay?\n"))
            if num_pep == 0:
                tip = input("There are not enough people in the group to split the bill. Is there anyone willing to tip? (y/n)\n").strip().lower()
                if tip == "y":
                    print("Calculating tip...")
                    # Implement tip calculation logic here
                else:
                    print("No one is paying for the meal.")
            else:
                calculate_split(names, num_pep, total_bill)
        except ValueError:
            print("Please enter a valid number for the number of people.")
    elif pay_choice == "one person":
        selected_person = random.choice(names)
        print(f"{selected_person} is paying for the meal!")
    else:
        print("Please choose one of the options: splitting or one person.")

if __name__ == "__main__":
    main()
