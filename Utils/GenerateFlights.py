from datetime import date, datetime, time, timedelta
from random import randint, randrange

from DataStructures.Flight import Flight
from DataStructures.LocationTypes import BaseLocation, Country, USState, Airport
from Utils.CustomExceptions import InvalidModeException
from Utils.Utils import LocationsDB as LBD, get_random_list_item

"""
Methods for the purpose of generating flight instances. """

num_flights_counter = 100

def _random_date_in_range(start_date:date, end_date:date) -> date:
    return start_date + timedelta(randrange((end_date - start_date).days))

def random_time_in_range(start_time:time, end_time:time) -> time:
    """
    Generate a random time betwen two ranges.

    Args:
        start_time (time): lower bound of range in which to select date.
        end_time (time): higher bound of range in which to select date.

    Returns: time:
        Randomly generated time between start_time and end_time with minutes
        limited to increments of five.  """

    start_hour = start_time.hour()
    start_min = start_time.min()
    end_hour = end_time.hour()
    end_min = end_time.min()
    
    def down_tenth(i:int) -> int:
        return i - (i%10)
    
    return time(
        hour=randint(start_hour, end_hour),
        minute=down_tenth(randint(start_min, end_min)))
    
def random_time_from_mode(mode:int=0) -> time:
    """
    Method for selecting an approximate time of day. Mode determins the ranges
    of hours from which to randomly select. Minutes are randomly selected in 5
    minute increments.

    Args:
        mode (int, optional):
            0 -> 24 hr range (default)
            1 -> Morning
            2 -> Night
            3 -> Morning
            4 -> Afternoon
            5 -> Evening
            6 -> Late evening/early night

    Raises: InvalidModeException: If less than 0 or greater than 6.

    Returns: time: A randomized time object from the selected range.    """
        
    if mode == 0:
        hour_range = (0, 24)
    elif mode == 1:
        hour_range = (8, 17)
    elif mode == 2: # Red eye
        hour_range = [(18, 24), (0, 8)][randint(0, 1)]
    elif mode == 3:
        hour_range = (6, 12)
    elif mode == 4:
        hour_range = (12, 16)
    elif mode == 5:
        hour_range = (16, 20)
    elif mode == 6:
        hour_range = (20, 24)
    else:
        raise InvalidModeException(mode, 0, 7)
    
    return time(hour=randrange(*hour_range),
                minute=randrange(0, 59, 5))
    

def generate_flights(num_flights:int,
                     origin_range:list[type[str]],
                     dest_range:list[type[str]],
                     flight_date_l_r:date=None,
                     flight_date_h_r:date=None,
                     depart_time_l_r:time=None,
                     departure_time_h_r:time=None,
                     duration_l_r:int=None,
                     duration_h_r:int=None,
                     departure_time_mode:int=None) -> list[Flight]:
    
    global num_flights_counter
    flights_list = []
    
    flight_date_l_r = date.today() \
        if flight_date_l_r is None else flight_date_l_r
    
    flight_date_h_r = date.today() + timedelta(weeks=1) \
        if flight_date_h_r is None else flight_date_l_r
    
    for _ in range(num_flights):
        
        # Find departure & arrival airports.
        origin_airport = get_random_list_item(
            LBD.find_airports_obj(origin_range[randint(0, len(origin_range) -1)]))
        
        destination_airport = get_random_list_item(
            LBD.find_airports_obj(dest_range[randint(0, len(dest_range) -1)]))
        
        flight_date = \
            _random_date_in_range(flight_date_l_r, flight_date_h_r)
        
        # Departure & arerival times
        if departure_time_mode is not None:
            departure_time = random_time_from_mode(departure_time_mode)
            
        elif depart_time_l_r is not None and departure_time_h_r is not None:
            departure_time = \
                random_time_in_range(depart_time_l_r, departure_time_h_r)
                
        else:
            departure_time = random_time_from_mode()
            
        departure_datetime = datetime.combine(flight_date, departure_time)
        
        # Duration
        if duration_l_r is None or duration_h_r is None:
            flight_duration = randint(1, 8)
        else:
            flight_duration = randint(duration_l_r, duration_h_r)
        
        arrival_datetime = departure_datetime + timedelta(hours=flight_duration)

        flights_list.append(
            Flight(num_flights_counter, origin_airport, destination_airport,
                   departure_datetime, arrival_datetime))
        
        num_flights_counter += 1
        
    return flights_list