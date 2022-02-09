import pickle

def intro():
    print("*********************************************")
    print("*          Friends of Seaview Pier          *")
    print("*********************************************")
    print()


def capture_new_member_details(volunteer_locations):
    member_details = []
    firstname = ""
    lastname = ""
    volunteer = False
    volunteer_area = "none"
    joining_date = 0
    joining_fee_paid = False

    member_details.append(input("What is your first name? "))
    member_details.append(input("What is your last name? "))
    volunteer_choice = input("Do you wish to work as a volunteer (y/n)? ").lower()
    if volunteer_choice in ["y", "yes", "yeah", "yep", "indeed"]:
        volunteer = True
        volunteer_area = capture_volunteer_area(volunteer_locations)
    member_details.append(volunteer)
    member_details.append(volunteer_area)
    member_details.append(capture_joining_date())
    joining_fee = input("Have you paid the joining fee (y/n)? ").lower()
    if joining_fee in ["y", "yes", "yeah", "yep", "indeed"]:
        joining_fee_paid = True
    member_details.append(joining_fee_paid)   
    return member_details


def capture_volunteer_area(volunteer_locations):
    print("Here are the volunteering areas:")
    for key, value in volunteer_locations.items():
        print(key, value)
    print()
    area_choice = int(input("Please choose an area to volunteer (1, 2 or 3): "))
    while area_choice not in [1, 2, 3]:
        area_choice = input("That is not a valid choice, please choose 1, 2 or 3: ")
    volunteer_area = volunteer_locations[area_choice]
    return volunteer_area


def capture_joining_date():
    joining_date = input("Please enter the date you joined, using the form dd.mm.yyyy: ")
    return joining_date


def save_members(members):
    """Serialise param members to text file.

    :param members:
    2d list; 2nd dimension represents individual member_details lists.
    """
    
    filename = "fsp_members.txt"
    output_file = open(filename, "wb")
    pickle.dump(members, output_file)
    output_file.close()


def load_members():
    filename = "fsp_members.txt"
    input_file = open(filename, "rb")
    members = pickle.load(input_file)
    input_file.close()
    return members

def output_volunteers(members):
    for member in members:
        if member[2] == True:
            print(member[0], member[1])


def output_pier_gate_volunteers(members):
    for member in members:
        if member[3] == "pier entrance gate":
            print(member[0], member[1])


def output_gift_shop_volunteers(members):
    for member in members:
        if member[3] == "gift shop":
            print(member[0], member[1])


def output_paint_decor_volunteers(members):
    for member in members:
        if member[3] == "painting and decorating":
            print(member[0], member[1])


def main():
    volunteer_locations = {1: 'pier entrance gate',
                           2: 'gift shop',
                           3: 'painting and decorating'}
    members = []
    intro()
    answer = True
    while answer:
        print("1. Register a new member")
        print("2. Write members records to file")
        print("3. Load members records from file")
        print("4. Output the first and last names of members in any of a number of categories")
        print("5. Output member by list index")
        print("X. Exit/Quit")
        answer = input("What would you like to do? ")
        print()
        if answer == "1":
            member_details = capture_new_member_details(volunteer_locations)
            members.append(member_details)
            print()
        elif answer == "2":
            save_members(members)
            print()
        elif answer == "3":
            members = load_members()
            print()
        elif answer == "4":
            answer3 = True
            while answer3:
                print("Output categories:")
                print("1. Members who have chosen to work as volunteers.")
                print("2. Volunteers who would like to work at the pier entrance gate")
                print("3. Volunteers who would like to work in the gift shop")
                print("4. Volunteers who would like to help with painting and decorating tasks")
                print("5. Members whose membership has expired (they have not re-joined this year)")
                print("6. Members who have not yet paid their £75 fee.")
                print("X. Return to main menu")
                answer = input("What would you like to do? ")
                print()
                if answer == "1":
                    output_volunteers(members)
                    print()
                elif answer == "2":
                    output_pier_gate_volunteers(members)
                    print()
                elif answer == "3":
                    output_gift_shop_volunteers(members)
                    print()
                elif answer == "4":
                    output_paint_decor_volunteers(members)
                    print()
                elif answer == "5":

                    print()
                elif answer == "6":

                    print()
                elif answer.lower() == "x":
                    print("\nGoodbye") 
                    answer3 = None
                else:
                   print("\n Not Valid Choice Try again")
        elif answer.lower() == "x":
            print("\nGoodbye") 
            answer = None
        else:
           print("\n Not Valid Choice Try again")


main()    
