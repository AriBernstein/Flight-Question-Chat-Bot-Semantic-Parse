from typing import Type

from Utils.GenerateLocations import generate_location_objects
from Utils.CustomExceptions import InvalidModeException
from DataStructures.LocationTypes import USState, City, Airport
        
class StaticClass:
    """
    Quick hack to make static classes.  """
    
    def __init__(self) -> None:
        raise TypeError("Static classes cannot be instantiated")

class LocationsDB(StaticClass):
    states_dict, cities_dict, airports_dict, states_to_cities, \
        states_to_airports, cities_to_airports, state_abbr_to_state, \
            city_abbr_to_city, airport_names_to_faa = generate_location_objects()
            
    @staticmethod
    def _loc_exists(loc_str:str, mode:int) -> tuple[str, int]:
        """
        Args:
            loc_str (str): possible location from input.
            code (int): 1. State, 2. City, 3. Airport

        Returns:
            tuple[str, int]: string in format to query for state, city, or
                country from the dictionaries in this class, as well as the 
                number representing which of the three data sets it found. """
        if not 1 <= mode <= 3: raise InvalidModeException(mode, 1, 3)
        
        if mode == 1:
            if loc_str in LocationsDB.state_abbr_to_state:
                return LocationsDB.state_abbr_to_state[loc_str], 1
            if loc_str in LocationsDB.states_dict:
                return loc_str, 1
            return None, None
        
        elif mode == 2:
            if loc_str in LocationsDB.city_abbr_to_city:
                return LocationsDB.city_abbr_to_city[loc_str], 2
            if loc_str in LocationsDB.cities_dict:
                return loc_str, 2
            return None, None
        
        else:
            if loc_str in LocationsDB.airport_names_to_faa:
                return LocationsDB.airport_names_to_faa[loc_str], 3
            if loc_str in LocationsDB.airports_dict:
                return loc_str, 3
            return None, None
        
    @staticmethod
    def query_state(state_str:str) -> USState:
        state_str, _ = LocationsDB._loc_exists(state_str, 1)
        return None if state_str is None else LocationsDB.states_dict[state_str]
    
    @staticmethod
    def query_city(city_str:str) -> City:
        city_str, _ = LocationsDB._loc_exists(city_str, 2)
        return None if city_str is None else LocationsDB.cities_dict[city_str]
    
    @staticmethod
    def query_airport(airport_str:str) -> Airport:
        airport_str, _ = LocationsDB._loc_exists(airport_str, 1)
        return None if airport_str is None else LocationsDB.airports_dict[airport_str]
    
    @staticmethod
    def query_location(loc_str) -> tuple[Type[USState], int]:
        for i in range(1, 4):
            loc_str_new, code = LocationsDB._loc_exists(loc_str_new, i)
            if not loc_str_new is None:
                if code == 1:
                    return LocationsDB.query_state(loc_str), code
                elif code == 2:
                    return LocationsDB.query_city(loc_str), code
                elif code == 3:
                    return LocationsDB.query_airport(loc_str), code
                else:
                    raise Exception(f"location query return code was {code}. That's weird :(")
        return None, None