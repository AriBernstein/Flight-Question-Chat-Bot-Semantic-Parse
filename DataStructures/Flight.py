from datetime import datetime

from DataStructures.LocationTypes import Airport

class Flight:
    
    def __init__(self, flight_number:int, origin:Airport, destination:Airport, 
                 departure_time:datetime, arrival_time:datetime) -> None:
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        
    def __eq__(self, __o: object) -> bool:
        if isinstance(__o, Flight):
            return self.flight_number == __o.flight_number and \
                self.origin == __o.origin and \
                    self.destination == __o.destination and \
                        self.departure_time == __o.departure_time and \
                            self.arrival_time == __o.arrival_time
        return False
        
    def __str__(self) -> str:
        return f"Flight {self.flight_number}, {self.origin.abbr()} -> " + \
            f"{self.destination.abbr()}, departing {self.departure_time}"
            
    def __repr__(self) -> str:
        return f"Flight {self.flight_number} ({self.origin.abbr()} -> " + \
            f"{self.destination.abbr()})"