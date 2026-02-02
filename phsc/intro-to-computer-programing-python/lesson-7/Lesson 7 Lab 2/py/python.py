class Vehicle:
    occupancy_max = 8
    def __init__(self, occupants):
        if occupants > self.occupancy_max:
            print("The maximum occupancy limit has been exceeded.", occupants - self.occupancy_max, "occupants must exit the vehicle")
            self.occupants = self.occupancy
        