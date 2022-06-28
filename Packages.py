import Distance
import ReadCSV

first_delivery = []
second_delivery = []
third_delivery = []
truck_1_distance = []
truck_2_distance = []
truck_3_distance = []

# Truck leave times
truck_1_leaves = ['8:00:00']
truck_2_leaves = ['9:10:00']
truck_3_leaves = ['11:00:00']

# Set leave times for packages on truck 1
for index, value in enumerate(ReadCSV.get_first_delivery()):
    ReadCSV.get_first_delivery()[index][9] = truck_1_leaves[0]
    first_delivery.append(ReadCSV.get_first_delivery()[index])

# Compare addresses for truck 1
for index, outer in enumerate(first_delivery):
    for inner in Distance.get_address():
        if outer[2] == inner[2]:
            truck_1_distance.append(outer[0])
            first_delivery[index][1] = inner[0]

# Optimize route for truck 1
Distance.get_shortest_route(first_delivery, 1, 0)
total_distance_1 = 0

# Calculate distance for first truck and each package
for index in range(len(Distance.get_truck_1_index())):
    try:
        total_distance_1 = Distance.get_distance(int(Distance.get_truck_1_index()[index]),
                                                 int(Distance.get_truck_1_index()[index + 1]), total_distance_1)

        deliver_package = Distance.get_time_truck_1(Distance.get_current_distance(int(Distance.get_truck_1_index()[index]), int(Distance.get_truck_1_index()[index + 1])))
        Distance.get_truck_1()[index][10] = (str(deliver_package))
        ReadCSV.get_hash_map().update(int(Distance.get_truck_1()[index][0]), first_delivery)
    except IndexError:
        pass

# Set leave times for packages on truck 2
for index, value in enumerate(ReadCSV.get_second_delivery()):
    ReadCSV.get_second_delivery()[index][9] = truck_2_leaves[0]
    second_delivery.append(ReadCSV.get_second_delivery()[index])

# Compare addresses for truck 2
for index, outer in enumerate(second_delivery):
    for inner in Distance.get_address():
        if outer[2] == inner[2]:
            truck_2_distance.append(outer[0])
            second_delivery[index][1] = inner[0]

# Optimize route for truck 2
Distance.get_shortest_route(second_delivery, 2, 0)
total_distance_2 = 0

# Calculate distance for second truck and each package
for index in range(len(Distance.get_truck_2_index())):
    try:
        total_distance_2 = Distance.get_distance(int(Distance.get_truck_2_index()[index]),
                                                 int(Distance.get_truck_2_index()[index + 1]), total_distance_2)

        deliver_package = Distance.get_time_truck_2(Distance.get_current_distance(int(Distance.get_truck_2_index()[index]), int(Distance.get_truck_2_index()[index + 1])))
        Distance.get_truck_2()[index][10] = (str(deliver_package))
        ReadCSV.get_hash_map().update(int(Distance.get_truck_2()[index][0]), second_delivery)
    except IndexError:
        pass

# Set leave times for packages on truck 3
for index, value in enumerate(ReadCSV.get_third_delivery()):
    ReadCSV.get_third_delivery()[index][9] = truck_3_leaves[0]
    third_delivery.append(ReadCSV.get_third_delivery()[index])

# Compare addresses for truck 3
for index, outer in enumerate(third_delivery):
    for inner in Distance.get_address():
        if outer[2] == inner[2]:
            truck_3_distance.append(outer[0])
            third_delivery[index][1] = inner[0]

# Optimize route for truck 3
Distance.get_shortest_route(third_delivery, 3, 0)
total_distance_3 = 0

# Calculate distance for third truck and each package
for index in range(len(Distance.get_truck_3_index())):
    try:
        total_distance_3 = Distance.get_distance(int(Distance.get_truck_3_index()[index]),
                                                 int(Distance.get_truck_3_index()[index + 1]), total_distance_3)

        deliver_package = Distance.get_time_truck_3(Distance.get_current_distance(int(Distance.get_truck_3_index()[index]), int(Distance.get_truck_3_index()[index + 1])))
        Distance.get_truck_3()[index][10] = (str(deliver_package))
        ReadCSV.get_hash_map().update(int(Distance.get_truck_3()[index][0]), third_delivery)
    except IndexError:
        pass

# Get distance of all packages
def total_distance():
    return total_distance_1 + total_distance_2 + total_distance_3

def truck_1_travel():
    return total_distance_1

def truck_2_travel():
    return total_distance_2

def truck_3_travel():
    return total_distance_3
