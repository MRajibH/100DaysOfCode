class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_Passengers(self, name):
        if not self.availableSeats():
            return False
        self.passengers.append(name)
        return True

    def availableSeats(self):
        return self.capacity - len(self.passengers)


capacity = Flight(2)
people = ["Rajib", "Salman", "Merajul", "Arifin"]
for person in people:
    success = capacity.add_Passengers(person)
    if success:
        print(f'Congratulations! {person} added to the flight succesfully.')
    else:
        print(f'Sorry! No available set for {person}')
