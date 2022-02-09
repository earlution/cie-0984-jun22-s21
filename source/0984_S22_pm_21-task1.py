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


def print_members(members):
    print("Register of members:")
    print()
    for member in members:
        print(f"      First name: {member[0]}")
        print(f"       Last name: {member[1]}")
        print(f"    Is volunteer: {member[2]}")      
        if member[2]:
            print(f"  Volunteer area: {member[3]}")
        print(f"    Joining date: {member[4]}")
        print(f"Joining fee paid: {member[5]}")
        print()


def main():
    volunteer_locations = {1: 'pier entrance gate',
                           2: 'gift shop',
                           3: 'painting and decorating'}
    members = []
    intro()
    while True:
        register_member = input("Would you like to register a new member (y/n)? ")
        if register_member.lower() not in ["y", "yes", "yep", "indeed"]:
            break
        print()
        members.append(capture_new_member_details(volunteer_locations))
        print()
    print_members(members)


main()    
