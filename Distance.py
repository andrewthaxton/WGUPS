import csv
import datetime

# Read WGUPS Distance Table files
with open('Distance_Data.csv') as csvfile_1:
    distance_csv = list(csv.reader(csvfile_1, delimiter=','))
with open('Distance_Names.csv') as csvfile_2:
    distance_names = list(csv.reader(csvfile_2, delimiter=','))

    # Get address for package
    def get_address():
        return distance_names

    # Calculate total distance
    def get_distance(row, col, total):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]
        return total + float(distance)

    # Calculate current distance
    def get_current_distance(row, col):
        distance = distance_csv[row][col]
        if distance == '':
            distance = distance_csv[col][row]
        return float(distance)

    truck_1_leaves = ['8:00:00']
    truck_2_leaves = ['9:10:00']
    truck_3_leaves = ['11:00:00']

    # Calculate total distance for truck 1
    def get_time_truck_1(distance):
        new_time = distance / 18
        distance_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_min + ':00'
        truck_1_leaves.append(final_time)
        total = datetime.timedelta()
        for i in truck_1_leaves:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        return total

    # Calculate total distance for truck 2
    def get_time_truck_2(distance):
        new_time = distance / 18
        distance_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_min + ':00'
        truck_2_leaves.append(final_time)
        total = datetime.timedelta()
        for i in truck_2_leaves:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        return total

    # Calculate total distance for truck 3
    def get_time_truck_3(distance):
        new_time = distance / 18
        distance_min = '{0:02.0f}:{1:02.0f}'.format(*divmod(new_time * 60, 60))
        final_time = distance_min + ':00'
        truck_3_leaves.append(final_time)
        total = datetime.timedelta()
        for i in truck_3_leaves:
            (hrs, mins, secs) = i.split(':')
            total += datetime.timedelta(hours=int(hrs), minutes=int(mins), seconds=int(secs))
        return total

    # Lists to represent sorted trucks in order of efficiency
    truck_1 = []
    truck_1_indices = []
    truck_2 = []
    truck_2_indices = []
    truck_3 = []
    truck_3_indices = []

    # Finds the shortest route using Greedy Approach

    def get_shortest_route(delivery, num, current_location):
        if len(delivery) == 0:
            return delivery

        else:
            try:
                lowest_value = 50.0
                location = 0

                for i in delivery:
                    value = int(i[1])
                    if get_current_distance(current_location, value) <= lowest_value:
                        lowest_value = get_current_distance(current_location, value)
                        location = value

                for i in delivery:
                    if get_current_distance(current_location, int(i[1])) == lowest_value:
                        if num == 1:
                            truck_1.append(i)
                            truck_1_indices.append(i[1])
                            delivery.pop(delivery.index(i))
                            current_location = location
                            get_shortest_route(delivery, 1, current_location)
                        elif num == 2:
                            truck_2.append(i)
                            truck_2_indices.append(i[1])
                            delivery.pop(delivery.index(i))
                            current_location = location
                            get_shortest_route(delivery, 2, current_location)
                        elif num == 3:
                            truck_3.append(i)
                            truck_3_indices.append(i[1])
                            delivery.pop(delivery.index(i))
                            current_location = location
                            get_shortest_route(delivery, 3, current_location)
            except IndexError:
                pass

    # Inserts a 0 for the first index of each index list
    truck_1_indices.insert(0, '0')
    truck_2_indices.insert(0, '0')
    truck_3_indices.insert(0, '0')

    # Get Truck 1 list
    def get_truck_1():
        return truck_1

    # Get Truck 2 list
    def get_truck_2():
        return truck_2

    # Get Truck 3 list
    def get_truck_3():
        return truck_3

    # Get Truck 1 index
    def get_truck_1_index():
        return truck_1_indices

    # Get Truck 2 index
    def get_truck_2_index():
        return truck_2_indices

    # Get Truck 3 index
    def get_truck_3_index():
        return truck_3_indices
