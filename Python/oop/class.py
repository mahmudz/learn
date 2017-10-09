class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, speed_in_an_hour):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.speed_in_an_hour = speed_in_an_hour

    def destinationReachingTime(self, totalDistance):
        reachingTime = totalDistance / self.speed_in_an_hour
        return reachingTime

    def make_noise(self):
        print('VRUUUUUUUM')


tesla_model_s = Vehicle(4, 'electric', 5, 85)
time_to_reach = tesla_model_s.destinationReachingTime(4884)
print("Tesla Model S needs %.1f hours to reach %d kilometers." %(time_to_reach, 4884))
tesla_model_s.make_noise()