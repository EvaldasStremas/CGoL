available_flights = [
    {"from": "City Y", "to": "City X", "price": 60, "flight id": "000"},
    {"from": "City X", "to": "City Z", "price": 78, "flight id": "001"},
    {"from": "City Y", "to": "City T", "price": 91, "flight id": "002"},
    {"from": "City Z", "to": "City Y", "price": 58, "flight id": "003"},
    {"from": "City E", "to": "City X", "price": 100, "flight id": "004"},
    {"from": "City T", "to": "City W", "price": 49, "flight id": "005"},
    {"from": "City Z", "to": "City T", "price": 45, "flight id": "006"},
    {"from": "City X", "to": "City W", "price": 205, "flight id": "007"},
    {"from": "City Z", "to": "City T", "price": 56, "flight id": "008"},
    {"from": "City W", "to": "City T", "price": 40, "flight id": "009"},
    {"from": "City Y", "to": "City M", "price": 50, "flight id": "010"},
    {"from": "City X", "to": "City W", "price": 45, "flight id": "011"},
    {"from": "City X", "to": "City W", "price": 35, "flight id": "012"},
];

class Flight:

    fromCity = ""
    toCity = ""
    
    def __init__(self):
        pass

    def addFields(self, data):
        self.fromCity = data["from"]
        self.toCity = data["to"]
        self.price = data["price"]
        self.id = data["flight id"]

    def __str__(self):
        return "{} {} {} {}".format(self.fromCity, 
        self.toCity,
        self.price,
        self.id
        )

class FlightTable:

    _accessCount = 0
    _flights = []

    def __init__(self, flights):
        for fl in flights:
            fli = Flight()
            fli.addFields(fl)
            self._flights.append(fli)

    def getFlights(self):
        self._accessCount += 1
        return self._flights

    def addFlight(self, data):
        fl = Flight()
        self._fli

    def get_fromCity_list(self):
        return self._flights
    
    def print_flights(self):
        a = []
        for item in self._flights:
            print(item.fromCity)

# Get all flight ids for flights that are going to 'city t'
    def get_ids_to_city(self, city):
        ids_list = []

        for flight in self._flights:
            if flight.toCity == city:
                ids_list.append(flight.id)
        
        return ids_list

# Get all available destinations for every city mentioned in the input
    def get_availables_to_cities(self, input_city):
        available_cities = []

        for flight in self._flights:

            if input_city == flight.toCity:
                available_cities.append(flight.fromCity)

        return available_cities

# Get cheapest roundtrip from 'city x' to 'city w'
    def get_cheapest_roundtrip(self):
        price_list = []
        target_destinations = []

        for flight in self._flights:
            if flight.fromCity == 'City X':
                if flight.toCity == 'City W':
                    target_destinations.append(str(flight))
            
        price_list.append(flight.price)
        price_list.sort()
        lowest_price = price_list[0]

        for target in target_destinations:
            target = target.split()
            if str(lowest_price) in target:
                lowest_price_flight = target

        return lowest_price_flight

flighttable = FlightTable(available_flights)
flights = flighttable.getFlights()
fromCity = flighttable.get_fromCity_list()

# print(fromCity)
# flighttable.print_flights()
print(flighttable.get_ids_to_city('City X'))
print(flighttable.get_availables_to_cities('City X'))
print(flighttable.get_cheapest_roundtrip())