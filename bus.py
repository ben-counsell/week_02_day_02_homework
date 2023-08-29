from bus_stop import BusStop

class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
    def drive(self):
        return "vroom vroom"
    def passenger_count(self):
        return len(self.passengers)
    def pick_up(self, passenger):
        self.passengers.append(passenger)
    def drop_off(self, passenger):
        self.passengers.remove(passenger)
    def empty_bus(self):
        self.passengers = []
    def pick_up_from_stop(self, bus_stop):
        while len(bus_stop.queue) > 0:
            self.passengers.append(bus_stop.queue[0])
            bus_stop.queue.remove(bus_stop.queue[0])