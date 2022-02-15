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

def sponsor_plank():
    confirm = True
    while confirm:
        sponsor_name = capture_sponsor()
        plaque_names = capture_sponsor_names()
        message = capture_sponsor_message()
        sponsor_info = dict()
        sponsor_info['sponsor'] = sponsor_name
        sponsor_info['plaque names'] = plaque_names
        sponsor_info['message'] = message
        confirm = confirm_info(sponsor_info)
    return sponsor_info


def capture_sponsor():
    sponsor_name = input('Enter the name of the person sponsoring the plaque (does not have to appear on plaque): ')
    return sponsor_name


def capture_sponsor_names():
    plaque_names = list()
    while True:
        plaque_name = input('Enter the name of a person to appear on the plaque: ')
        plaque_names.append(plaque_name)
        another = input('Do you want to add another name (Y/N)? ')
        if another.lower() in ['n', 'no', 'nay', 'nope', 'negative']:
            break
    return plaque_names


def capture_sponsor_message():
    print('Please enter the message you wish to appear on the plaque: ')
    message = input()
    return message


def confirm_info(sponsor_info):
    confirm = False
    while True:
        print('This is the information you have provided:')
        print('Name(s):')
        for name in sponsor_info['names']:
            print(f' {name}')
        print('Message:')
        print(f' {message}')
        print()
        print('Please check for errors in the provided information.')
        print('In the case of an error, you will re-enter your information.')
        confirm = input('Please confirm the information is as you intend (Y/N): ')
        positive_confirmation = ['yes', 'y', 'yeah', 'yep', 'positive']
        if confirm.lower() in positive_confirmation:
            confirm = True
            break
    return confirm


def main():
    menu_options = {'1': 'Register a new member',
                    '2': 'Write members records to file',
                    '3': 'Load members records from file',
                    '4': 'Output the first and last names of members in any of a number of categories',
                    '5': 'Output member by list index',
                    '6': 'Sponsor pier plank',
                    'X': 'Exit/Quit'}
    volunteer_locations = {1: 'pier entrance gate',
                           2: 'gift shop',
                           3: 'painting and decorating'}
    members = []
    intro()
    answer = True
    while answer:
        for key, value in menu_options.items():
            print(key, value)
        print()
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
        elif answer == "5":
            raise NotImplementedError
        elif answer == "6":
            sponsor_info = sponsor_plank()
            print()
        elif answer.lower() == "x":
            print("\nGoodbye") 
            answer = None
        else:
           print("\n Not Valid Choice Try again")


main()
