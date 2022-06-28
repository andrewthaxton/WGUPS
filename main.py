# Andrew Thaxton Student ID: 001515619

from ReadCSV import get_hash_map
from Packages import total_distance
from Packages import truck_1_travel
from Packages import truck_2_travel
from Packages import truck_3_travel
import datetime

class Main:
    # User interface
    print('WGUPS Route Optimization\n')
    print(f'Truck 1 travelled {truck_1_travel():.2f} miles.')
    print(f'Truck 2 traveled {truck_2_travel():.2f} miles.')
    print(f'Truck 3 traveled {truck_3_travel():.2f} miles.')
    print(f'Route was a total of {total_distance():.2f} miles.\n')

    user_input = input("""
    Please type the number option to continue or 'quit' to quit:
        1. Get info for one package at a chosen time.
        2. Get info for all packages at a chosen time.
    """)

    while user_input != 'quit':
        # Get info for one package
        if user_input == '1':
            try:
                id = input('Enter package ID or "quit" to quit: ')
                sent_time = get_hash_map().search(str(id))[9]
                delivered_time = get_hash_map().search(str(id))[10]
                input_time = input('Enter a time using the format HH:MM:SS ')
                (hrs, mins, secs) = input_time.split(':')
                converted_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins, secs) = sent_time.split(':')
                converted_sent_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                (hrs, mins,secs) = delivered_time.split(':')
                converted_delivered_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))

                if converted_sent_time >= converted_user_time:
                    at_hub = 'At Hub'
                    leave_time = 'Leaves at ' + sent_time
                    print(
                        f'Package ID: {get_hash_map().search(str(id))[0]}\n'
                        f'Street Address: {get_hash_map().search(str(id))[2]}\n'
                        f'Required Delivery Time: {get_hash_map().search(str(id))[6]}\n'
                        f'Package Weight: {get_hash_map().search(str(id))[7]}\n'
                        f'Truck Status: {leave_time}\n'
                        f'Delivery Status: {at_hub}\n'
                    )

                elif converted_sent_time <= converted_user_time:
                    if converted_user_time < converted_delivered_time:
                        en_route = 'En route'
                        leave_time = 'Left at ' + sent_time
                        print(
                            f'Package ID: {get_hash_map().search(str(id))[0]}\n'
                            f'Street Address: {get_hash_map().search(str(id))[2]}\n'
                            f'Required Delivery Time: {get_hash_map().search(str(id))[6]}\n'
                            f'Package Weight: {get_hash_map().search(str(id))[7]}\n'
                            f'Truck Status: {leave_time}\n'
                            f'Delivery Status: {en_route}\n'
                        )

                else:
                    delivered_at = 'Delivered at ' + delivered_time
                    leave_time = 'Left at ' + sent_time
                    print(
                        f'Package ID: {get_hash_map().search(str(id))[0]}\n'
                        f'Street Address: {get_hash_map().search(str(id))[2]}\n'
                        f'Required Delivery Time: {get_hash_map().search(str(id))[6]}\n'
                        f'Package Weight: {get_hash_map().search(str(id))[7]}\n'
                        f'Truck Status: {leave_time}\n'
                        f'Delivery Status: {delivered_at}\n'
                    )
            except ValueError:
                print('Invalid entry')
                exit()

            user_input = input("""
                Please type the number option to continue or 'quit' to quit:
                    1. Get info for one package at a chosen time.
                    2. Get info for all packages at a chosen time.
                """)

        # Get info for all packages
        elif user_input == '2':
            try:
                input_time = input('Enter a time using the format HH:MM:SS or "quit" to quit: ')
                (hrs, mins, secs) = input_time.split(':')
                converted_user_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                for id in range(1, 41):
                    try:
                        sent_time = get_hash_map().search(str(id))[9]
                        delivered_time = get_hash_map().search(str(id))[10]
                        (hrs, mins, secs) = sent_time.split(':')
                        converted_sent_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                        (hrs, mins, secs) = delivered_time.split(':')
                        converted_delivered_time = datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
                    except ValueError:
                        pass

                    if converted_sent_time >= converted_user_time:
                        at_hub = 'At Hub'
                        leave_time = 'Leaves at ' + sent_time
                        print(
                            f'Package ID: {get_hash_map().search(str(id))[0]}, '
                            f'Street Address: {get_hash_map().search(str(id))[2]}, '
                            f'Required Delivery Time: {get_hash_map().search(str(id))[6]}, '
                            f'Package Weight: {get_hash_map().search(str(id))[7]}, '
                            f'Truck Status: {leave_time}, '
                            f'Delivery Status: {at_hub}'
                        )

                    elif converted_sent_time <= converted_user_time:
                        if converted_user_time < converted_delivered_time:
                            en_route = 'En route'
                            leave_time = 'Left at ' + sent_time
                            print(
                                f'Package ID: {get_hash_map().search(str(id))[0]}, '
                                f'Street Address: {get_hash_map().search(str(id))[2]}, '
                                f'Required Delivery Time: {get_hash_map().search(str(id))[6]}, '
                                f'Package Weight: {get_hash_map().search(str(id))[7]}, '
                                f'Truck Status: {leave_time}, '
                                f'Delivery Status: {en_route}'
                            )

                        else:
                            delivered_at = 'Delivered at ' + delivered_time
                            leave_time = 'Left at ' + sent_time
                            print(
                                f'Package ID: {get_hash_map().search(str(id))[0]}, '
                                f'Street Address: {get_hash_map().search(str(id))[2]}, '
                                f'Required Delivery Time: {get_hash_map().search(str(id))[6]}, '
                                f'Package Weight: {get_hash_map().search(str(id))[7]}, '
                                f'Truck Status: {leave_time}, '
                                f'Delivery Status: {delivered_at}'
                            )
            except IndexError:
                print(IndexError)
                exit()
            except ValueError:
                print('Invalid entry')
                exit()

            user_input = input("""
                Please type the number option to continue or 'quit' to quit:
                    1. Get info for one package at a chosen time.
                    2. Get info for all packages at a chosen time.
                """)

        # Exits program
        elif user_input == 'quit':
            exit()

        # Prints Invalid entry and exits program
        else:
            print('Invalid entry')
            exit()

