class HashMap:

    # Constructor
    def __init__(self, initial_capacity=10):
        self.map = []
        for i in range(initial_capacity):
            self.map.append([])

    # Creates hash key
    def create_hash_key(self, key):
        return int(key) % len(self.map)

    # Inserts items in the hash table
    def insert(self, key, item):
        bucket = self.create_hash_key(key)
        key_value = [key, item]

        if self.map[bucket] is None:
            self.map[bucket] = list([key_value])
            return True
        else:
            for pair in self.map[bucket]:
                if pair[0] == key:
                    pair[1] = key_value
                    return True
            self.map[bucket].append(key_value)
            return True

    # Updates items in the hash table
    def update(self, key, item):
        bucket = self.create_hash_key(key)
        if self.map[bucket] is not None:
            for pair in self.map[bucket]:
                if pair[0] == key:
                    pair[1] = item
                    print(pair[1])
                    return True
        else:
            print('There was an error updating key: ' + key)

    # Searches for item with matching key
    def search(self, key):
        bucket = self.create_hash_key(key)
        if self.map[bucket] is not None:
            for kv in self.map[bucket]:
                if kv[0] == key:
                    return kv[1]
        return None

    # Removes an item with the matching key
    def remove(self, key):
        bucket = self.create_hash_key(key)
        if self.map[bucket] is None:
            return False
        for i in range(0, len(self.map[bucket])):
            if self.map[bucket][i][0] == key:
                self.map[bucket].pop(i)
                return True
        return False
