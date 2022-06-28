import csv
from HashTable import HashMap

with open('WGUPS Package File.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    hash_table_insert = HashMap()  # Creates HashMap object
    first_delivery = []  # List for first truck delivery
    second_delivery = []  # List for second truck delivery
    third_delivery = []  # List for third truck delivery

    # Reads values from CSV file and inserts into Hash Table as key:value pairs
    for row in readCSV:
        package_ID = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zipcode = row[4]
        delivery = row[5]
        size = row[6]
        note = row[7]
        delivery_start = ''
        address_location = ''
        delivery_status = 'At hub'
        iterate_value = [package_ID, address_location, address, city, state, zipcode, delivery, size, note,
                         delivery_start, delivery_status]

        key = package_ID
        item = iterate_value

        # Adds the package constraints to determine which packages are loaded on which truck.
        if item[6] != 'EOD':
            if 'Must' in item[8] or 'None' in item[8]:
                first_delivery.append(item)
        if 'Can only be' in item[8]:
            second_delivery.append(item)
        if 'Delayed' in item[8]:
            second_delivery.append(item)
        if '84104' in item[5] and '10:30' not in item[6]:
            third_delivery.append(item)
        if 'Wrong address listed' in item[8]:
            item[2] = '410 S State St'
            item[5] = '84111'
            third_delivery.append(item)
        if item not in first_delivery and item not in second_delivery and item not in third_delivery:
            second_delivery.append(item) if len(second_delivery) < len(third_delivery) else third_delivery.append(item)

        hash_table_insert.insert(key, item)

    # Gets list of package items
    def get_hash_map():
        return hash_table_insert

    # Gets list of packages in the first delivery
    def get_first_delivery():
        return first_delivery

    # Gets list of packages in the second delivery
    def get_second_delivery():
        return second_delivery

    # Gets list of packages in the third delivery
    def get_third_delivery():
        return third_delivery
